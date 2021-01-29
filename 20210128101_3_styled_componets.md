---
id: 20210128101_3_styled_components
title: styled-components 101
subtitle: 什么是 styled-components
subject: react
category: 概念理解
tags: react;css;styled-components
keywords: fullstack
level: 100
cover: https://styled-components.com/logo.png
author: Chis Wei
created_when: 2021-01-28
updated_when: 2021-01-28
---

# styled-components 101

## 参考

- [Styled-Components 官网](https://styled-components.com/)

> Visual primitives for the component age

## styled-components 是什么

#### 将 `css` 样式和 `html` 标签封装成 `react` 组件

- `react` 将 `HTML` 和 `JS` 做了整合，形成了 `jsx`
- `styled-components` 进一步的将 `css` 做了进一步整合，纳入了 `jsx` 体系

## 入门

```
const Button = styled.a`
  /* This renders the buttons above... Edit me! */
  display: inline-block;
  border-radius: 3px;
  padding: 0.5rem 0;
  margin: 0.5rem 1rem;
  width: 11rem;
  background: transparent;
  color: white;
  border: 2px solid white;

  /* The GitHub button is a primary button
   * edit this to target it specifically! */
  ${props => props.primary && css`
    background: white;
    color: black;
  `}
`

render(
  <div>
    <Button
      href="https://github.com/styled-components/styled-components"
      target="_blank"
      rel="noopener"
      primary
    >
      GitHub
    </Button>

    <Button as={Link} href="/docs">
      Documentation
    </Button>
  </div>
)
```
