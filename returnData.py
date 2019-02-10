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
	#return all categories.
	#execute the sql to show tables with the naming convention of category
	cursor.execute("SHOW TABLES LIKE 'cat_%'")
	#grabs all of the data returned and puts it into variable array result
	result = cursor.fetchall()
	print("Existing Category: ")
	#goes through the array
	for line in result:
		#prints first index of the array and from the 4th indexed character of the string until the end of the string
		print(line[0][4:] + " "),