import sqlite3


sqlite_file = (r"files/sqlite.db")
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()

table_name = 'Archive'

sql = "CREATE TABLE IF NOT EXISTS " + table_name + "(first_name varchar NOT NULL, datetime)"
cursor.execute(sql)

sql = "INSERT INTO " + table_name + "(first_name,datetime) VALUES (\"value1\",CURRENT_TIMESTAMP)"
cursor.execute(sql)

conn.commit()
cursor.close()

#
# sqlite_file = (r"files/sqlite.db")
# conn = sqlite3.connect(sqlite_file)
# cursor = conn.cursor()
#
#
# table_name = 'Archive'
#
# sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + '("first_name" varchar NOT NULL, "second_name" varchar NOT NULL)'
# cursor.execute(sql)
#
# sql = 'INSERT INTO ' + table_name + '(first_name,second_name) VALUES ("value1","value2");'
# cursor.execute(sql)
#
#
# for rows in cursor.execute('select * from archive'):
#     print(rows)
