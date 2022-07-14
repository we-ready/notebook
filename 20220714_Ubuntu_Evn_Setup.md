---
id: 20220714_ubuntu_env_setup
title: Ubuntu 全栈环境配置步骤
subtitle: 如何在 Ubuntu 系统上配置 Docker Compose + NodeJS + Git + Electron
subject: 运维
category: 指导手册
tags: ubuntu;docker;docker compose;nodejs;git;electron
keywords: 环境配置;系统安装
level: 200
cover: https://media.inkscape.org/media/resources/file/Koi_carp_2.svg
authors: Chris Wei
created_when: 2022-07-14
updated_when: 2022-07-14
---

# 准备工作

1. 确保板子为出厂状态，必要的时候做固件升级
2. 确保板子可以连接网络，有线网络或者 WiFi

3. 升级系统基础软件

```
$ sudo apt update
$ sudo apt-get update
$ sudo apt upgrade
```


# 安装 docker

## 安装

```
$ sudo apt install docker
$ sudo apt install docker.io
```

## 启动

```
$ sudo systemctl start docker
```

## 设置开机启动

```
$ sudo systemctl enable docker
```

## 检查

```
$ sudo systemctl status docker
$ sudo docker version
$ sudo docker images
$ sudo docker ps
```

# 安装 docker Compose

```
$ sudo curl -L "https://get.daocloud.io/docker/compose/releases/download/v2.1.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose --version
```

# 获取 docker 镜像

```
sudo docker pull node:16.14.0-alpine
sudo docker pull redis:5.0.7-alpine
sudo docker pull rabbitmq:3.8.2-alpine
sudo docker pull postgres:12.1-alpine
sudo docker pull nginx:1.17.6-alpine

sudo docker images
```

# 安装 git

```
$ sudo apt install git
$ git --version
```


# 安装 nodejs

```
$ curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```
or
```
$ curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```

```
$ sudo apt-get install -y nodejs

$ node -v
v16.15.1

$ npm -v
8.11.0
```

# 安装全局 npm 包

```
$ sudo npm install --location=global yarn
```


# 创建项目目录

1. 桌面 Home 目录下创建 projects

# 可选验证 ******

## 获取源码

1. projects 目录下创建 `atlas.clone.sh`
1. 启动 Terminal Shell
1. 进入 Home/projects
1. 执行 

```
$ sh atlas.clone.sh
$ mv atlas.new atlas
```

## 构建项目

```
$ cd atlas
$ sudo yarn build
```

> 如果 `websocket` 构建失败，必要时修改 `websocket` 源码和 `package.json`，去掉 `instrument` 和 `nodemon`

## 启动项目

```
sudo docker images
sudo yarn start
sudo docker ps
```

> 第一次启动因为需要下载 `influxdb` 和 `search` 镜像，会很慢

## 停止项目

```
sudo yarn stop
```

# 桌面应用

1. 进入 `desktop/manager` 目录
1. 删掉 `package.lock`
1. 编辑 `package.json`
1. 删除 `electron`
1. 安装其他依赖包 `yarn`
1. 安装依赖包 `yarn add -D electron`
1. 运行 `yarn start`
1. 改造构建参数 `--platform=linux --arch=arm64`
1. 构建桌面应用 `yarn build:<???>`
1. 运行

```
$ cd ./dist/Manager-linux-arm64
$ ./Manager
```
