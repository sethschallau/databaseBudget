import mysql.connector as mariadb
import re
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
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_spending(amount DOUBLE null)")
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_saving(amount DOUBLE null)")
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_people(names TEXT null)")
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_category(type TEXT null)")
	cursor.execute("CREATE TABLE IF NOT EXISTS tbl_total(amount DOUBLE null)")

	cursor.execute("SHOW TABLES")
	result = cursor.fetchall()
	
	for line in result:
		print(line[0] + " table created")