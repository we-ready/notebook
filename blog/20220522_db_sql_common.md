---
id: 20220522_db_sql_common
title: 数据库SQL基础
subtitle: 
subject: 数据库相关基础知识
category: 经验技巧
tags: sql;db;database;运维;
keywords: 
level: 200
cover: https://media.inkscape.org/media/resources/file/Ladybug-icon.png
authors: Chris Wei
created_when: 2021-06-05
updated_when: 2022-05-22
---

# 数据库SQL基础

## 创建表

```
CREATE TABLE t_class (
  id                  serial not null PRIMARY KEY,
  name                text,
  memo                text,
  balance             int NOT NULL DEFAULT 20,
  updated_when        timestamp DEFAULT current_timestamp,
  ex_info             jsonb,
  UNIQUE           (name)
);

CREATE TABLE t_student (
  id                  serial not null PRIMARY KEY,
  name                text,
  gender              text NOT NULL DEFAULT 'MALE',
  age                 int NOT NULL DEFAULT 20,
  class_id            serial REFERENCES t_class (id)
);

```

## 增表内加记录

```
INSERT INTO t_class (name, memo, balance, ex_info)
VALUES
  ('2022001', 'momo111', 10, '{"x": "123", "y": "456"}'),
  ('2022002', 'momo222', 20, '{"x": "xxx", "y": "yyy"}'),
  ('2022003', 'momo333', 30, '{"x": "123", "y": "456"}')
;

INSERT INTO t_student (name, class_id)
VALUES
  ('Alice', 1),
  ('Bob', 2),
  ('Chris', 3),
  ('Angel', 1),
  ('Peter', 2),
  ('Tom', 3),
  ('Jerry', 1),
  ('John', 2),
  ('Jack', 3)
;
```

## 查询表内加记录

- 无条件全部记录

```
SELECT * FROM t_class;
SELECT * FROM t_student;
```

- 按条件查询

```
SELECT * FROM t_class
WHERE balance=10;
```

- 排序

```
SELECT * FROM t_class
ORDER BY balance;

SELECT * FROM t_student
ORDER BY class_id, name;
```

## 修改表内加记录

```
UPDATE t_class
SET memo='update by update'
WHERE balance=10;
```

## 删除表内加记录

```
DELETE FROM t_student
WHERE name='John';
```

## 关联表查询

```
SELECT  s."name" as "sname", s."id" as "sid", c.*
FROM t_student s
LEFT JOIN t_class c ON (c.id=s.class_id)
;
```

## 创建视图

```
CREATE OR REPLACE VIEW v_student AS
  SELECT  s."name" as "sname", s."id" as "sid", c.*
  FROM t_student s
  LEFT JOIN t_class c ON (c.id=s.class_id)
;
```

```
CREATE OR REPLACE VIEW v_class AS
    SELECT  c.*,
            s.name AS sname,
            json_build_object(
              'name',     s.name,
              'gender',   s.gender,
              'age',      s.age
            )::JSON AS student
    FROM t_class c
    LEFT JOIN t_student s ON c.id=s.class_id
;
```

### 时间过滤 (mysql)

#### 今天的数据

```
SELECT * FROM 表名 WHERE to_days(时间字段) = to_days(now());
```

#### 昨天的数据

```
SELECT * FROM 表名 WHERE to_days(now()) - to_days(时间字段) <= 1;
```

#### 近7天的数据

```
SELECT * FROM 表名 WHERE date_sub(curdate(), interval 7 day) <= date(时间字段);
```
