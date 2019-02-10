from calculations import *
from returnData import *
import os
def subMenu():

	done = 0
	while done == 0:
		print("\n1) Enter Person\n2) Enter Category\n3) Total Spent\n4) Spending Money\n5) In Savings\n6) Exit")
		inputChoice = raw_input()

		if inputChoice == "1":
			os.system('clear')
			returnPeople()
			print("\nEnter the name of the person: ")
			person = raw_input()
			costOf = calcPerson(person)
			total = calcTotalSpent()
			percen = int(costOf/total * 100)
			print("\n" + str(person) + " has used $" + str(costOf) +
				" and accounts for " + str(percen) + "% of all money spent")


		elif inputChoice == "2":
			os.system('clear')
			returnCategory()
			print("\nEnter the name of the category: ")
			category = raw_input()
			costOf = calcCategory(category)
			total = calcTotalSpent()
			percen = int(costOf/total * 100)
			print('\n')
			print("\n" + str(person) + " cost $" + str(costOf) +
				" and accounts for " + str(percen) + "% of all money spent")

		elif inputChoice == "3":
			os.system('clear')
			print(calcTotalSpent())

		elif inputChoice == "4":
			os.system('clear')
			print(calcRemain())

		elif inputChoice == "5":
			os.system('clear')
			print(calcSavings())

		elif inputChoice == "6":
			os.system('clear')
			done = 1