"""
Building an arithmetic calculator
Placing error handling and formating input fields line of code

"""
""" Enter two numbers for input """
var_1 = int(input("Enter 1st Number: "))
var_2 = int(input("Enter 2nd Number: "))

""" Enter the operator """
# take input from the user
add, subtract, multiply, divide = 1, 2, 3, 4
print("Add(1) ........... [+]")
print("Subtract(2) ...... [-]")
print("Multiply(3) ...... [*]")
print("Divide(4) ........ [/]")
print("Do not add the angle brackets [ ]")
print("-------------")
print("Enter your choice below: ")
print("-------------")

opr_choice = int(input("Enter choice: "))	
# Perform calculations on the values provided
# Execute the calculation for each function
# add, subtract, multiply, divide
def calculate(my_input, var_one, var_two):
	if my_input == add:
		print("ADDITION result", var_one + var_two)
		
	if my_input == subtract:
		print("SUBTRACTION result", var_one - var_two)
		
	if my_input == multiply:
		print("MULTIPLICATION result", var_one * var_two)
		
	if my_input == divide:
# 	Catch exceptions before performing calculation
#   Exit program if value has 0 on either variable 
		if var_1 == 0 or var_2 == 0:
			"Please enter a value greater or less 0"
			exit()
			
		print("DIVISION result", var_one / var_two)
		
# Execute calculate function
# Use variables provided (var_1 and var_2)

calculate(opr_choice, var_1, var_2)


