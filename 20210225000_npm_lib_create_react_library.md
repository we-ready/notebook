---
id: 20210225000_npm_lib_create_react_library
title: 利用 create-react-lirary 命令行工具构建 npm lib 库
subtitle: 共性可复用的代码，最好能抽取出来，形成独立的 lib 库。create-react-lirary 命令行工具，可以帮助快速构建一个 npm lib 项目
subject: npm
category: 精选推荐
tags: npm
keywords: create-react-lirary;
level: 200
cover: https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg
author: Chris Wei
created_when: 2021-02-25
updated_when: 2021-02-25
---

# 利用 create-react-lirary 命令行工具构建 npm lib 库

## 使用说明

#### 创建项目

```
npx create-react-library
```

> 注意项目名称，不能和已有的 npm lib 重名；

#### 运行开发模式

```
yarn start
```

#### 构建 npm lib

```
yarn build
```

#### 登录 npm

```
npm login
```

```
npm whoami
```

#### 发布新版本

```
npm deploy
```

> 注意版本号
