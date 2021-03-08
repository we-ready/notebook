---
id: 20210308000_get_react_component_style_value
title: 如何获取 React 组件的样式属性的当前值
subtitle: 正向设置 React 组件的样式很常见，但仍然有时候需要动态获取某个组件的属性的当前值
subject: React
category: 经验技巧
tags: form
keywords: react;componet;style
level: 200
cover: https://media.inkscape.org/media/resources/file/Ladybug-icon.png
author: Chris Wei
created_when: 2021-03-08
updated_when: 2021-03-08
---

# 如何获取 React 组件的样式属性的当前值

```
const refX = useRef();
...
const answer = window.getComputedStyle(refX.current).getPropertyValue("margin-left");
...
<Component ref={refX} />
...
```
