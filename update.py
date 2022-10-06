import mysql.connector
import datetime

connection = mysql.connector.connect (
    host="localhost",
    user="username",
    password="passwordbd",
    database="namebd"
)

cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = (
    'First User Edited',
    'firstuseredited@teste.com.br',
    1
)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, "Records changed")

