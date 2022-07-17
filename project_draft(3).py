import mysql.connector

mydb = mysql.connector.connect(host="localhost",user = "root",passwd="paritosh",database ="draft")

mycursor = mydb.cursor()
mycursor.execute("select * from marks1")

for i in mycursor:
    print(i)