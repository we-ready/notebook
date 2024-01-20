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
