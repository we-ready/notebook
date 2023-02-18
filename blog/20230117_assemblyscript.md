---
id: 20230117_assemblyscript
title: 创建一个基于AssemblyScript语法的WASM项目
subtitle: AssemblyScript语法的WASM项目
subject: AssemblyScript
category: 配套源码
tags: wasm;webassembly;assemblyscript
keywords: wasm
level: 200
cover: https://oscimg.oschina.net/oscnet/4d61b0d3264e651fde2e5a07d856381323d.jpg
authors: Chris Wei
created_when: 2023-01-17
updated_when: 2023-01-17
---

# create wasm project based on assemblyscript

#### `wasm.ts` in `/src` (react)

```
export const lib:any = {};

WebAssembly.instantiateStreaming(
  fetch(`${process.env.PUBLIC_URL}/release.wasm`),
  {
    "env": {
      abort() {
        console.error('abort from wasm')
      }
    },
    "utils": {
      callback(r: number) {
        console.log('callback: ', r);
      }
    }
  }
).then(wasmModule => {
  console.log('initial result: ', wasmModule);
  lib.exFunction = wasmModule?.instance?.exports;
});
```

#### `utils.ts` in `assembly`

```
export declare function callback(t: u32): void;
```

#### `index.js` in `assembly`

```
import { callback } from "./utils";

export function add(a: i32, b: i32): i32 {
  if (a<0 || b<0) callback(a+b);
  return a + b;
}
```

> [webassembly](https://webassembly.org/)
