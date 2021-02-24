---
id: 20210224004_react_lazy_suspense
title: react 中的懒加载
subtitle: 利用最新的 react 懒加载，可以将单页应用由一个大的 chunk 分成多个小chunk，部分组件，只有需要的时候才加载
subject: 开发环境
category: 经验技巧
tags: react
keywords: lazy;suspense;chunk
level: 200
cover: data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K
author: Chris Wei
created_when: 2021-02-24
updated_when: 2021-02-24
---

# react 中的懒加载

#### 常规代码

```
import LoginForm from '../forms/Login'

...

  <Dialog open={open === 'dialog'} onClose={() => setOpen(false)} >
    <LoginForm toLogin={toLogin} />
  </Dialog>
...

```

#### 懒加载代码

```
const LoginForm = lazy(() => import('../forms/Login'))

...

  <Dialog open={open === 'dialog'} onClose={() => setOpen(false)} >
    <Suspense fallback="Loading ...">
      <LoginForm toLogin={toLogin} />
    </Suspense>
  </Dialog>
...
```

> `LoginForm` 中包含了很多不是很常用的 `npm` 包（react-hook-form, @hookform/resolvers, yup, node-md5, 等等）
