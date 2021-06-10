---
id: 20210303000_node_prj_with_ts
title: 从零开始构架一个支持 ts 语法的 nodejs 项目
subtitle: 如何 step by step 的构建一个支持 typescript 语法的 nodejs 项目
subject: typescript
category: 指导手册
tags: nodejs;typescript;npm
keywords: 
level: 200
cover: https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg
author: Chris Wei
created_when: 2021-03-03
updated_when: 2021-03-03
---

# 从零开始构架一个支持 ts 语法的 nodejs 项目

## 创建并配置

#### 创建项目目录

#### 进入项目目录并初始化 `package.json`

```
npm init
```

#### 增加对 `typescript` 的支持

```
npm install --save-dev typescript tslint @types/node
```

> `devDependencies` in `package.json`

#### 初始化 `ts` 开发环境

```
node_modules\.bin\tsc --init
```

> `tsconfig.json` 概要

- `include`   `ts`文件所在的文件夹
- `target`    `ts`编译成js的标准
- `module`    `ts`代码编译成什么模块系统
- `lib`       运行环境包含哪些 `api`
- `outDir`    编译后的输出目录
- `strict`    严格模式

#### 初始化语法检查 `tslint.json`

```
node_modules\.bin\tslint --init
```

> `tslint.json` 摘要

```
{
  "defaultSeverity": "error",
  "extends": [
    "tslint:recommended"
  ],
  "jsRules": {},
  "rules": {
    "noo-console": false
  },
  "rulesDirectory": []
}
```

#### 编译构建

```
node_modules\.bin\tsc
```

#### 运行

```
node ./dist/main.js
```

#### 安装 `ts-node`

```
npm install --save-dev ts-node
```

```
node_modules\.bin\ts-node ./src/main
```

#### 修改 `scripts` in `package.json`

```
  ... ...
  "scripts": {
    "start": "node_modules/.bin/ts-node ./src/main",
    "build": "node_modules/.bin/tsc",
  ... ...
```

#### 执行

```
yarn start
```
