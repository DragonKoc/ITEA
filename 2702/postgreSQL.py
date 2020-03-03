import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="postgres",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")

cursor = con.cursor()
cursor.execute('create table b (id integer primary key, name varchar(30));')

print("Table created successfully")

con.commit()
con.close()