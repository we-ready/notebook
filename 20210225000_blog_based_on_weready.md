---
id: 20210225000_blog_based_on_weready
title: 如何利用 weready 构建自己的博客
subtitle: 利用博客，或者笔记，逐步梳理构建更新自己的知识体系
subject: 博客
category: 精选推荐
tags: blog;gatsby;github;workflow;CI;
keywords: 博客;构建;部署;定制;自动化
level: 200
cover: https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg
author: Chris Wei
created_when: 2021-02-25
updated_when: 2021-02-25
---

# 如何利用 weready 构建自己的博客

## 使用说明

1. `github` 上面申请一个代码库，用于存放文章，这里会称呼这个代码库为 `notebook repo`
1. `github` 上面再申请一个代码库，用于存放博客网站，这里会称呼这个代码库为 `blog repo`
1. `notebook repo` 需要创建 `release` 分支
1. `notebook repo` 需要启用 `workflow actions`
1. `notebook repo` 需要配置 `blog repo` 的访问权限
1. `blog repo`需要启用`pages`功能
1. `notebook repo` 引入自动构建的脚本 `.github/workflows/publish.yml` 文件（[参考：github actions 101](/blog/20210203101_github_actions)）
1. `notebook repo` 需要创建 `markdown` 文件
1. `notebook repo` 的本地更新，推送到 `github` （主分支）
1. `notebook repo` 的更新确认无误，确认要发布到博客网站的时候，将主分支合并到 `release` 分支，并推送到 `github`

推送动作会触发 `github` 工作流，工作流会自动完成以下工作：

1. 准备一台服务器
1. 安装 `nodejs` 环境
1. 克隆博客文章
1. 构建博客网站页面
1. 保存构建结果
1. 克隆演示项目文章（这里可以省略）
1. 构建演示项目结果（这里可以省略）
1. 保存构建结果（这里可以省略）
1. 推送到博客网站库

## 博客文件

博客文件是 格式的，但需要包含文件头，以`---`包围，在文件内容最前面

```
---
id: 20210225000_blog_based_on_weready
title: 如何利用 weready 构建自己的博客
subtitle: 利用博客，或者笔记，逐步梳理构建更新自己的知识体系
subject: 博客
category: 精选推荐
tags: blog;gatsby;github;workflow;CI;
keywords: 博客;构建;部署;定制;自动化
level: 200
cover: http://xxxxx.com/picture.png
author: Chris Wei
created_when: 2021-02-24
updated_when: 2021-02-24
---

# 博客标题

博客内容
```

## 定制

如果有前端开发经验，可以自行定制。

### 关键知识点

定制前，需要理解如下内容：

- `html`
- `css`
- `js`
- `nodejs`
- `github actions`
- `react`
- `styled-components`
- `gatsby`

### 系统构成

目前的博客系统，由三部分构成：`notebook repo` `blog repo` `factory repo`。前两个代码库前面已经讨论过，第三个代码库，就是存放网站构建代码的代码库。`factory repo`里面的代码，决定了网站的样式、路由、内容组织、内在逻辑。

### 定制

#### 为了实现自动化构建部署

1. `fork` `factory repo`
1. 修改 `notebook repo` 中的 `publish.yml`

#### 手动构建

1. 克隆自己的 `factory repo` 到本地
1. 本地执行 `yarn start` 可以本地定制开发调试
1. 本地执行 `yarn build` 可以本地构建
1. 本地构建的结果，可以手动推送到 `blog repo`

## 历史回顾

|代号|技术栈|
|---|---|
|Universal|Express + Ant Design + |
|Atlantis|pm2 + Redux + Saga|
|Aquoman|Nestjs + Ant Pro[Umi + Dva] + TypeORM|
|Alita|Material UI + React.FC + Formik|
|Athena|Nest + Ant Pro + i18n + GraphQL|
|Achellis|Nest + Ant Pro + Workflow Worker + Docker + K8S|
|Argus|Typescript + Nestjs 6 + Function Compoent + React Hook Context + Ant Design 4 + Gatsby + Material UI + Styled Components + StoryBook + react-hook-form + we-ready lib + i18n|
