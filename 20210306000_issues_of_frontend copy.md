---
id: 20210306000_issues_of_frontend
title: 前端开发中的疑难杂症
subtitle: 前端开发中的掉坑和出坑记录
subject: Issues
category: 疑难杂症
tags: form
keywords: bug;issue
level: 200
cover: https://media.inkscape.org/media/resources/file/Ladybug-icon.png
author: Chris Wei
created_when: 2021-03-06
updated_when: 2021-03-06
---

# 前端开发中的疑难杂症

## 表单内任意的 `button` 点击都会触发 `submit`

> 在自定义表单组件的时候，任何情况下，都需要避免使用 `button`

## `react-hook-form` 向自己二次封装的表单传入 onSubmit 的时候，需要二次传递，而不能直接作为 `handleSubmit` 的参数

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