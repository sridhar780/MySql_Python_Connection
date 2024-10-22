import mysql.connector
myFirstdb = mysql.connector.connect(host="localhost",user="root",password="SYSTEM",database="sivasivanidc")
mycursor = myFirstdb.cursor()
mycursor.execute("CREATE TABLE student (htno int(10),name VARCHAR(20),address VARCHAR(255))")


