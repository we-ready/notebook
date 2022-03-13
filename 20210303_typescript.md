---
id: 20210303_typescript
title: 什么是 Typescript
subtitle: ts和js/es是什么关系？使用ts有什么好处？如何构建一个支持 ts 语法的 nodejs 项目
subject: typescript
category: 概念理解
tags: typescript
keywords: javascript;typescript;js;es;ts
level: 200
cover: https://oscimg.oschina.net/oscnet/4d61b0d3264e651fde2e5a07d856381323d.jpg
authors: Chris Wei
created_when: 2021-03-03
updated_when: 2021-03-13
---

# 什么是 Typescript

## 关系梳理

- JS (Javascript)
  + 上世纪互联网出现之后，为了增强互联网用户访问网页的用户体验，网景 (Netscapte) 公司开发了一种可以随网页加载，并在浏览器中运行的脚本语言，名为 LiveScript 。而后，改名为 Javascript
  + 微软公司为了和网景公司在浏览器领域竞争，在 IE 浏览器里加入了类似的脚本语言，起名叫做 JScript

- ECMA (European Computer Manufacture)：欧洲计算机制造商协会
- ES (ECMAScript)
  + 随着浏览器层出不穷，大家互相竞争又各自为政，搞得互联网开发兼容问题不断，加之 Javascript 在满足各种开发需求方面，确实有很多短板要补
  + ECMA 基于 Javascript 和 JScript 开始制定标准，名叫：ES
  + 各方协商讨论（话语权之争）
  + ES 也有不同的版本迭代：ES6 = ES2015，ES2016，ES2017..., ES7, ES8, ...

- TS (Typescript)
  + 微软推出的编程语言（另起炉灶，独辟蹊径）
  + JS 是脚本型语言，是动态语言（可以直接在运行时中执行，语句只有在`运行时`才知道是否能执行，是否报错，是否有异常：`anyObj.whatEver()`）
  + TS 是静态语言，编译型语言（必须先由编译器编译成 JS 语言，编译时就会报错）
  + TS 语法是 ES 的超级，包含很多还在讨论中的 ES 语法
  + 语法层面完全兼容现有 JS

## 创建支持 TS 的项目

- 创建目录

- 项目初始化

```
npm init -y
```

> `package.json`

- 安装

```
yarn add -D typescript ts-node @types/node tslint

```

或者使用 `npm`

```
npm install --save-dev
```

> `devDependencies` in `package.json`

- 添加执行脚本 `package.json`

```
  ... ...

  "scripts": {
    "init:ts": "node_modules/.bin/tsc --init",
    "init:lint": "node_modules/.bin/tslint --init",
    "dev": "node_modules/.bin/ts-node ./main.ts",
    "build": "node_modules/.bin/tsc",
    "runjs": "node ./dist/main.js",
  ... ...
```

- 执行 `yarn init:ts`

> `tsconfig.json` 概要

|配置|说明|
|---|---|
|`include`|`ts`文件所在的文件夹|
|`target` |`ts`编译成js的标准, "ES3", "ES", "ES2017"|
|`module` |`ts`代码编译成什么模块系统|
|`lib`    |运行环境包含哪些 `api`, "dom", "ES2017"|
|`outDir` |编译后的输出目录|
|`strict` |严格模式|
|`removeComments`|
|`watch`|

- 修改

```
"outDir": "./dist", 
```

## TS 源码（兼容 JS）

- 创建文件 `main.ts`

```
console.log('hello world')
```

- 执行 `yarn build`
- 检查 `./dist/main.js`

## TS 源码（同样的 TS 语句，不同的 ES 版本）

- 更新文件 `main.ts`

```
const delay: (n: number) => Promise<any> = (n) => (
    new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(null)
        }, n * 1000)
    })
)

async function main() {
    console.log('>>> main +++', new Date())
    await delay(3)
    console.log('<<< main ---', new Date())
}

main()
```

- 执行 `yarn build`
- 检查 `main.js`
- 执行 `yarn runjs`

- 更新 `tsconfig.json`

```
"target": "es3",
```

```
"target": "es2017",
```

## 本地开发调试

```
yarn dev
```

## 语法

- 类型说明

  + 隐式声明

  ```
  let name = 'chris'
  name = 124
  ```

  + 显式声明

  ```
  let name: string = 'chris'
  name = 124
  ```

  ```
  let name: any = 'chris'
  name = 124
  ```

- 类型

```
type JobState = 'prepare' | 'doing' | 'done'
const s: JobState = 'done'
```

```
type MetaData = [number?, string?, boolean?]
const s: MetaData = []
s.push(123)
```

```
type MetaData = number | null
const s: MetaData = 12
```

- 枚举

```
enum JobState {
  new = 100,
  pending,
  working,
  completed,
  failed,
  abort,
}

const js: JobState = JobState.abort

console.log(js)
```

```
enum JobState {
  new = 'N',
  pending = "P",
  working = "W",
  completed = "C",
  failed = "F",
  abort = "A",
}

const js: JobState = JobState.abort
```

- 接口

```
interface Room {
  number: string;
  size: number;
  hasWindow?: boolean; 
  setTemp: (tmp: number) => void;
}

const room1: Room = {
}
```

- 函数接口

```
interface FnAdd {
  (a: number, b: number): number;
}

const fnAdd: FnAdd = (a, b) => (a + b)
```

- 函数参数及返回值

```
function fnAdd (a: number, b: number): number {
  return a + b
}
```

- 函数类型的变量

```
const fnAdd: (a: number, b: number) => number = (a, b) => a + b
```

## 其他

- 初始化语法检查 `tslint.json`

> `tslint.json` 摘要

```
{
  "defaultSeverity": "error",
  "extends": [
    "tslint:recommended"
  ],
  "jsRules": {},
  "rules": {
    "no-console": false
  },
  "rulesDirectory": []
}
```
