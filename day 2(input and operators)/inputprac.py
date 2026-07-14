#1 Ask the user for their favorite color.
# Print a message back to them saying "Your favorite color is [color]!"

color = input("enter your favorite color: ")
print("your favourite color is:" ,color) 

#enter your favorite color: pavan 
# your favourite color is: pavan

#2 Problem: Run the code below, type the number 25, and look closely at the output.
# Why is the type not an integer?

age = input("Enter your age: ")
print(type(age)) #output: Enter your age: 20 <class 'str'>

#soln because in python the intrepreter thinks it as a str,
# we have to explicitly give int(input()), float(input()) bool(input())
#to covert that into the int type is below

age = int(input("Enter your age: "))
print(type(age)) #now this will be int type #output: Enter your age: 19 <class 'int'>

#3 Problem: Ask the user for their birth year. 
# Convert it to an integer, subtract it from the current year (2026), and print their current age.

birth_year = int(input("enter your birth year: "))
current_age = 2026-birth_year
print("your age is: ",current_age) #output: enter your birth year: 2006 your age is:  20

#4 Problem: Ask the user to input the price of a meal. 
# Calculate a 15% tip and print the result.

price = float(input("enter your meal price: "))
tip = price * 0.15
print(f"your meal price is {price}$ with a tip of {tip}$") #output: enter your meal price: 190 your meal price is 190.0$ with a tip of 28.5$

#5 Problem: The following code crashes when a user runs it. 
# Why does it crash, and how do you fix it?

tickets = input("How many tickets do you want? ")
total_cost = tickets * 10
print(total_cost) #output: How many tickets do you want? 10 10101010101010101010

#soln here we are printing the string values that's why when even we print the output.
#we get that number multiply with 10 ex (input is 9 means output will be 999999999).
#to eradicate this the inputs are taking the str no, add int before input that's it
#corrected code is this

tickets = int(input("How many tickets do you want? "))
total_cost = tickets * 10
print(total_cost) #output: How many tickets do you want? 8 80
