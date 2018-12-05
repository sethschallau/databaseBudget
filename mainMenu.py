from createNew import createTheDatabase
import mysql.connector as mariadb
import re

print("1) Create a new Database ")

inputChoice = raw_input()
if inputChoice == "1":
	createTheDatabase()