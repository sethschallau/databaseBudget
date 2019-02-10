import mysql.connector as mariadb

def calcTotalSpent():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM tbl_totalSpent")
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
		totalSpent = totalSpent + float(line[0])
	return totalSpent

#returns the data from tbl_saving
def calcSavings():
	#create a new conncetion to the user budget and use the budget database
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	#execute sql statement that takes returned data from the table and puts it in an array
	cursor.execute("SELECT amount FROM tbl_saving")
	result = cursor.fetchall()
	totalSaving = 0.0
	for line in result:
		totalSaving = totalSaving + float(line[0])
	return totalSaving

#person and category can be merged into one method using a second parameter to 
#decide which table type is searched, but there isn't really any benefit to that modularity
#except for about 10 less lines typed, a few bytes of data.
def calcPerson(name):
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM per_"+name)
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
		#print(float(line[0]))
		totalSpent = totalSpent + float(line[0])
	return totalSpent

def calcCategory(name):
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	cursor.execute("SELECT amount FROM cat_"+name)
	result = cursor.fetchall()
	totalSpent = 0.0
	for line in result:
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