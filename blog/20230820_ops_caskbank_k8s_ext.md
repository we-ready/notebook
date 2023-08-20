---
id: 20230820_ops_caskbank_k8s_ext
title: Caskbank k8s 集群证书过期的运维处置
subtitle: 如何应对 caskbank 项目中 k8s 集群证书过期问题
subject: 云原生
category: 指导手册
tags: kubernetes;k8s;Ingress;calico;LENS;caskbank
keywords: kubeadm;k8s集群;caskbank
level: 200
cover: http://qiniuargus.weready.online/blog/tech_logos.png
authors: Chris Wei
created_when: 2023-08-20
updated_when: 2023-08-20
---

# k8s 集群证书过期的处置步骤

## 参考

- 20210125003_k8s_cluster_setup

## 问题的具体表现

> 执行 `kubectl get pods` 命令报错：证书过期

> 错误提示

```
Unable to connect to the server: x509: certificate has expired or is not yet valid
```

## 问题的检查确认及必要准备

1. 登录 master 节点

2. 执行命令，查看证书有效期（简单查看）

```
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text |grep ' Not '
```

3. 详细查看

```
cd /etc/kubernetes
ls
```

```
cd /etc/kubernetes/pki
openssl x509 -in apiserver.crt -noout -text |grep ' Not '
kubeadm alpha certs check-expiration
```

详细结果

```
[root@k8s-m1 ~]# openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text |grep ' Not '
            Not Before: Jul  8 03:24:35 2020 GMT
            Not After : Jul  8 03:24:35 2021 GMT
```

```
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Jul 08, 2021 03:24 UTC   <invalid>                               no      
apiserver                  Jul 08, 2021 03:24 UTC   <invalid>       ca                      no      
apiserver-etcd-client      Jul 08, 2021 03:24 UTC   <invalid>       etcd-ca                 no      
apiserver-kubelet-client   Jul 08, 2021 03:24 UTC   <invalid>       ca                      no      
controller-manager.conf    Jul 08, 2021 03:24 UTC   <invalid>                               no      
etcd-healthcheck-client    Jul 08, 2021 03:24 UTC   <invalid>       etcd-ca                 no      
etcd-peer                  Jul 08, 2021 03:24 UTC   <invalid>       etcd-ca                 no      
etcd-server                Jul 08, 2021 03:24 UTC   <invalid>       etcd-ca                 no      
front-proxy-client         Jul 08, 2021 03:24 UTC   <invalid>       front-proxy-ca          no      
scheduler.conf             Jul 08, 2021 03:24 UTC   <invalid>                               no      

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Jul 06, 2030 03:24 UTC   8y              no      
etcd-ca                 Jul 06, 2030 03:24 UTC   8y              no      
front-proxy-ca          Jul 06, 2030 03:24 UTC   8y              no      
```

> `ca`, `etcd-ca`, `front-proxy-ca` 这三个证书有效期8年，并未过期。其他 10 个证书已经过期。

4. 备份证书 及 k8s 配置文件

```
cd /
cd ~
mkdir backup
cp -r /etc/kubernetes ./backup/etc_k8s_2023
ls ./backup/etc_k8s/
```

5. 登录 k8s 工作节点

6. 查找 dbpg pod

```
docker ps
```

找到 `k8s_dbpg-container`

7. 进入容器

```
docker exec -it 0d36 /bin/bash
```

8. 备份数据库

```
cd script
pg_dump -h dbpg -U postgres archellis > 20230820.yunzhi.bak
```

9. 退出容器

```
exit
```

10. 检查备份文件

```
cd ~/projects/caskbank/database/script
ls
```

11. 异地备份

```
scp 20230820*.bak 172.17.64.152:~/projects/dbdump/202308
```

## 问题解决的实际操作（k8s主节点）

1. 手动更新证书

```
cd /etc/kubernetes/pki
kubeadm alpha certs renew all
```

2. 检查证书有效期

```
openssl x509 -in apiserver.crt -noout -text |grep ' Not '
kubeadm alpha certs check-expiration
```

```
[root@k8s-m1 pki]# openssl x509 -in apiserver.crt -noout -text |grep ' Not '
            Not Before: Jul  8 03:24:35 2020 GMT
            Not After : Jul 17 01:01:13 2022 GMT
```

```
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Jul 17, 2022 01:01 UTC   364d                                    no      
apiserver                  Jul 17, 2022 01:01 UTC   364d            ca                      no      
apiserver-etcd-client      Jul 17, 2022 01:01 UTC   364d            etcd-ca                 no      
apiserver-kubelet-client   Jul 17, 2022 01:01 UTC   364d            ca                      no      
controller-manager.conf    Jul 17, 2022 01:01 UTC   364d                                    no      
etcd-healthcheck-client    Jul 17, 2022 01:01 UTC   364d            etcd-ca                 no      
etcd-peer                  Jul 17, 2022 01:01 UTC   364d            etcd-ca                 no      
etcd-server                Jul 17, 2022 01:01 UTC   364d            etcd-ca                 no      
front-proxy-client         Jul 17, 2022 01:01 UTC   364d            front-proxy-ca          no      
scheduler.conf             Jul 17, 2022 01:01 UTC   364d                                    no      

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Jul 06, 2030 03:24 UTC   8y              no      
etcd-ca                 Jul 06, 2030 03:24 UTC   8y              no      
front-proxy-ca          Jul 06, 2030 03:24 UTC   8y              no   
```

3. 更新用户配置

```
cd /etc/kubernetes

kubeadm alpha kubeconfig user --client-name=admin
kubeadm alpha kubeconfig user --org system:masters --client-name kubernetes-admin  > /etc/kubernetes/admin.conf
kubeadm alpha kubeconfig user --client-name system:kube-controller-manager > /etc/kubernetes/controller-manager.conf
kubeadm alpha kubeconfig user --org system:nodes --client-name system:node:$(hostname) > /etc/kubernetes/kubelet.conf
kubeadm alpha kubeconfig user --client-name system:kube-scheduler > /etc/kubernetes/scheduler.conf
```

4. master 节点 config

```
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
```

5. 登录 `worker` 节点

> 将master节点上的 `$HOME/.kube/config` 文件拷贝到 `worker` 节点对应的文件中

```
scp k8s-m1:~/.kube/config $HOME/.kube
chown $(id -u):$(id -g) $HOME/.kube/config
```

6. 重启 主从节点 `reboot`



## 重新配置 LENS 

1. 检查配置文件中的公网地址

```
cd ~
cat ./kubeadm-config.yaml
```

```
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
kubernetesVersion: v1.18.3
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers

#master地址
controlPlaneEndpoint: "********:6443"
networking:
  serviceSubnet: "10.96.0.0/16"

  #k8s容器组所在的网段
  podSubnet: "10.20.0.1/16"
  dnsDomain: "cluster.local"

# 为了让证书包含公网IP，从而允许从外网访问集群
apiServer:
  certSANs:       #填写所有kube-apiserver节点的hostname、IP、VIP
  - k8s-m1        #请替换为hostname
  - ********   #请替换为公网
  - ********   #请替换为私网
  - 10.96.0.1     #不要替换，此IP是API的集群地址，部分服务会用到
```

2. 检查

```
cd ~
cat ~/.kube/config
```

```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS......LQo=
    server: https://***************:6443
  name: kubernetes
  
contexts:
- context:
    cluster: kubernetes
    user: kubernetes-admin
  name: kubernetes-admin@kubernetes
current-context: kubernetes-admin@kubernetes

kind: Config
preferences: {}
users:
- name: kubernetes-admin
  user:
    client-certificate-data: LS...........LQo=
    client-key-data: LS.........LQo=
```

3. 复制上面的 config 内容

4. 并修改其中的 ***********:6443 ， 修改为公网地址

5. 修改 context 的 name，和 current-context（否则，LENS无法添加）

> 比如，改为：kubernetes-admin@kubernetesCMCC

6. 进入 LENS ，Add Cluster，paste config
