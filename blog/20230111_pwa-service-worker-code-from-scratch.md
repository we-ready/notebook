---
id: 20230111_pwa-service-worker-code-from-scratch
title: React 项目从零开始写代码支持 service worker
subtitle: ES语法
subject: service worker
category: 配套源码
tags: react;service worker
keywords: service worker
level: 200
cover: https://oscimg.oschina.net/oscnet/4d61b0d3264e651fde2e5a07d856381323d.jpg
authors: Chris Wei
created_when: 2023-01-11
updated_when: 2023-01-11
---

# service worker code from scratch in React

#### `swReg.ts` in `src`

```
const URL_SW = `${process.env.PUBLIC_URL}/sw.js`;

export function register() {
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register(URL_SW).then((result) =>{
        console.log("!!!!!! service worker register result", result)
      })
    })
  }
}
```

#### `sw.js` in `public`

```
console.log('###### service worker loaded!')

const CACHE_NAME = 'PWA_SW_DEMO_V1';
const CACHE_LIST = [
  `/static/js/bundle.js`,
  '/static/media/logo.103b5fa18196d5665a7e12318285c916.svg',
  '/manifest.json',
  '/favicon.ico',
  '/logo192.png',
  `/index.html`,
  '/',
  '/about',
  '/home',
  '/todo',
]

this.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(CACHE_LIST);
    })
  )
})

this.addEventListener('fetch', (event) => {
  // console.log('fetch event ', event)
  // if (!navigator.onLine)
  {
    event.respondWith(
      caches.match(event.request).then((cachedRes) => {
        console.log('search cached response', cachedRes)
        if (!!cachedRes)
        {
          return cachedRes
        }
        // else
        return fetch(event.request).then((response) => {
          console.log('fetch response to cache', response)
          if(!response || response.status !== 200) {
            console.error('response not accepted')
            return response;
          }

          // IMPORTANT: response will be sonsumed by DOM, so 
          // we need to clone a new one for cache
          const res4Cache = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            console.log('cache', event.request, res4Cache);
            return cache.put(event.request, res4Cache);
          })

          return response;
        }); // .catch(() => caches.match('offline.html'));
      })
    )
  }
})

this.addEventListener('activate', (event) => {
  const whiteList = [CACHE_NAME];
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((name) => {
          if (!whiteList.includes(name)) {
            return caches.delete(name);
          }
        })
      )
    })
  )
})
```

#### `manifest.json` in `public`

```
  ...
  "purpose": "any maskable"
  ...
```

#### reference

> [web.dev](https://web.dev/progressive-web-apps/)
> [PWA example squoosh](https://squoosh.app/)
