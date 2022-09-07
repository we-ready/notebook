---
id: 20220424_frontend_auto_scale
title: 前端自适应弹性布局
subtitle: 前端自适应弹性所需要了解的相关技术点
subject: auto-scale
category: 概念理解
tags: frontend;auto-scale
keywords: frontend;auto-scale
level: 100
cover: https://media.inkscape.org/media/resources/file/Koi_carp_2.svg
videos: 
authors: Chris Wei
created_when: 2022-04-24
updated_when: 2022-04-24
---

# CSS `Media` & `padding` tricky

```
import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.section`
  display: grid;
  place-items: center;
  height: 100vh;

  background: #06f;
  @media screen and (min-width: 800px) {
    background: #0af;
  }
  @media screen and (min-width: 1280px) {
    background: #0ff;
  }
`

const Card = styled.div`
  background: #fff;
  height: 30vh;
  border: 1px solid #f00;

  margin: 0 auto;
  width: calc(100% - 60px);
  @media screen and (min-width: 800px) {
    width: calc(100% - 120px);
  }
  @media screen and (min-width: 1280px) {
    width: 800px;
  }
`

const RatioFrame = styled.div`
  background: #fff;
  width: 50%;
`
const RatioPlaceHoder = styled.div`
  padding: 0 0 150% 0;
`

function StyleMedia() {
  return (
    <Wrapper>
      <h1>Auto Scale</h1>

      <Card />

      <RatioFrame>
        <RatioPlaceHoder />
      </RatioFrame>
    </Wrapper>
  );
}

export default StyleMedia;
```

# CSS `min`, `max` & `clamp`

```
import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.section`
  height: 100vh;
  background: #06f;

  /* display: grid;
  place-items: center; */

  @media screen and (min-width: 800px) {
    background: #0af;
  }
  @media screen and (min-width: 1280px) {
    background: #0ff;
  }
`

const Card = styled.div`
  height: 30vh;
  background: #fff;
  margin: 0 auto;

  /* width: 80%;
  max-width: 800px; */

  /* width: min(80%, 800px); */

  width: clamp(600px, 90%, 1200px);
`

function StyleMinMax() {
  return (
    <Wrapper>
      <h1>Auto Scale</h1>
      <Card>max-width</Card>
    </Wrapper>
  );
}

export default StyleMinMax;

```

# CSS `REM` & `EM`

```
import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.section`
  height: 100vh;
  background: #09f;

  display: grid;
  place-items: center;
`

const Card = styled.div`
  height: 30vh;
  background: #fff;
  text-align: center;

  font-size: 96px;
  width: 5rem;
`

function StyleRem() {
  return (
    <Wrapper>
      <h1>Auto Scale</h1>
      <Card>REM EM</Card>
    </Wrapper>
  );
}

export default StyleRem;

```

# JS event listener

```
import React, { useEffect, useState, useCallback } from 'react';
import styled from 'styled-components';

const Wrapper = styled.section`
  height: 100vh;
  font-size: 64px;
  text-align: center;

  display: grid;
  place-items: center;
`

function JSCode() {
  const [size, setSize] = useState({
    width: document.documentElement.clientWidth,
    height: document.documentElement.clientHeight,
  })

  const onResize = useCallback(() => {
    setSize({
      width: document.documentElement.clientWidth,
      height: document.documentElement.clientHeight,
    })
  }, [])

  useEffect(() => {
    window.addEventListener('resize', onResize);
    return(() => {
      window.removeEventListener('resize', onResize);
    })
  }, [])

  return (
    <Wrapper>
      <div>
        <h1>Auto Scale</h1>
        <p style={{
          color: (size.width > 800) ? 'green' : 'blue'
        }}>
          size sensor:
          {size.width} x {size.height}
        </p>
      </div>
    </Wrapper>
  );
}

export default JSCode;

```

# html `flex` & `grid`

```
import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.section`
  padding: 2rem;
`

const Card = styled.div`
  height: 98px;
  background: #09f;
  text-align: center;

  font-size: 64px;
  width: 98px;
`

// const List = styled.div`
//   border: 1px solid #f00;

//   display: flex;
//   gap: 8px;
//   flex-wrap: wrap;
//   justify-content: space-between;
// `

const List = styled.div`
  border: 1px solid #f00;

  display: grid;
  grid-gap: 8px;
  grid-template-columns: repeat(auto-fill, 98px);
  justify-content: space-between;
  align-content: start;
`

const items = new Array(13).fill(' ')
function Element() {
  return (
    <Wrapper>
      <List>
      { items.map((x, i) => (
        <Card key={i}>{i}</Card>
      )) }
      </List>
    </Wrapper>
  );
}

export default Element;

```
