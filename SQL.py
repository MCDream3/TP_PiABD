import mysql.connector

connection = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='zamowieniaPrzyklad',auth_plugin='mysql_native_password')

query = 'SELECT * FROM klienci'

cursor = connection.cursor
cursor.execute(query)

for row in cursor:
    print(row)
