---
id: 20210129002_postman_skill
title: Postman的使用技巧
subtitle: 在调试后端接口时，postman 是比较常用的一个工具。挖掘深层功能，进一步提升开发与沟通效率。
subject: API
category: 经验技巧
tags: postman
keywords: 环境变量;js脚本
level: 200
cover: https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg
videos: 
authors: Chris Wei
created_when: 2021-01-29
updated_when: 2021-01-29
---

# Postman的使用技巧

## 账号

可以注册 `postman` 账号，从而把本地的各种数据，同步到云端。

## 接口的组织

- `collection` - 可以用于组织不同项目，不同服务的接口
- `folder` - 可以用于组织不同业务场景，或者不同实体的相关接口

## 环境变量

- `environment` 可以定义多个可命名的环境
- `variable` 某个环境下，可以定义可复用的环境变量
- `global` 也有全局的环境变量

## API 请求地址栏

通过环境变量，写入可变的 `url` 地址 及 `port` 端口
```
http://{{hostname}}:{{portnumber}}/api/login
```

## Body

不要在 Body 里面写如固定的请求参数，而是使用一个环境变量，比如：`requestBody`

```
{{requestBody}}
```

## Pre-request

接口请求正式发送给后端服务 API 之前，`Pre-request` 中的脚本会被执行，因此，可以在这里，通过脚本，设置 `requestBody`

```
const functionName = "add";
const params = [119,111, { name: 'Chris', role: 'dev' }];

postman.setGlobalVariable("requestBody", JSON.stringify({
    functionName, 
    params
}));
```

## Test

接口请求完成之后，`Test` 中的脚本会被执行，因此，可以在这里，通过脚本，获取请求所获得的响应，进而设置相关的环境变量。例如，登录接口请求完成之后，可以根据响应信息，设置用户的`token`、`ID` 等信息

```
let res = JSON.parse(responseBody);

pm.environment.set("token", res.token);
pm.environment.set("credential_id", res.credential.id);
pm.environment.set("user_id", res.credential.user_id);
```

## 导入与导出

- 可以导出某个 `collection` 的全部接口定义
- 可以导出某个 `environment` 的全部 `variable`
- 导出的内容，可以作为 API 文档的补充，供开发人员参考