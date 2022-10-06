import mysql.connector
import datetime 

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="passwordbd",
    database="namebd"
)

cursor = connection.cursor()

sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
    'First User',
    'firstuser@teste.com.br',
    datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("There is a new user registered with de ID: ", userid)