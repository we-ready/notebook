---
id: 20210125004_pg_backup_restore
title: postgres 数据库的备份与恢复
subtitle: pg数据库的全备份，以及数据恢复
subject: 运维
category: 指导手册
tags: postgresql;devops
keywords: 数据备份;数据恢复
level: 200
cover: http://qiniuargus.weready.online/blog/coder.jpg
author: Chis Wei
created_when: 2021-01-25
updated_when: 2021-01-25
---

# postgres 数据库的备份与恢复

## 参考

- [1](https://www.jianshu.com/p/0602d5c77b8f?tdsourcetag=s_pcqq_aiomsg)

## 备份

#### 命令格式

```
pg_dump -h [host] -U [user] [database] > [output file]
```

```
#!/bin/bash

pg_dump -h dbpg -U postgres [database] > /backup/pgdump.sql
mv -f /backup/pgdump.sql /backup/pg_dump_`date +%Y%m%d%H%M%S`.sql
```

## 恢复

### Option 1

#### 进入容器 `dbpg`
#### 进入脚本目录

```
cd script
```

#### 进入数据库

```
psql -d archellis -U postgres
```

#### 清空数据

```
\i clear_all.sql;
```

#### 恢复数据

```
\i pg_dump_xxxxxxx.sql;
```

### Option 2

#### 登录数据库

```
psql -U postgres 
```

#### 断开所有连接

```
SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE datname = 'archellis' AND pid <> pg_backend_pid();
```

#### 退出登录

```
\q
```

#### 删除数据库

```
dropdb -U postgres [database]
```

#### 创建数据库

```
createdb -U postgres [database]
```

#### 恢复数据

```
psql -d [database] -U postgres -f pg_dump_xxxxxxxx.sql
```
