import mysql.connector as mariadb

def addFunds():
	mariadb_connection = mariadb.connect(user='budget', password='schallau49', database='budget')
	cursor = mariadb_connection.cursor()
	#grab the data from 
	proceed = "n", "no"
	answer = "n"
	while answer in proceed:
		print("Amount Earned?")
		paycheck = raw_input()
		flt_paycheck = float(paycheck)
		print("Percentage to save? (.XX format)")
		percentage = float(raw_input())
		print("Is this correct? (y/n)")
		answer = raw_input()

	#make the calculations to determine what goes into savings and spending
	intoSpending = flt_paycheck * percentage
	intoSpending = round(intoSpending,2)
	intoSavings = flt_paycheck - intoSpending
	#turn the numbers back into strings so they are compatible with the cursor execution
	intoSpending = str(intoSpending)
	intoSavings = str(intoSavings)
	#add the data into the corresponding tables
	cursor.execute("INSERT INTO tbl_spending(amount) VALUES("+intoSpending+")")
	cursor.execute("INSERT INTO tbl_saving(amount) VALUES("+intoSavings+")")
	#commit is needed to save these changes to the database.
	mariadb_connection.commit()
	print("\n")
