---
id: 20240117_daily_ops_of_jade
title: JADE 项目的日常运维
subtitle: PG数据库的备份
subject: DevOps
category: 操作手册
tags: 
keywords: postgres;backup
level: 200
cover: http://qiniuargus.weready.online/blog/desktop.jpg
authors: Chris Wei
created_when: 2024-01-17
updated_when: 2024-01-17
---

# JADE 项目日常运维

## 操作步骤

1. 远程连接服务器
  > `ssh`

2. 进入数据库运行时目录
  > `cd projects/atlas/database/script/`
   
3. 检查 docker 实例
  > `docker ps`

4. 进入 db 实例
  > `docker exec -it dbpg /bin/bash`
   
5. 进入实例内部的相应目录
  > `cd /script`

6. 执行备份
  > pg_dump -h dbpg -U postgres atlas > `date +%Y%m%d%H%M%S`.bak
   
7. 检查备份结果
  > `ls`

8. 退出容器回到主机环境
  > `exit`

9. 检查主机环境下的备份文件
  > `ls`

10. 异地复制（提前准备目标机 root 密码）
  > #1 jiabang `scp 2024*.bak 172.17.59.85:~/dbdump/`
  > #2 li      `scp 2024*.bak 172.22.48.193:~/dbdump/`
 
11. 删除本地备份
  > `rm -rf 2024*.bak`

12. 退出远程连接


## OSSUtil 工具

1. 安装
   `wget https://gosspublic.alicdn.com/ossutil/1.7.13/ossutil64`
2. 修改权限
   `chmod 755 ossutil64`
3. 生成配置文件
   `./ossutil64 config`
4. 上传文件
   `./ossutil64 cp [source] oss://[bucket]/path`
5. 具体上传命令
   `./ossutil64 cp ./projects/atlas/database/runtime/backup/dump-*.sql.gz oss://jadestore2024backup/rongyue/`
   `./ossutil64 cp ./projects/atlas/database/runtime/backup/dump-*.sql.gz oss://jadestore2024backup/xienan/`
   `./ossutil64 cp ./projects/atlas/database/script/2024*.bak oss://jadestore2024backup/jiabang/`
   `./ossutil64 cp ./projects/atlas/database/script/2024*.bak oss://jadestore2024backup/lishewen/`

  > 文件的时间戳是 `UTC` 时间，转换成北京时间需要 `+8` 小时

6. 删除本地文件
   `ls projects/atlas/database/runtime/backup/`
   `rm -rf  projects/atlas/database/runtime/backup/dump-*.sql.gz`

7. 检查磁盘空间
  `df -hl`


## 备份文件解压缩

  `gzip -d dump-2024xxxx_xxxxx.sql.gz`

## 从备份文件中还原数据库

  `pg_restore -C -U postgres -d atlas dump-2024xxxx_xxxx.sql`

> 还原数据库的时候，会出现报错：`error: could not execute query: ERROR:  option "locale" not recognized`
> 原因在于用于备份的定时任务 `Docker` 环境的版本，可能是 `pg v13`，所以会在 `sql` 脚本里增加 `locale` 信息
> 而我们的 `atlas` 采用的 `Docker` 环境是 `pg v12`，这个版本无法识别 `locale` 信息

## 解决方案

1. 停止 `docker-compose`
2. 进入 `projects/atlas/database/runtime`
3. 删除 `data` 目录下的全部内容
4. 编辑 `docker-entrypoint-initdb.d/initial.sh`
5. 注释掉最后一句：`sh initial.sh`
6. 重新启动 `docker-compose`
7. 进入 `dbpg` 容器 `docker exec -it dbpg /bin/bash`
8. 执行 `pg_restore -C -U postgres -d atlas dump-2024xxxx_xxxx.sql`

> 因为删除了 `runtime/data` 目录，`docker-compose` 再次启动时会执行 `docker-entrypoint-initdb.d/initial.sh`
> 因为注释掉了 `sh initial.sh`，`pg` 数据库只会创建一个空的数据库 `atlas`，而不会创建任何表、视图、函数等内容
> 再次执行 `pg_restore -C -U postgres -d atlas dump-2024xxxx_xxxx.sql` 虽然会报错，但只是 创建数据库 `atlas` 报错，而 `atlas` 我们已经创建好了。脚本里其他内容，因为 `atlas` 库已经存在，所以可以正常执行
> 这样，我们可以实现数据库的恢复