import mysql.connector
myFirstdb = mysql.connector.connect(host="localhost",user="root",password="SYSTEM",database="cvr")
mycursor = myFirstdb.cursor()




sql = "INSERT INTO student (student_id, name,phone_no) VALUES (%s,%s,%s)"
val = (105,"ss",85888)


mycursor.execute(sql, val)
myFirstdb.commit()
print(f"{mycursor.rowcount} records inserted.")




mycursor.close()
mycursor.close()
