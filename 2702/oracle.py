import cx_Oracle

connection = cx_Oracle.connect("system", "Oracle123", "localhost/docker")

cursor = connection.cursor()
cursor2 = connection.cursor()

cursor.execute("""
    SELECT *
    FROM max1
    WHERE num = :val""",
    val = 2)
print("YEAP!")

cursor2.execute("""
    SELECT *
    FROM max1
    """,)
print("YEAP!")

for row in cursor:
    print(row)
print('*********')
for row2 in cursor2:
    print(row2)

cursor.close()
cursor2.close()