import mysql.connector as mariadb
from returnData import *
#will find the table by showing the categories and people then calling them with
#the proper prefix before them in the cursor statement
def spendIncome():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()

	proceed = "n", "no"
	answer = "n"
	while answer in proceed:
		print("What category was the purchase out of the following?")
		returnCategory()
		print("\n")
		category = raw_input()
		print("What person was the purchase for out of the following?")
		returnPeople()
		print("\n")
		person = raw_input()
		print("How much? (xxx.xx format)")
		cost = raw_input()
		print("Is this correct? (y/n)")
		answer = raw_input()

	#send the cost to its corresponding tables. The person and category
	#are both independently keeping track while totalSpent is used 
	#to calculate and track all purchases.
	cursor.execute("INSERT INTO per_"+person+"(amount) VALUES("+cost+")")

	cursor.execute("INSERT INTO cat_"+category+"(amount) VALUES("+cost+")")

	cursor.execute("INSERT INTO tbl_totalSpent(amount) VALUES("+cost+")")
	#commit is needed to save these changes to the database.
	mariadb_connection.commit()
	print("\n")