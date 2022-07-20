import mysql.connector
# import MySQLConnetion, Error
# from python_mysql_dbconfig import  read_db_config


mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="sql_store")
mycursor = mydb.cursor()
mycursor.execute("SELECT first_name from customers")
result = mycursor.fetchall()
for i in result:
    print(i)


