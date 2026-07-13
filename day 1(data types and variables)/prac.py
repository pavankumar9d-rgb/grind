#1 swapping of two numbers without using temp variable
#a value inserting before swapping

a = 123
print("a value is",a)

#b value inserting before swapping

b = 90
print("b value is",b)

#a,b=b,a exchanges the values from each other without using temp we can do this 😏😏

a,b = b,a
print("after swapping a is:",a) #a is swapped by the previous line of code
print("after swapping b is:",b) #b is swapped by that exchaning line of code

#2 type of data types in python
print(type(5.0)) #float

print(type("5")) #str because "" is used

#3 
x = "10"
y = "20"
print(x+y) #1020 because these are not the int these are str

#4 Task: Create three variables to store a person's first name, age, and hourly wage.
# Print out a complete profile summary in one line using an f-string.

first_name = "pavan"
age = 20
hr_wage = '200$'
print(f"user : {age},name : {first_name},hour wage : {hr_wage}/hr")
print(f"He's name is {first_name} and his age is {age} with an hourly salary of {hr_wage}/hr") #He's name is pavan and his age is 20 with an hourly salary of 200$/hr


#5 Task: Initialize a = 5 and b = 10. Swap their values so that a becomes 10 and b becomes 5.
# Bonus points if you do it in a single line without creating a third variable.

q = 5
w = 10
q,w = w,q
print("q and w values are :", q,w)

#6 Task: Ask the user for their birth year using the input() function. 
# Subtract that year from the current year to display their exact age.
# (Hint: Watch out for data type mismatches with input text!)

your_year = input("enter your birth year :")
c_age = 2026 - int(your_year)
print("age is :",c_age)

#7 Task: Store the phrase "Python Programming" inside a variable. 
# Use built-in functions to find its overall character length and convert the entire phrase to lowercase

g = "Python Programming"
print("the length of the text in g is : ",len(g))
print("in uppercase of text is", g.upper()) #makes upper of whole str
print("in lowercase of text is", g.lower()) #makes lower of whole str
