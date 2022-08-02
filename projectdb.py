import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="vandana", password="123456", database="dbconnect")
cur = mydb.cursor()
'''
mydb.commit()
mydb.close()

print('Connection created')
'''
cur.execute("select * from student")
for i in cur:
    print(i)