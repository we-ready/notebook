---
id: 20210125003_k8s_cluster_setup
title: Kubernetes (k8s) 集群安装部署
subtitle: 在 CentOS 服务器环境下，K8S 一主一从的集群安装
subject: 云原生
category: 指导手册
tags: kubernetes;k8s;Ingress;calico;LENS
keywords: kubeadm;k8s集群
level: 200
cover: http://qiniuargus.weready.online/blog/tech_logos.png
author: Chris Wei
created_when: 2021-01-25
updated_when: 2021-01-25
---

# Kubernetes (k8s) 集群安装部署

## 环境概述

- 阿里云 (athena) ECS (2C 8G) x2
- CentOS 7.8
- kubernetes 1.18
- [Master Public IP] ([Master Private IP]): k8s-m1 (master)
- [Worker Public IP] ([Worker Private IP]): k8s-w1 (worker)

## 准备工作

#### 检查操作系统版本

```
# cat /etc/redhat-release
CentOS Linux release 7.8.2003 (Core)
```

#### 检查并修改机器名称

```
# hostname
# hostnamectl
# cat /etc/hostname
```

```
# vi /etc/hostname
```

```
k8s-m1
```

```
# systemctl restart systemd-hostnamed
```

```
# reboot
```

#### 配置集群 hosts (私有地址)

```
# vi /etc/hosts
```

```
[Master Private IP] k8s-m1
[Worker Private IP] k8s-w1
```

#### 禁用`防火墙`

```
# systemctl stop firewalld && systemctl disable firewalld
# systemctl stop firewalld
```

#### 禁用`selinux`

```
# setenforce 0
# sed -i '7s/enforcing/disabled/' /etc/selinux/config
```

```
# reboot
```

#### 创建配置文件（`/etc/sysctl.d/k8s.conf`）

> 创建文件并添加内容

```
# cat >/etc/sysctl.d/k8s.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```

> 执行命令使之生效

```
# modprobe br_netfilter && sysctl -p /etc/sysctl.d/k8s.conf
```

#### 安装ipvs

> 创建文件并添加内容（保证在节点重启后能自动加载所需模块）

```
# cat > /etc/sysconfig/modules/ipvs.modules <<EOF
#!/bin/bash
modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack_ipv4
EOF
```

> 修改权限以及查看是否已经正确加载所需的内核模块

```
# chmod 755 /etc/sysconfig/modules/ipvs.modules && bash /etc/sysconfig/modules/ipvs.modules
```

> 查看是否已经正确加载所需的内核模块

```
# lsmod | grep -e ip_vs -e nf_conntrack_ipv4
nf_conntrack_ipv4      15053  0 
nf_defrag_ipv4         12729  1 nf_conntrack_ipv4
ip_vs_sh               12688  0 
ip_vs_wrr              12697  0 
ip_vs_rr               12600  0 
ip_vs                 145497  6 ip_vs_rr,ip_vs_sh,ip_vs_wrr
nf_conntrack          139264  2 ip_vs,nf_conntrack_ipv4
libcrc32c              12644  2 ip_vs,nf_conntrack
```

> 安装 `ipset` 和 `ipvsadm` (便于查看 ipvs 的代理规则)

```
# yum -y install ipset ipvsadm
```

#### 同步服务器时间

> 安装chrony

```
# yum -y install chrony
```

> 修改同步服务器地址为阿里云

```
# sed -i.bak '3,6d' /etc/chrony.conf && sed -i '3cserver ntp1.aliyun.com iburst' /etc/chrony.conf
```

> 启动`chronyd`及加入开机自启

```
# systemctl start chronyd && systemctl enable chronyd
```

> 查看同步结果

```
# chronyc sources
```

#### 关闭`swap`分区

> 手动关闭swap

```
# swapoff -a
```

> 修改fstab文件，注释swap自动挂载 (!!!!!! 此处有些问题：貌似原文件中并没有这句话，因此这个命令实际并未发生作用 !!!!!!)

```
# sed -i '/^\/dev\/mapper\/centos-swap/c#/dev/mapper/centos-swap swap                    swap    defaults        0 0' /etc/fstab
```

> 查看swap是否关闭

```
# free -m
              total        used        free      shared  buff/cache   available
Mem:           7821         123        7395           0         301        7472
Swap:             0           0           0
```

> `swappiness` 参数调整，修改`/etc/sysctl.d/k8s.conf`添加下面一行

```
# cat >>/etc/sysctl.d/k8s.conf <<EOF
vm.swappiness=0
EOF
```

> 使配置生效

```
# sysctl -p /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
vm.swappiness = 0
```

## 安装

#### 安装 Docker18.09.9

> 安装 `yum-utils` 命令包，从而可以使用 `yum-config-manager` 命令

```
yum -y install yum-utils
```

> 添加阿里云yum源

```
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

> 查看可用版本

```
yum list docker-ce --showduplicates | sort -r
已加载插件：fastestmirror, langpacks
可安装的软件包
 * updates: mirrors.aliyun.com
Loading mirror speeds from cached hostfile
 * extras: mirrors.aliyun.com
docker-ce.x86_64            3:19.03.5-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.4-3.el7                     docker-ce-stable
。。。。。。
docker-ce.x86_64            3:18.09.9-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.8-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.7-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.6-3.el7                     docker-ce-stable
。。。。。。
```

> 安装docker18.09.9

```
yum -y install docker-ce-18.09.9-3.el7 docker-ce-cli-18.09.9
```

> 启动docker并设置开机自启

```
systemctl enable docker && systemctl start docker
```

> 配置阿里云docker镜像加速

```
cat > /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://gqk8w9va.mirror.aliyuncs.com"]
}
EOF
```

> 配置完后重启docker

```
systemctl restart docker
```

> 查看加速

```
docker info
```

找到Registry Mirrors一行
Registry Mirrors:
 https://gqk8w9va.mirror.aliyuncs.com/
  
> 查看docker版本

```
docker version

Client:
 Version:           18.09.9
 API version:       1.39
 Go version:        go1.11.13
 Git commit:        039a7df9ba
 Built:             Wed Sep  4 16:51:21 2019
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.9
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.11.13
  Git commit:       039a7df
  Built:            Wed Sep  4 16:22:32 2019
  OS/Arch:          linux/amd64
  Experimental:     false
```

#### 修改`docker Cgroup Driver`为`systemd`

> 将/usr/lib/systemd/system/docker.service文件中的这一行 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
> 修改为 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --exec-opt native.cgroupdriver=systemd
> 如果不修改，在添加 worker 节点时可能会碰到如下错误
> [WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". 
Please follow the guide at https://kubernetes.io/docs/setup/cri/

> 使用如下命令修改

```
sed -i.bak "s#^ExecStart=/usr/bin/dockerd.*#ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --exec-opt native.cgroupdriver=systemd#g" /usr/lib/systemd/system/docker.service
```

> 重启docker

```
systemctl daemon-reload && systemctl restart docker
```

#### 安装`Kubeadm`

> 使用阿里云`yum`源

```
cat >/etc/yum.repos.d/kubernetes.repo <<EOF
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
        http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```

> 安装 `kubeadm`、`kubelet`、`kubectl` (阿里云yum源会随官方更新最新版，因此指定版本)

> 安装1.18.4版本

```
yum -y install kubelet-1.18.4 kubeadm-1.18.4 kubectl-1.18.4
```

> 查看版本

```
kubeadm version

kubeadm version: &version.Info{Major:"1", Minor:"16", GitVersion:"v1.18.4", GitCommit:"a17149e1a189050796ced469dbd78d380f2ed5ef", GitTreeState:"clean", BuildDate:"2020-04-16T11:42:30Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
```

> 设置`kubelet`开机自启

```
systemctl enable kubelet
```

> 设置`k8s`命令自动补全

```
yum -y install bash-completion
source /usr/share/bash-completion/bash_completion
source <(kubectl completion bash)
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

# 初始化集群

## 初始化 `master` 节点

#### 配置 `kubeadm` 初始化文件

```
cat <<EOF > ./kubeadm-config.yaml
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
kubernetesVersion: v1.18.3
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers

#master地址
controlPlaneEndpoint: "[Mater Private IP]:6443"	
networking:
  serviceSubnet: "10.96.0.0/16"	

  #k8s容器组所在的网段
  podSubnet: "10.20.0.1/16"	
  dnsDomain: "cluster.local"

# 为了让证书包含公网IP，从而允许从外网访问集群
apiServer:
  certSANs:       #填写所有kube-apiserver节点的hostname、IP、VIP
  - k8s-m1        #请替换为hostname
  - [Master Public IP]  #请替换为公网
  - [Mater Private IP]  #请替换为私网
  - 10.96.0.1     #不要替换，此IP是API的集群地址，部分服务会用到

EOF
```

#### 初始化 `master`

> ⚠️如果想要重新初始化，需要执行命令 `kubeadm reset -f`

> `kubeadm init --config=kubeadm-config.yaml --upload-certs`

```
# kubeadm init --config=kubeadm-config.yaml

....

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of control-plane nodes by copying certificate authorities
and service account keys on each node and then running the following as root:

  kubeadm join [Mater Private IP]:6443 --token xxxxxx.xxxxxxxxxxxxxxxxx \
    --discovery-token-ca-cert-hash sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
    --control-plane 

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join [Mater Private IP]:6443 --token xxxxxx.xxxxxxxxxxxxxxxxx \
    --discovery-token-ca-cert-hash sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

```

> ⚠️ 保存 token sha256

> 拷贝 `kubeconfig` 文件（这里的路径为 `/root`）

```
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
```

## 初始化 `worker` 节点

> 将master节点上的 `$HOME/.kube/config` 文件拷贝到 `worker` 节点对应的文件中

```
mkdir -p $HOME/.kube 
scp k8s-m1:~/.kube/config $HOME/.kube
chown $(id -u):$(id -g) $HOME/.kube/config
```

> 将 `worker` 节点加入到集群中

> 这里需要用到2.2中初始化master最后生成的token和sha256值

```
kubeadm join [Mater Private IP]:6443 --token xxxxxx.xxxxxxxxxxxxxxxxx \
    --discovery-token-ca-cert-hash sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

... ...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

> 如果忘记了token和sha256值，可以在master节点使用如下命令查看

```
#kubeadm token list
TOKEN                     TTL       EXPIRES                     USAGES                   DESCRIPTION   EXTRA GROUPS
px979r.mphk9ee5ya8fgy44   20h       2020-03-18T13:49:48+08:00   authentication,signing   <none>        system:bootstrappers:kubeadm:default-node-token
```         
            
> 查看sha256

```
#openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> 同时查看token和sha256

```
#kubeadm token create --print-join-command
kubeadm join 192.168.9.10:6443 --token 9b28zg.oyt0kvvpmtrem4bg     --discovery-token-ca-cert-hash sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> master节点查看node（发现状态都是NotReady，因为还没有安装网络插件，这里我们安装calio官方插件文档）

```
kubectl get nodes
```

## `Master` 节点安装网络插件calio

> 下载文件

```
wget https://docs.projectcalico.org/v3.8/manifests/calico.yaml
```

> 因为在上边kubeadm-config.yaml配置文件中指定了容器组IP，所以需要将文件中的`625`行改为如下：

```
value: "10.20.0.1/16"
```

> vi 命令

```
:set number
```

> 修改完成后安装calico网络插件

```
kubectl apply -f calico.yaml
```

> 安装完成后稍等一会查看pods状态

```
kubectl get pods -n kube-system
```

> 查看node状态

```
kubectl get nodes 
```

## 启动 `LENS` 

#### 阿里云开通 `6443` 端口

#### Lens 添加集群

```
cat ~/.kube/config
```

> IP 修改为公网IP

#### 启用集群的 `Metrics` Feature

# 准备镜像

#### 镜像列表

- registry.cn-beijing.aliyuncs.com/[???]/worker:0.2.0-[???]
- registry.cn-beijing.aliyuncs.com/[???]/service:0.2.0-[???]
- registry.cn-beijing.aliyuncs.com/[???]/frontend:0.2.0-[???]
- rabbitmq:3.8.2-alpine
- postgres:12.1-alpine
- node:12.14.1-alpine
- redis:5.0.7-alpine
- nginx:1.17.6-alpine
- busybox

#### 命令 - 登录阿里云镜像服务

```
docker login -u [user name] -p [password] registry.cn-hangzhou.aliyuncs.com
```

> 可以参考阿里云镜像服务的命令行提示

#### 命令 - 获取镜像

```
docker pull
```

# 安装 Git

```
yum install git
```

# 获取 Demo 脚本

> git repo of dockerimages

```
#!/bin/bash
git clone --depth=1 https://[user name]:[password]@github.com/YunzhiWei/dockerimages.git
```

# 启动 Ingress 

## Ingress Controller of Traefik

> 切换到 `architecture/traefik` 目录

#### Apply rbac role and role binding

```
# kubectl apply -f traefik-rbac.yaml
# kubectl describe clusterrole traefik-ingress-controller -n kube-system
```

#### Apply daemonset

```
kubectl apply -f traefik-ds-http.yaml
kubectl get all -n kube-system | grep traefik
```



# 服务器重启后，k8s 重启失败

## 参考

https://www.hangge.com/blog/cache/detail_2419.html
原文出自：www.hangge.com  转载请保留原文链接：https://www.hangge.com/blog/cache/detail_2419.html

## 背景及现象

在安装配置好 Kubernetes 后，正常情况下服务器关机重启，kubelet 也会自动启动的。
但最近配置的一台服务器重启后，输入命令 `kubectl get nodes` 查看节点报如下错误：
`The connection to the server xxx.xxx.xxx.xxx:6443 was refused - did you specify the right host or port?`

## 检查

输入 `systemctl status kubelet` 命令查看 `kubelet` 的情况

> 发现 kubelet 确实没有启动

```
... ...
code=exited, status=255
... ...
```

## 原因

由于 K8s 必须保持全程关闭交换内存，之前我安装是只是使用 swapoff -a 命令暂时关闭 swap。而机器重启后，swap 还是会自动启用，从而导致 kubelet 无法启动。

## 解决办法

#### 首先，执行如下命令关闭 swap

```
swapoff -a
```

#### 然后，编辑 /etc/fstab 文件

```
vi /etc/fstab
```

将 `/dev/mapper/centos-swap swap swap default 0 0` 这一行前面加个 `#` 号将其注释掉。

## 重启服务器



# 执行 kubectl 命令报错：证书过期

## 错误提示

> `Unable to connect to the server: x509: certificate has expired or is not yet valid`

## 参考

#### [k8s master 出现问题证书过期问题](https://q.cnblogs.com/q/133037/)

```
经过实际验证，解决方法非常简单，只需运行2个命令：

1）更新所有证书

kubeadm alpha certs renew all

2）更新当前用户的 .kube/config

cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
注：如果少了第2步，运行 kubectl 命令时会报错

error: You must be logged in to the server (Unauthorized)
```

#### [kubernets 证书过期的问题](https://www.cnblogs.com/kuku0223/p/11867391.html)

> 原理及预防（似乎版本过老，稳重用的命令`kubeadm alpha phase certs`，已经改成了`kubeadm alpha certs`）

```
kubeadm 是 kubernetes 提供的一个初始化集群的工具，使用起来非常方便。但是它创建的apiserver、controller-manager等证书默认只有一年的有效期，同时kubelet 证书也只有一年有效期，一年之后 kubernetes 将停止服务。
官方推荐一年之内至少用 kubeadm upgrade 更新一次 kubernetes 系统，更新时也会自动更新证书。不过，在产线环境或者无法连接外网的环境频繁更新 kubernetes 不太现实。
我们可以在过期之前或之后，使用kubeadm alpha phase里的certs和kubeconfig命令，同时配合kubelet证书自动轮换机制来解决这个问题。
```

> 操作注意事项

```
一旦证书过期，使用kubectl时会出现如下提示：
Unable to connect to the server: x509: certificate has expired or is not yet valid
在此，我们使用 kubeadm alpha phase certs 系统命令，重新生成证书。
建议不要重新生成ca证书，因为更新了ca证书，集群节点就需要手工操作，才能让集群正常(会涉及重新join)。

操作之前，先将/etc/kubernetes/pki下的证书文件，mv到其它文件夹，作个临时备份，不要删除。

kubeadm alpha phase certs etcd-healthcheck-client --config cluster.yaml
kubeadm alpha phase certs etcd-peer --config cluster.yaml
kubeadm alpha phase certs etcd-server --config cluster.yaml
kubeadm alpha phase certs front-proxy-client--config cluster.yaml
kubeadm alpha phase certs apiserver-etcd-client --config cluster.yaml
kubeadm alpha phase certs apiserver-kubelet-client --config cluster.yaml
kubeadm alpha phase certs apiserver --config cluster.yaml
kubeadm alpha phase certs sa --config cluster.yaml


在生成这些新的证书文件之后，再需要kubeadm alpha phase config命令，重新生成新的kubeconfig文件。
操作之前，先将/etc/kubernetes/下的kubeconfig，mv到其它文件夹，作个临时备份，不要删除。
kubeadm alpha phase kubeconfig all --config cluster.yaml

由于service account的密钥是以rsa密钥对形式生成，所以没有过期时间。
如无必要，千万不要生成重新生成sa密钥。因为sa密钥关联到一切系统pod内的进程访问api server时的认证。
如果更新了sa，则需要先重新生成这些pod加截的token，再删除这些pod之后，重新加载token文件。

```

#### [kubeadm安装的k8s集群证书过期处理](http://t.zoukankan.com/qinghe123-p-12582393.html)

#### [Unable to connect to the server: x509: certificate has expired or is not yet valid](https://blog.csdn.net/swan_tang/article/details/115755311)

```
1.  登录master服务器，进入 `/etc/kubernetes/` 查看证书，确认证书有效期：openssl x509 -in apiserver.crt -noout -text |grep ' Not '
2.  备份 `/etc/kubernetes/pki` 目录下的所有文件
3.* 手动更新证书 `kubeadm alpha certs renew all`
4.  查看证书有效期是否更新
5.  在master节点上将/etc/kubernetes目录下的所有配置文件备份
6.  更新用户配置：执行下面多个命令

kubeadm alpha kubeconfig user --client-name=admin
kubeadm alpha kubeconfig user --org system:masters --client-name kubernetes-admin  > /etc/kubernetes/admin.conf
kubeadm alpha kubeconfig user --client-name system:kube-controller-manager > /etc/kubernetes/controller-manager.conf
kubeadm alpha kubeconfig user --org system:nodes --client-name system:node:$(hostname) > /etc/kubernetes/kubelet.conf
kubeadm alpha kubeconfig user --client-name system:kube-scheduler > /etc/kubernetes/scheduler.conf

7.* 用更新后的admin.conf替换/root/.kube/config文件
8.  更新后，把master 节点服务器的 home目录下的 .kube 文件夹 复制到本机的/home/用户目录下
9.  重启所有master节点上的apiserver和scheduler两个系统组件
10. 本机执行kubectl 命令

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
cp -r /etc/kubernetes ./backup/etc_k8s
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
docker exec -it d7a /bin/bash
```

8. 备份数据库

```
cd script
pg_dump -h dbpg -U postgres archellis > 20210717.yunzhi.bak
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
scp 20210717.yunzhi.bak 172.17.64.152:~/projects/dbdump/
```

## 问题解决的实际操作

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

6. 重启 master 节点服务（命令执行失败）

```
systemctl restart kube-apiserver
systemctl restart kube-scheduler
```

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
