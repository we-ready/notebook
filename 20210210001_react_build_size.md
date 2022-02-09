---
id: 20210210001_react_build_size
title: create-react-app 脚手架构建的程序大小
subtitle: 作为单页应用，应用的尺寸直接影响加载速度，也就是用户体验。
subject: create-react-app
category: 最佳实践
tags: react
keywords: create-react-app;react-router-dom;styled-components;
level: 100
cover: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K
authors: Chris Wei
created_when: 2021-02-10
updated_when: 2021-02-10
---

# 20210210001_react_build_size

## 参考

#### 常规

|依赖|大小|备注|
|---|---|---|
|react|41.33 KB|最大chunk|
|+ react-router-dom|49.55 KB|增加了 `Exception` & `Welcome` 页面|
|+ styled-components|61.43 KB|增加了 `GlobalStyle` |
|+ material-ui|103.35 KB|增加了 `Button` `Dialog`|
|+ |105.28 KB|增加了一些页面|
|+ react-hook-form|116.09 KB|增加了一个 `form`|
|+ yup & @hookform/resolvers|135.85 KB|增加了几个 `form`|
|react-google-maps/api|15.5KB|通过懒加载实现 `google map lib` 在一个独立 `bundle` 中，最简单功能下的`bundle`大小为 15.5KB |

#### 其他

|依赖|大小|备注|
|---|---|---|
|基于以上配置|61.95 KB|删除大部分代码|
|+ i18next + i18next-browser-languagedetector + react-i18next|143.1 KB| 增加代码并引用所有的 `npm` |
|+ weready-base-front + weready-context-provider |145.68 KB|替换原有的简陋的 `UserContext`|
|+ crypto |279.3 KB|密码加密|
|- crypto |||
|+ node-md5 |147.17 KB|替换算法库|

#### 懒加载

|依赖|main|2|3|4|5|css|备注|
|---|---|---|---|---|---|---|---|
|以上配置懒加载前|21.75 KB|147.17 KB| <2 KB| | |||
|相同配置懒加载后|21.45 KB|29.29 KB|117.83 KB| <1 KB| <2 KB|727 B||

