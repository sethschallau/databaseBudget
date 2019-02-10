from createNew import *
from returnData import *
from addFunds import *
from calculations import *
from spendIncome import *
from spendIncome import *
from whoWhatHowmuchMenu import subMenu
import os
import mysql.connector as mariadb

#loop for the menu
done = 0
while done == 0:
	print("1) Setup\n2) Add People\n3) Add Categories\n4) Spend Money\n5) Earn Money\n6) Who, What, How Much?\n7) Exit")
	inputChoice = raw_input()
	#setup calls
	if inputChoice == "1":
		os.system('clear')
		createTheDatabase()
		createTables()
		print("Setup Complete")
	#calls the function to create a new table for people
	elif inputChoice == "2":
		os.system('clear')
		#we want a funciton that returns all persons
		print("Enter the name of a new person: ")
		person = raw_input()
		createPersonTable(person)

	elif inputChoice == "3":
		os.system('clear')
		#we want a funciton that returns all persons
		print("Enter the name of a new category: ")
		person = raw_input()
		createCategoryTable(person)

	elif inputChoice == "4":
		os.system('clear')
		spendIncome()

	elif inputChoice == "5":
		os.system('clear')
		addFunds()

	elif inputChoice == "6":
		os.system('clear')
		subMenu()
	elif inputChoice == "7":
		os.system('clear')
		done = 1