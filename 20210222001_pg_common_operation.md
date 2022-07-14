---
id: 20210222001_pg_common_operation
title: postgres 数据库的常规操作
subtitle: pg数据库运维中的常规操作命令
subject: 运维
category: 指导手册
tags: postgresql;devops;sql
keywords: 
level: 200
cover: https://media.inkscape.org/media/resources/file/Koi_carp_2.svg
authors: Chris Wei
created_when: 2021-02-22
updated_when: 2021-02-22
---

# postgres 常规命令

## 更新

- 示例

```
select credential, password from dbt_user_credentials where credential='xxx';
update dbt_user_credentials set password='25d55ad283aa400af464c76d713c07ad' where credential='xxx';
```
