---
id: 20210128_styled_components
title: styled-components 让 React 如虎添翼 
subtitle: 在 React 的 jsx 基础上，styled-components 通过 ES 的模板字符串 + Tag，进一步的将 `css` 整合纳入了 `js`，实现了样式的 组件化、可编程
subject: CSS-in-JS
category: 概念理解
tags: react;css;sass;less;styled-components;CSs-in-JS
keywords: styled-components
level: 100
cover: https://styled-components.com/logo.png
videos: https://qiniuargus.weready.online/blog/sharing/video/2022-03-17-styled-components.mp4
authors: Chris Wei
created_when: 2021-01-28
updated_when: 2022-03-17
---

# styled-components 入门与动手实践

## styled-components 是什么

> 将 `css` 样式和 `html` 标签封装成 `react` 组件

- `react` 通过 `jsx` 将 `HTML` 和 `JS` 进行整合，让 `HTML` 和 `JS` 实现你中有我，我中有你，实现了 `HTML`：模块化、可编程
- `styled-components` 通过 `ES` 的模板字符串、`Tag`，进一步的将 `css` 整合纳入了 `js`，实现了 `css`：组件化、可编程

> 有关 `react` 通过 `jsx` 统一了 `html` 和 `js` ，请参考 [React 101](/blog/20210128_react)

## `react` 如何设置样式

- 创建 `react` 项目

```
npx create-react-app mydemo
```

- `App.jsx`

```
... ...

import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          ... ...
        >
    ... ...
```

- `App.css`

```
.App { ... ... }
.App-logo { ... ... }
@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: ... ...
  }
}
.App-header { ... ... }
.App-link { ... ... }
@keyframes App-logo-spin { ... ... }
```

> 以上代码可以看到，基础的 `react`，`css` 还仍然是割裂的。需要独立定义样式文件，然后在 `jsx` 中通过 `className` 指定样式；而且，没有可变成能力；

> 其他方案，比如 `sass`、`less`、`module css`、`css 变量`，有增强，但没有从本质上解决问题，而且需要付出比较大的额外成本

## `styled-components` 的功能概要

> 将 `css` 通过 `模板字符串` + `Tag` 纳入了 `jsx` 体系（`CSS-in-JS`）

- 仍然兼容 `className`
- 自动处理 `-moz`, `-webkit` 等浏览器兼容
- 样式继承
- 支持主题
- 全局样式
- 可动态配置的样式参数
- 可动态配置的动画参数

#### 分解动作逐一说明

- 安装

```
yarn add styled-components
```

- 告别无意义的原始 `html` 标签（尤其是 `div` 满天飞）

```
const LinkButton = styled.a``
```

> 浏览器调试模式，检查编译后的结果

- `class` 命名避免冲突

```
  & span {
    font-weight: 700;
  }
```

- `css` 类似的选择器语法

```
  &:hover {
    box-shadow: 
      0px 9px 12px rgba(0, 0, 0, 0.14),
      0px 3px 16px rgba(0, 0, 0, 0.12),
      0px 5px 6px rgba(0, 0, 0, 0.2);
  }
```

```
  &.class-name
  & ~ &
  & + &
```


- 告别无意义的原始 `html` 标签（尤其是 `div` 满天飞）

```
  cursor: pointer;
  color: white;
  background: linear-gradient(#00f, #00a);
  border-radius: 6px;
  border: none;
```

- 样式参数动态可编程

```
  height: ${props => props.size};
  line-height: ${props => props.size};
  font-size: ${props => `calc(${props.size} - 8px);`};
```

> 利用模板字符串的嵌套

-  多态（变种）

```
  ${props => props.frame && css`
    color: black;
    background: white;
    border: 1px solid #00f;
  `}
  ${props => props.disabled && css`
    color: #333;
    background: #777;
    cursor: not-allowed;
  `}
```

- 继承

> 相当于 `sass` `less` 中的 `mixin`，但完全是 `js` 风格和思维

- 全局样式

`index.tsx`

```
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background: transparent;

  .debug-r {
    outline: 1px solid #f00;
  }

  img, iframe {
    loading: lazy;
  }
}
```

- 动效

```
const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

const Rotate = styled.div`
  display: inline-block;
  animation: ${rotate} 2s linear infinite;
`;
```

#### `typescript`

> 定义 `interface`

## 参考

- [Styled-Components 官网](https://styled-components.com/)
- [React 101](/blog/20210128101_2_react)
- [React Website Using Styled Components - Beginner React JS Project Fully Responsive](/watch?v=iP_HqoCuRI0&t=5941s)

> Visual primitives for the component age
