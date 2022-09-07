---
id: 20210322000_chii_h5_web_page_debug
title: 使用 chii 调试移动端页面
subtitle: 网站页面在不同浏览器上，显示效果会有差异，尤其在移动端的浏览器差异，调试需要额外工作
subject: website
category: 精选推荐
tags: 
keywords: chii
level: 100
cover: https://cdn.pixabay.com/photo/2012/06/19/10/32/owl-50267_960_720.jpg
authors: Chris Wei
created_when: 2021-03-22
updated_when: 2021-03-22
---

# 使用 chii 调试移动端页面

#### 安装

```
npm install chii -g
```

#### 启动

```
chii start -p 8080
```

#### 使用

浏览器打开：`localhost:8080`

#### 检查开发电脑的局域网 IP 地址

```
ipconfig
```

> 假设电脑本机`IP`地址是：`10.0.0.10`

#### 网站注入脚本

```
<script src="http//10.0.0.10:8080/target.js"></script>
```

#### 启动网站应用

> 假设网站应用运行在端口：`9090`

#### 手机浏览器打开网站应用

```
http://10.0.0.10:9090
```

#### 继续使用并调试

回到浏览器`localhost:8080`页面
点击 `inspect`
