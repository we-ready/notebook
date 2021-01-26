---
id: 20210125001_win_dev_env_setup
title: Windows开发环境的安装设置
subtitle: Windows系统下，基于Nodejs做全栈开发的系统设置
subject: 开发环境
category: 指导手册
tags: 
keywords: Windows;Development Environment
cover: http://qiniuargus.weready.online/blog/Coder_desk.png
author: Chis Wei
created_when: 2021-01-25
updated_when: 2021-01-25
---

# Windows开发环境的安装设置

## Chrome

1. [Download Here](https://www.google.com/chrome/)
1. 登录并同步信息
1. 设置启动页

## Firefox

- [Download Here](http://www.firefox.com.cn/)

## 1Passport

1. [Download Here](https://1password.com/)
1. 同步信息

## VPN

1. 复制可执行文件
1. 配置服务器设置

## Xshell

1. [Download Here](https://www.netsarang.com/en/xshell/)
1. 新建`会话`，连接到服务器
1. 添加到`会话地址栏`

## Git

1. [Download Here](https://git-scm.com/downloads)
1. [Check GUI clients here](https://git-scm.com/downloads/guis)

## Github Tools

- [Github Desktop](https://desktop.github.com/)

## SourceTree

- [Download Here](https://www.sourcetreeapp.com/)

## VSCode

- [Download Here](https://code.visualstudio.com/)
- 安装扩展
  + Chinese (Simplified) Language Pack for Visual Studio Code
  + Markdown Preview Enhanced
  + Quokka.js
  + Emoji Snippets
  + VSCode NestJs Snippets
  + ES7 React/Redux/GraphQL/React-Native snippets
  + vscode-styled-components

## Postman

1. [Download Here](https://www.postman.com/downloads/)
1. 登录账号
1. 同步数据

## Nodejs

1. [Download Here](https://nodejs.org/en/download/)
1. 全局安装

```
npm install -g yarn
npm install -g mocha
npm install -g istanbul
```

## postgresql

1. [Download Here](https://www.postgresql.org/download/)
1. [Windows Version](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
  
  > Stack Builder may fail. It doesn't matter.

3. 增加环境变量：C:\Program Files\PostgreSQL\xx.x\bin
1. 重启 Windows
1. SQL Shell (psql)

```
c:\xxx > psql
postgres=# DROP DATABASE [database name];
postgres=# DROP USER [user name];
postgres=# CREATE USER [user name] WITH PASSWORD '[password]';
postgres=# CREATE DATABASE [database name] OWNER [user name];
postgres=# GRANT ALL PRIVILEGES ON DATABASE [database name] TO [user name];
```

6. 安装扩展

```
c:\xxx > psql -U [database name] -d [user name]
[database name]=> \c [database name] postgres;
[database name]=# create extension ltree;
[database name]=# create extension "pgcrypto";
[database name]=# create extension tablefunc;
[database name]=# \c [database name] [user name];
```

## LENS

- [Download Here](https://github.com/lensapp/lens/releases/download/v3.5.0/Lens-Setup-3.5.0.exe)

## VMWare Workstation

1. Download
1. Install
1. 创建虚机
1. 启动虚机
1. 安全容器或集群环境，参考：xxxx

## 其他

- 钉钉
- 腾讯会议
