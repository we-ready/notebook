---
id: 20210129002_postman_skill
title: Postman的使用技巧
subtitle: 在调试后端接口时，postman 是比较常用的一个工具。挖掘深层功能，进一步提升开发与沟通效率。
subject: API
category: 经验技巧
tags: postman
keywords: 环境变量;js脚本
level: 200
cover: data:image/png;base64,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
author: Chris Wei
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