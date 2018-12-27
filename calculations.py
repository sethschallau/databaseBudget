import mysql.connector as mariadb

def calcTotalSpent():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM tbl_totalSpent")
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
		print(float(line[0]))
		totalSpent = totalSpent + float(line[0])
	return totalSpent

def calcPerson(name):
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM per_"+name)
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
		print(float(line[0]))
		totalSpent = totalSpent + float(line[0])
	return totalSpent

def calcCategory(name):
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM cat_"+name)
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
		print(float(line[0]))
		totalSpent = totalSpent + float(line[0])
	return totalSpent

def calcRemain():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM tbl_totalSpent")
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
		totalSpent = totalSpent + float(line[0])

	cursor.execute("SELECT amount FROM tbl_spending")
	result = cursor.fetchall()
	spending = 0.0
	for line in result:
		spending = spending + float(line[0])

	return (spending - totalSpent)

#print(calcCategory("gas"))
#print(calcTotalSpent())
#print(calcPerson("percy"))
#print(calcRemain())