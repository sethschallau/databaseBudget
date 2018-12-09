from createNew import *
import mysql.connector as mariadb
import re

#loop for the menu
done = 0
while done == 0:
	print("1) Setup\n2) Add People\n3) Add Categories\n4) Spend Money\n5) Earn Money\n6) Exit")
	inputChoice = raw_input()
	#setup calls
	if inputChoice == "1":
		print("\n\n\n")
		createTheDatabase()
		createTables()
		print("Setup Complete\n\n\n")
	#exit
	elif inputChoice == "6":
		done = 1