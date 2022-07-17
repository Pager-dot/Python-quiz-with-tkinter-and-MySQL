from re import sub
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="paritosh",
                               database="draft")
mycursor = mydb.cursor()
 
# Fecthing Data From mysql to my python progame
mycursor.execute("select sub1, sub2 from marks1")
result = mycursor.fetchall
 
sub1 = []
sub2 = []
 
for i in mycursor:
    sub1.append(i[0])
    sub2.append(i[1])
     
print("Name of Students = ", sub1)
print("Marks of Students = ", sub2)
 
 
# Visulizing Data using Matplotlib
plt.bar(sub1, sub2)
plt.ylim(0, 5)
plt.xlabel("Name of Students")
plt.ylabel("Marks of Students")
plt.title("Student's Information")
plt.show()