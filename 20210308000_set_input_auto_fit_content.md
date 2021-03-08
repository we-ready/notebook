---
id: 20210308000_set_input_auto_fit_content
title: 如何设置 input 随着输入的内容而自适应宽度
subtitle: input 的宽度受 size 限制，很多解决方案是通过 js 代码去计算的
subject: React
category: 经验技巧
tags: input;width;
keywords: react;input;auto fit;useEffect;useMemo
level: 200
cover: https://media.inkscape.org/media/resources/file/Ladybug-icon.png
author: Chris Wei
created_when: 2021-03-08
updated_when: 2021-03-08
---

# 如何设置 input 随着输入的内容而自适应宽度

## 方法 1：利用一个隐藏的 `span`

```
const calculateWidth = (instance) => {
  return !instance ? null : window.getComputedStyle(instance).getPropertyValue("width");
}

const Component = ({placeholder}) => {
  const refSpan = useRef(null);
  const [spanWidth, setSpanWidth] = useState(null)
  const [input, setInput] = useState<string>('');
  
  const onChange = (e) => { 
    setInput(e.target.value) 
  }

  useEffect(() => {
    setSpanWidth(calculateWidth(refSpan?.current))
  }, [refSpan?.current, input]);

  return (
    <InputFieldContainer {...restProps} >
      <InputContainer validInput={!!input} >
        <SpanHelper ref={refSpan} className="debug">{input || placeholder}</SpanHelper>
        <InputPrefix className="debug">$</InputPrefix>
        <InputStyled className="debug" type={ type || 'text' } name={name} placeholder= {placeholder}
          value={input}
          width={spanWidth || 'auto'}
          onChange={onChange}
        />

```

> `useMemo` 会在渲染前执行
> `useEffect` 会在渲染后执行

## 方法 2：利用 `canvas` 内置的 `measureText` 方法

> 未成功：计算的结果，原小于正确的值

```
const calculateWidth = (instance, font, text) => {
  console.log('calculateWidth: ', instance, text);
  const context = instance?.getContext("2d");
  context.font= font || "16px Arial";
  context?.fillText(text, 0, 0)
  return Math.ceil(context?.measureText(text).width);
}

const refCanvas = useRef(null);
const [input, setInput] = useState<string>('');

const inputWidth = useMemo(()=> {
  return calculateWidth(refCanvas?.current, '16px Roboto', input || placeholder)
}, [refCanvas?.current, input]);


return(
  ...
      <InputContainer validInput={!!input} >
        <CanvasHelper ref={refCanvas} />
        <InputPrefix className="debug">$</InputPrefix>
        <InputStyled className="debug" type={ type || 'text' } name={name} placeholder= {placeholder}
          value={input}
          width={`${inputWidth}px`}
          onChange={onChange}
        />

```