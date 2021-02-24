---
id: 20210224002_create_react_app_config
title: create-react-app 脚手架的简单配置
subtitle: create-react-app 构建的单页应用在开发环境下的简单配置
subject: 开发环境
category: 指导手册
tags: create-react-app
keywords: port
level: 200
cover: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K
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
