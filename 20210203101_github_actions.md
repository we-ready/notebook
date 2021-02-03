---
id: 20210203101_github_actions
title: github actions 101
subtitle: 如何利用 github actions 实现持续集成（CI）
subject: devops
category: 概念理解
tags: github;actions;CI
keywords: 持续集成
level: 100
cover: 
author: Chis Wei
created_when: 2021-02-03
updated_when: 2021-02-03
---

# github actions 101

## git repos

|repo|作用|性质|
|--:|---|---|
|blog|构建博客站点|public，博客源码|
|argus|demo|private，前端演示代码|
|we-ready.github.io|博客发布|public，github pages|

## github workflow

### 步骤

#### 创建目标 `repo` 的 `access token`

> `account profile` >>> `setting` >>> `developer setting` >>> `Personal access tokens` >>> `Generate new token`

> 不要急着关闭页面，生成的 `token` 在下一步要用

### 创建博客源 `repo` 的 `secrets`

> `repo` >>> `setting` >>> `Secrets` >>> `New repository secret`

> 这里的 `secret` 名称是：`GIT_ACCESS_TOKEN_OF_WE_READY`

### 创建 `github actions`

> `repo` >>> `Actions` >>> `New workflow` >>> `Publish Node.js Package` `Set up this workflow`

> 用以下内容替换生成的 `yml` 文件内容

```
# This workflow will run tests using node and then publish a package to GitHub Packages when a release is created
# For more information see: https://help.github.com/actions/language-and-framework-guides/publishing-nodejs-packages

name: Build All

on:
  push:
    branches:    
      - release

jobs:
  build:

    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [12.x]

    steps:
    - name: 1. Setup Node.js ${{ matrix.node-version }} ...
      uses: actions/setup-node@v1
      with:
        node-version: ${{ matrix.node-version }}

    - name: 2 Prepare empty folder ...
      run:
        mkdir output

    - name: 3.1 Checkout blog source code ...
      env:
        REPO_TARGET: github.com/we-ready/blog.git
      run:
        git clone --depth=1 -b main https://${REPO_TARGET} ./blog

    - name: 3.2 Build blog ...
      env:
        CI: false
      run: |
        cd ./blog
        npm install
        npm run build --if-present
        rm -rf ./public/*.map
        rm -rf ./public/*.txt
        cd ../

    - name: 3.3 Deploy result ...
      run:
        cp -r ./blog/public/. ./output

    - name: 4.1 Checkout argus/storybook source code ...
      env:
        REPO_TARGET: github.com/we-ready/argus.git
        GIT_ACCOUNT_TOKEN: ${{ secrets.GIT_ACCESS_TOKEN_OF_WE_READY }}
      run:
        git clone --depth=1 -b main https://${GIT_ACCOUNT_TOKEN}@${REPO_TARGET} ./argus

    - name: 4.2 Build argus/storybook ...
      env:
        CI: false
      run: |
        cd ./argus/npmlib/components/storybook
        npm install
        npm run build-storybook --if-present
        mv ./storybook-static/index.html ./storybook-static/storybook.html
        rm -rf ./storybook-static/*.map
        rm -rf ./storybook-static/*.txt
        cd ../../../../

    - name: 4.3 Deploy result ...
      run:
        cp -r ./argus/npmlib/components/storybook/storybook-static/. ./output

    - name: 5 Deploy to weready repo ...
      env:
        REPO_TARGET: github.com/we-ready/we-ready.github.io.git
        GIT_ACCOUNT_TOKEN: ${{ secrets.GIT_ACCESS_TOKEN_OF_WE_READY }}
      run: |
        git clone --depth=1 -b master https://${GIT_ACCOUNT_TOKEN}@${REPO_TARGET} ./weready
        cd ./weready
        find ! -regex '^./.git\(/.*\)?' -delete
        cp -r ../output/. ./
        git config --global user.email "yunzhi.wei@qq.com"
        git config --global user.name "we-ready"
        git add -A
        git commit -m "Update by github workflow actions"
        git push origin master

```
