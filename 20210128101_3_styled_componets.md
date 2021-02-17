---
id: 20210128101_3_styled_components
title: styled-components 101
subtitle: 什么是 styled-components
subject: CSS-in-JS
category: 概念理解
tags: react;css;jsx;CSs-in-JS;styled-components;
keywords: fullstack
level: 100
cover: https://styled-components.com/logo.png
author: Chris Wei
created_when: 2021-01-28
updated_when: 2021-01-28
---

# styled-components 101

## 参考

- [Styled-Components 官网](https://styled-components.com/)
- [React 101](/blog/20210128101_2_react)

> Visual primitives for the component age

## styled-components 是什么

#### 将 `css` 样式和 `html` 标签封装成 `react` 组件

- `react` 将 `HTML` 和 `JS` 做了整合，形成了 `jsx`
- `styled-components` 进一步的将 `css` 做了进一步整合，纳入了 `jsx` 体系

#### 为什么说，`react` 没有统一 `css`

有关 `react` 通过 `jsx` 统一了 `html` 和 `js` 的说法，请参考 [React 101](/blog/20210128101_2_react)

以下代码可以看到，基础的 `react`，`css` 还仍然是割裂的。需要独立定义样式文件，然后在 `jsx` 中通过 `className` 指定样式。

`App.css`

```
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

`App.css`

```
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
```

## 其他好处

上述的，将 `css` 纳入 `jsx` 体系（`CSS-in-JS`），是 `styled-components` 最大的价值。除此之外，`styled-components` 还有很多其他价值，取代并超越了 `sass`，`less`，`module css`，等其他解决方案。

- 自动处理 `-moz`, `-webkit` 等浏览器兼容；
- 仍然兼容 `className`；
- 样式继承；
- 支持主题；
- 可动态配置的样式参数；
- 可动态配置的动画参数；


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

> 上面的代码可以看到，`css` 样式，被组件化了，被纳入到 `jsx` 了。而且，在进一步了解 `styled-components` 之后会发现，`styled-components` 支持样式接受组件的参数，从而使得样式也是可编程的，动态的，受控的。

```
const Button = styled.button`
  /* Adapt the colors based on primary prop */
  background: ${props => props.primary ? "palevioletred" : "white"};
  color: ${props => props.primary ? "white" : "palevioletred"};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;
```

除此之外，`styled-components` 还支持样式的继承，等等高级操作。这实际上相当于 `sass` `less` 中的 `mixin`，也类似于 `js` 中的 `class` 和 `interface` 的继承。
这样，我们可以丢弃 `sass` 和 `less`。丢弃 `sass` 和 `less`，意味着少了很多 `babel` 预处理相关的额外工作，意味着减少很大的学习成本。（`styled-components` 的学习成本，要远远小于 [ `sass` | `less` ] + `babel` ）