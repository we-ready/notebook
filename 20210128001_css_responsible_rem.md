---
id: 20210128001_css_responsible_rem
title: font-size，em，rem在响应式布局中的应用
subtitle: 响应式布局，不再以所谓“像素的精准”为追求目标，而是追求页面能够自适应不同屏幕的尺寸
subject: 响应式布局
category: 实战技巧
tags: css
keywords: rem;em;px
level: 300
cover: http://qiniuargus.weready.online/blog/coder.jpg
author: Chis Wei
created_when: 2021-01-28
updated_when: 2021-01-28
---

# font-size，em，rem在响应式布局中的应用

## `px`，`em`，`rem` 概要

- `px` 代表像素尺寸；
- `em` 表示当前DOM元素 `font size`，或者父级（向上追溯）DOM元素的 `font size`;
- `rem` 表示根（`html`）元素 `font size`;

## 背景

为了实现响应式布局，页面针对不同的屏幕尺寸，需要动态调整大小。而页面上，最丰富的元素，就是`文字`。如何方便高效的设置并动态调整`文字`大小，就成了动态布局中，一个课题。

## 经验技巧

- 根（`html`）元素中明确设定 `font size`，缺省设置为：`16px`；浏览器尺寸变化时，尽量不动态调整；从而保持全局的统一；
- 页面局部范围，如果有需要，明确的设定`font size`；当浏览器尺寸变化时，动态调整；
- 所有跨页面复用的组件尺寸，采用 `rem` 为尺寸单位，并暴露 `size` 属性，并根据该属性动态调整组件大小；这样，所有组件，在不同页面，会有一个统一的效果；
- 所有局部相关的展示，采用 `em` 为尺寸单位；这样，不同的局部，同样的样式标签，也会呈现不同的尺寸，满足不同局部的需要；
