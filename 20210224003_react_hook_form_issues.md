---
id: 20210224003_react_hook_form_issue
title: react-hook-form 使用中的注意事项
subtitle: react-hook-form 使用中的注意事项
subject: 表单
category: 疑难杂症
tags: react-hook-form
keywords: bug;issue
level: 200
cover: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K
author: Chris Wei
created_when: 2021-02-24
updated_when: 2021-02-24
---

# react-hook-form 使用中的注意事项

## 表单内任意的 `button` 点击都会触发 `submit`

> 在自定义表单组件的时候，任何情况下，都需要避免使用 `button`

## 向自己二次封装的表单传入 onSubmit 的时候，需要二次传递，而不能直接作为 `handleSubmit` 的参数

> 正确的方式

```
export default function LoginForm ({toLogin}) {

  ...

  const onSubmit = (values) => {
    if (!!toLogin) toLogin(values)
  }
  return (
    <FormContainer>
      <form onSubmit={handleSubmit(onSubmit)}>
  
  ...

```

> 错误的方式

```
export default function LoginForm ({toLogin}) {

  ...

  return (
    <FormContainer>
      <form onSubmit={handleSubmit(toLogin)}>
  
  ...
```
