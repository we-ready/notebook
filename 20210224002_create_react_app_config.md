---
id: 20210224002_create_react_app_config
title: create-react-app 脚手架的简单配置
subtitle: create-react-app 构建的单页应用在开发环境下的简单配置
subject: 开发环境
category: 指导手册
tags: create-react-app
keywords: port
level: 200
cover: https://media.inkscape.org/media/resources/file/Snoopy_at_the_Bar.png
author: Chris Wei
created_when: 2021-02-24
updated_when: 2021-02-24
---

# create-react-app 脚手架的简单配置

## 开发调试时使用不同的本地端口

> 修改 `package.json` 的启动脚本

```
  "scripts": {
    "start": "set PORT=9000 && react-scripts start",
```
