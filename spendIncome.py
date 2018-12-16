import mysql.connector as mariadb
from returnData import *
#will find the table by showing the categories and people then calling them with
#the proper prefix before them in the cursor statement
def spendIncome():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	while choice != "n" || choice != "no":
		print("What category was the purchase out of the following?")
		returnCategory()
		category = raw_input()
		print("What person was the purchase for out of the following?")
		returnPeople()
		person = raw_input()
		print("How much? (xxx.xx format)")
		amount = float(raw_input())
		print("Is this correct?")
		choice = raw_input()

