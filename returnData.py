import mysql.connector as mariadb

def returnPeople():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	#return all people
	cursor.execute("SHOW TABLES LIKE 'per_%'")
	result = cursor.fetchall()
	print("Existing People: ")
	for line in result:
		print(line[0][4:] + " "),

def returnCategory():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	#return all people
	cursor.execute("SHOW TABLES LIKE 'cat_%'")
	result = cursor.fetchall()
	print("Existing Category: ")
	for line in result:
		print(line[0][4:] + " "),