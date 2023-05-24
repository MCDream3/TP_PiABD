import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\1Egr2\Desktop\ACCESS\ZamowieniaPrzyklad.accdb;')


cursor = conn.cursor
cursor.execute('select * from pracownicy')

for row in cursor.fetchall():
    print(row)
