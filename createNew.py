import mysql.connector as mariadb

def createTheDatabase():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49')
	cursor = mariadb_connection.cursor()
	cursor.execute("CREATE DATABASE IF NOT EXISTS budget")
	cursor.execute("SHOW DATABASES")
	result = cursor.fetchall()
	
	for line in result:
		if line[0] == "budget":
			print(line[0] + " database created")


def createTables():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	#to find money, use spending money table - total spent
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_spending(amount FLOAT null)")
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_totalSpent(amount FLOAT null)")
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_saving(amount FLOAT null)")

	cursor.execute("SHOW TABLES")
	result = cursor.fetchall()
	
	for line in result:
		print(line[0] + " table created")

#creates table for category
def createCategoryTable(catName):
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS cat_"+catName+"(amount FLOAT null)")

#creates a table for an individual to hold their spending
def createPersonTable(perName):
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS per_"+perName+"(amount FLOAT null)")