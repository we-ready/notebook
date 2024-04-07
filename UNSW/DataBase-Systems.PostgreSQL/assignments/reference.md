# 备忘

- 使用 `jade-jiabang` 作为跳板机
- 登录 `jade-jiabang` 可以查看历史命令
- 登录学生作业虚机（`nw-syd-vxdb2`）
  
  ```
  ssh z5374158@d2.cse.unsw.edu.au
  ```

  > 密码：Nsfz2024!Nsfz2024!

- 登录虚机（`nw-syd-vxdb2`）后执行

  ```
  source /localstorage/$USER/env
  p1
  ```

- 进入数据库

  ```
  psql -l
  psql MBDI
  ```

- 退出虚机（`nw-syd-vxdb2`）前执行

  ```
  p0
  ```

- !!! 虚机 `nw-syd-vxdb2` 的 `home` 目录下的 `zhuge` 目录 !!!


# `pkmom` 数据库

- `pkmon` 数据库相关操作

  ```
  dropdb --if-exists pkmon
  createdb pkmon
  psql pkmon -f pkmon.dump.sql
  ```

  ```
  select * from dbpop();
  ```

- 

# 原始参考信息

https://cgi.cse.unsw.edu.au/~cs3311/24T1/pracs/01/index.php
https://cgi.cse.unsw.edu.au/~cs3311/24T1/assignments/ass1/index.php
https://cgi.cse.unsw.edu.au/~cs3311/24T1/assignments/ass1/testing.php
https://webcms3.cse.unsw.edu.au/COMP3311/24T1/

ssh z5374158@d2.cse.unsw.edu.au

账号：z5374158@ad.unsw.edu.au
密码：Nsfz2024!Nsfz2024!

$ source /localstorage/$USER/env
$ p1
$ p0
$ 3311 autotest ass1
$ give cs3311 ass1 ass1.sql
$ 3311 classrun -collect ass1


$ python --version
$ python3 --version
$ python3


$ /home/cs3311/web/23T1/lectures/week07-tuesday/exercises/uni.dump
$ cp /home/cs3311/web/23T1/lectures/week07-tuesday/exercises/uni.dump .

$ ln -s /web/cs3311/current/assignments/ass2/database/pkmon.dump.sql .


$ python aa.py


Tony

