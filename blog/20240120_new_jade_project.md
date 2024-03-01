---
id: 20240120_new_jade_project
title: 创建 JADE 项目的Check List
subtitle: 项目部署手册
subject: DevOps
category: 操作手册
tags: 
keywords: docker-compose;deploy
level: 200
cover: http://qiniuargus.weready.online/blog/desktop.jpg
authors: Chris Wei
created_when: 2024-01-20
updated_when: 2024-01-20
---

# JADE 项目部署

## 阿里云准备 ECS 服务器

1. 安装操作系统
2. 安装 docker-compose
3. 安装 git
4. 安装 node + npm
5. 安装 yarn
6. 下载 docker 镜像
7. 下载 frp
8. 准备后期运维的 sh 脚本
9. 配置安全组，打开 80 端口，7000 端口 ( frp )

## 准备好域名, 并指向 ECS 服务器

> 后续内容中的 `[domain]` 指的就是这里准备好的域名

## OSS

1. 阿里云创建 `OSS Bucket`
2. 设置 Bucket 的跨域访问
3. 创建必要的 RAM 账号

## 短信

1. 短信管理后台备案签名和模板

## 项目控制及容器环境变量

1. `tools/ops` 目录下新建 一个 `docker-compose.XXXXXX.yml` 文件
2. `package.json` 中的 `start` / `stop` 脚本指向这个新的 `yml` 文件
3. 设置 `backend/services/restapi/.env`
4. 设置 `frontend/app/admin/.env`
5. 设置 `frontend/app/jade-buyer/.env`

## 微信相关配置的准备工作

1. 确认 服务号 和 商户 已经建立关联
  > 服务号 ==>> 接口权限 ==>> 功能服务 ==>> 微信支付 ==>> 微信支付接口权限已获得

2. 打开 frp
  > 确保 IP 地址 和 域名 已经正确配置正确

3. 确保 `[domain]` 能访问到本地服务，获得响应

## 微信服务号

#### 设置与开发 ==>> 公众号设置 ==>> 功能设置 ==>> JS 接口安全域名

1. 下载 `MP_verify_XXXXXX.txt`
2. 保存到 `backend\services\restapi\runtime\wechat`
3. 设置安全域名：`[domain]`（根目录，不设置子目录）

#### 设置与开发 ==>> 公众号设置 ==>> 功能设置 ==>> 网页授权域名

1. 设置网页授权域名：`[domain]`（根目录，不设置子目录）

#### 设置与开发 ==>> 基本配置

1. 记录：AppID
2. 开启并记录：开发者密码（AppSecret）
3. 刷新页面，会看到 IP 白名单设置选项，配置 IP 白名单

#### 设置与开发 ==>> 基本配置 ==>> 服务器配置

1. URL：能够响应 token 验证请求的地址，包括相关的 `wechat.token.controller` 的路由
2. Token：填入通用 token
3. EncodingAESKey：填入 通用 AES Key
4. 明文模式

## 微信商户

#### 产品中心

1. 确保开通了 JSAPI 支付（微信内打开网页，支付时微信内跳转直接支付） 和 Native 支付（网站显示二维码，用户扫码支付）

#### 产品中心 ==>> 开发配置

1. 记录商户号
2. 设置 JSAPI 支付授权目录（根域名：[domain]）
3. 设置 Native 支付回调链接（精确的，有 controller 响应的 域名 + 路由）

#### 产品中心 ==>> AppID账号管理

1. 在商户号里面填写服务号的 AppID，申请关联
2. 回到服务号的 接口授权 ==>> 功能服务 ==>> 微信支付 里面确认

#### 账户中心 ==>> API安全

1. 设置 API 密钥（partnerKey）（通用）
2. 申请证书
3. 保存到 `backend\services\restapi\runtime\wepay`

## 项目控制及容器环境变量

1. 确认下面内容的一致性
  > `backend/services/restapi/.env`
  > `tools/ops/docker-xxxxx.yml`

## !!!修改 ITAdmin 密码!!!