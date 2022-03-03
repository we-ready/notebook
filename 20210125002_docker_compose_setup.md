---
id: 20210125002_docker_compose_setup
title: Docker Compose 的安装设置
subtitle: CentOS 下 Docker 和 Docker Compose 的安装配置
subject: 开发环境
category: 指导手册
tags: Docker Compose
keywords: Docker;淘宝镜像;基本命令
level: 100
cover: https://media.inkscape.org/media/resources/file/Koi_carp_2.svg
videos: 
authors: Chris Wei
created_when: 2021-01-25
updated_when: 2021-01-25
---

# Docker Compose 的安装设置

## 参考文章

- [Get Docker Engine - Community for CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
- [docker 及 docker-compose 的快速安装和简单使用](https://www.cnblogs.com/morang/p/9501223.html)

## Install Docker

1. SET UP THE REPOSITORY

```
# sudo yum install -y yum-utils device-mapper-persistent-data lvm2
# sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

2. INSTALL DOCKER ENGINE - COMMUNITY

```
# sudo yum install docker-ce docker-ce-cli containerd.io
```

3. Start Docker

```
$ sudo systemctl start docker
```

4. Verify that Docker Engine - Community is installed correctly by running the hello-world image.

```
$ sudo docker run hello-world
```

5. Verify that Docker Engine - Community is installed correctly by running the whalesay image. (Optional)

> [docker/whalesa](https://hub.docker.com/r/docker/whalesay)

```
$ docker run docker/whalesay cowsay boo
```

## 使用中国区官方镜像

1. create json file

```
# vi /etc/docker/daemon.json
# cat /etc/docker/daemon.json
```

> daemon.json

```
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
```

2. restart docker

```
# systemctl daemon-reload
# systemctl restart docker
# systemctl restart docker.service
```

3. reboot server

```
# reboot
```

## Docker Compose

1. Download Docker Compose (with Daocloud Mirror)

```
# curl -L https://get.daocloud.io/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
```

2. Apply executable permissions to the binary:

```
# chmod +x /usr/local/bin/docker-compose
```

3. Verify that Docker Compose

```
# docker-compose --version
```

## 基本命令

### run - Run a container

- tag

```
# docker run redis:4.0
```

- STDIN
- -it (interactive mode, attach terminal)
- attach / detach (-d)
- Port Mapping (external:internal)

```
# docker run -p 8001:3000 xxxxx
# docker run -p 8002:3000 xxxxx
# docker run -p 8003:3000 xxxxx
# docker run -p 8004:3000 xxxxx
```

- Volume Mapping

```
# docker run --name db_pg_1 -v /my/own/datadir:/var/lib/postgresql/data -d postgres
```

- Environment Variables

```
# docker run -e APP_COLOR=blue XXXX
```

### ps - List containers

### stop - Stop a container

### rm - Remove a container

### rmi - Remove images

### pull - Download an image

### exec - Execute a command

### attach - attach a container

### inspect - inspect a container

### logs - show container's log

### 示例

```
# docker run centos
# docker run -it centos bash
# docker ps
# docker ps -a
# docker run centos sleep 20
# docker run -d --name thistest centos sleep 100
# docker exec thistest cat /etc/*release*
# docker stop thistest
# docker rm xxx xxx xxx
# docker images
# docker rmi xxxx
# docker pull centos
# docker inspect thistest
# docker logs thistest
```

## 典型镜像

### 使用 Node:alpine 启动 js 脚本

```
# docker run -it --rm --name node_main_1 -v "$PWD":/usr/src/app -w /usr/src/app node:11.10.1-alpine node index.js
```

### 使用 postgres:alpine 管理数据库

1. 下载镜像

```
# docker pull postgres:alpine
```

2. 启动容器

```
# docker run --name dbpg -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres:alpine
```

3. 进入容器

```
# docker exec -it dbpg /bin/bash
```

4. 启动 psql 

```
psql -U postgres -d postgres
```

## 参考

- [Docker for the Absolute Beginner - Hands On](https://kodekloud.com/courses/296044)
- [Docker Documents](https://docs.docker.com/)
- [docker实现postgresql](https://www.jianshu.com/p/9ab7b89637e7)
- [Docker网络和容器的通信](https://www.cnblogs.com/whych/p/9595671.html)
- [docker中容器之间通信方式](https://blog.csdn.net/u013355826/article/details/84987233)
- [使用docker-compose 大杀器来部署服务](https://www.cnblogs.com/neptunemoon/p/6512121.html#toc_30)

## 集成环境

### 下载 Node 镜像

```
# docker pull node:12.14.0-alpine
```

### 安装 Nodejs

1. download and install npm binary pakage

```
[root@ ~]# wget https://nodejs.org/dist/v12.14.0/node-v12.14.0-linux-x64.tar.xz
[root@ ~]# tar -xvf node-v12.14.0-linux-x64.tar.xz
[root@ ~]# ln -s ~/node-v12.14.0-linux-x64/bin/node /usr/bin/node
[root@ ~]# ln -s ~/node-v12.14.0-linux-x64/bin/npm /usr/bin/npm
[root@ ~]# npm -v
[root@ ~]# node -v
```

可以使用国内镜像

```
[root@ ~]# wget https://npm.taobao.org/mirrors/node/v12.14.0/node-v12.14.0-linux-x64.tar.gz

[root@ ~]# tar -xvf node-v12.14.0-linux-x64.tar.gz
[root@ ~]# ln -s ~/node-v12.14.0-linux-x64/bin/node /usr/bin/node
[root@ ~]# ln -s ~/node-v12.14.0-linux-x64/bin/npm /usr/bin/npm
[root@ ~]# npm -v
[root@ ~]# node -v

```

> install wget in case it is not installed

```
[root@ ~]# yum -y install wget
```

2. edit profile

```
[root@ ~]# vim /etc/profile
[root@ ~]# cat /etc/profile
```

> profile file content

```
export NODE_PATH="/root/node-v12.14.0-linux-x64"
export PATH=$NODE_PATH/bin:$PATH
```

3. restart the server from console

```
[root@ ~]# reboot
```

4. install global npm packages

```
[root@ ~]# npm install -g yarn
```

```
[root@ ~]# npm install -g gulp
[root@ ~]# npm install -g cross-env
[root@ ~]# npm install -g rimraf
```

可以使用淘宝镜像

```
npm install xxxx -g --registry=http://registry.npm.taobao.org
```


## 替代安装方案（未验证）

> https://www.youtube.com/watch?v=-gF-Jsk85bQ
> https://github.com/devopsjourney1/influxdb-2-dockercompose

```
apt-get update -y
apt install docker.io -y && apt install docker-compose -y
```
