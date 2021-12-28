---
id: 20210526000_regular_expression
title: 正则表达式
subtitle: 必定会遇到的问题
subject: 正则
category: 语法
tags: 
keywords: reg
level: 100
cover: https://geekboots.sfo2.cdn.digitaloceanspaces.com/post/regular-expression-1567485935882.jpg
author: Chris Wei
created_when: 2021-05-26
updated_when: 2021-05-26
---

# 正则表达式常规功能

## JS 中的字符串去掉特殊字符

```
const text = '1"2`3%4*5&6$7+8-9~0.a?b/c(d)e[f]g{h}='
const res = text.replace(/[~!@#$%^&*_+=?(){}\[\]\-\.\'\"\\\/\b\`\f\n\r\t]/g, '');
console.log(text, res)
```
