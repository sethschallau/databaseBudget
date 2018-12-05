import mysql.connector as mariadb
import re
def createTheDatabase():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49')
	cursor = mariadb_connection.cursor()
	#cursor.execute("CREATE DATABASE budget")
	cursor.execute("SHOW DATABASES")
	result = cursor.fetchall()
	
	for line in result:
		print(line[0])

	
	print("database created")
