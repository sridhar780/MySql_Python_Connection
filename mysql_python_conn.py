#No module named mysql.connector
#C:\Program Files\Python312\Scripts (cmd type in url)
#pip install mysql-connector-python
import mysql.connector
myFirstdb = mysql.connector.connect(host="localhost",user="root",password="SYSTEM")
print(myFirstdb)


mycursor = myFirstdb.cursor()

##mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("CREATE DATABASE sivasivanidc")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

