
# Linux

- cd ~
- ls
- pwd
- rm [-rf]
- vim
- psql -l
- psql MBDI
  
- dropdb --if-exists pkmon
- createdb pkmon
- psql pkmon -f pkmon.dump.sql

# vim

- i       (insert)
- ESC
- dd
- :wq

# inside psql

-  \l
-  \d [table name]
-  \dt
-  \dv
-  \df
-  \dD
-  \dT
-  \dT+ [type name]
-  SELECT enum_range(null::[type name]);

-  select * from dbpop();

-  [tab] for auto complete

-  [ctrl-c] to break current command output

