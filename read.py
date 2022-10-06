import mysql.connector
import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="passwordbd",
    database="namebd"
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print(results)