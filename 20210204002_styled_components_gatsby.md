---
id: 20210204002_styled_components_gatsby
title: gatsby 项目中如何引入并正确使用 styled-components
subtitle: gatsby 项目中，如果不引入插件，styled-components 的样式可能会丢失
subject: 前端开发
category: 指导手册
tags: gatsby;styled-components
keywords: plugin
level: 100
cover: https://cdn.pixabay.com/photo/2017/02/07/16/47/kingfisher-2046453_960_720.jpg
author: Chris Wei
created_when: 2021-02-04
updated_when: 2021-02-04
---

# gatsby 项目中如何引入并正确使用 styled-components

## 问题描述

`gatsby` 项目中，对于根据模版生成的页面，当通过页面的 `url` 直接访问的时候（而非从主页链接跳转到页面），页面中 `styled-components` 的样式会丢失。

#### 情况说明

`gatsby` 自动生成的 `class` 名称，在生产环境下，当 `url` 直接访问页面的时候，会和从主页链接跳转到页面时，不同，导致样式丢失。

#### `gatsby` 项目中正确使用 `styled-components` 需要

1. 安装 `styled-components` 极其插件

```
$ yarn add styled-components gatsby-plugin-styled-components babel-plugin-styled-components
```

2. 在 `gatsby-config` 中正确配置

```
module.exports = {
  plugins: [`gatsby-plugin-styled-components`],
}
```

> 如果需要进行服务端渲染等高级功能，可以通过 `options` 对插件进行进一步的配置

## 参考

- [Gatsby Docs](https://www.gatsbyjs.com/docs/how-to/styling/styled-components/)
- [Using styled-components in Gatsby](https://www.digitalocean.com/community/tutorials/gatsbyjs-using-styled-components-in-gatsbyjs)
