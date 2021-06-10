---
id: 20210601000_excel_pivot_table_mysql
title: 如何利用 Excel 的 Pivot Table 为运营提供数据报表
subtitle: 除了开发高度定制化的 Dashboard，可以利用 Excel 出报表
subject: 运营数据报表
category: 经验技巧
tags: excel;pivot table;mysql
keywords: 
level: 200
cover: https://media.inkscape.org/media/resources/file/Ladybug-icon.png
author: Chris Wei
created_when: 2021-06-01
updated_when: 2021-06-01
---

# 如何利用 Excel 的 Pivot Table 为运营提供数据报表

## 下载 mysql ODBC 驱动 并安装

[Connector/ODBC](https://dev.mysql.com/downloads/connector/odbc/)

## 操作系统添加数据源

> Windows 控制面板 ==>> 管理工具 ==>> ODBC Data Source (32-bit)

> User Name | Password | Database

## Excel 创建数据源

> Excel ==>> 数据 ==>> 获取数据 ==>> 自其他源 ==>> 从 ODBC

> SQL 语句

## 问题及解决

- SQL 执行报错，很可能是 32位 64位 版本问题。

> 可以尝试更换驱动程序。
