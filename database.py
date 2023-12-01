import sqlite3

conn = sqlite3.connect("mydata.db")

sql = "CREATE TABLE blocks(name TEXT, description TEXT)"
sql = "SELECT * FROM blocks ORDER BY 1"
cursor = conn.cursor()

cursor.execute(sql)
res = cursor.fetchall()
for r in res:
    print("Name: ", r[0])
    print("Description: ", r[1])

conn.close()