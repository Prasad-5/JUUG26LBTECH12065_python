#Assignment task unit 1
#Name : A Lakshmi prasad
#USN : 
#Course : Python programming
#Branch : AIDE – A
#Date : 31/07/2026

#Task 1 Print your
 #● Name
  #● Department
  #● College  
print("A.Lakshmi prasad")   
print("cse,AIDE")   
print("Jain university") 
 


#Task 2 Print the following pattern. 
'''******* 
*******
 *******'''
for i in range(3):
    print("*******")
 
#Task 3 Print the following using a single print() statement.
 '''Python is Easy'''
print("Python is Easy")

 
#Task 4 
'''Print 
1
 12
 123
 1234
 12345'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

 
#Task 5 
'''Use \n to print 
Computer 
Science 
Engineering'''
print("Computer\nScience\nEngineering")
 
#Task 6 
'''Use \t to print 
Name    Age    City'''
print("Name\tAge\tCity")
 
#Task 7 Write a Python program with a single-line comment explaining the purpose of the program.
print("Welcome to Python programming")
 
#Task 8 Write a Python program using multi-line comments.
"""
This is a multi-line comment.
This program demonstrates how multi-line comments
are written in Python using triple quotes.
"""
print("This program uses multi-line comments")

 
#Task 9
''' Write a program that contains
 ● Three comments  
● Three print statements'''
# Comment 1: This program displays basic information
# Comment 2: It uses three separate print statements
# Comment 3: Each print statement outputs a different line
print("Line 1: Hello")
print("Line 2: Welcome")
print("Line 3: Have a nice day")
 
#Task 10 
'''Create a variable called name. Store your name and print it.'''
name = "A. lakshmi prasad"   # Fill in your name
print(name)
 
#Task 11
''' Store 
10
 20
 30
 in three different variables and print them.'''


a = 10
b = 20
c = 30
print(a)
print(b)
print(c)
 
#Task 12 
'''Create a program that converts the string "100" into an integer and displays its value and data type.'''
num_str = "100"
num_int = int(num_str)
print("Value:", num_int)
print("Data type:", type(num_int))
 

#Task 13
''' Convert the integer 25 into a float and display the result and its type.'''
num_int2 = 25
num_float = float(num_int2)
print("Value:", num_float)
print("Data type:", type(num_float))
 
#Task 14 Accept the user's age using input(), convert it to an integer, and display the age.
age = int(input("Enter your age: "))
print("Your age is:", age)
 
#Task 15 Accept two numbers from the user, convert them to integers, and display their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum:", total)
 
#Task 16
'''(Using f-string) Accept a student's name, age and CGPA and display: My name is Rahul. I am 20 years old and my CGPA is 8.5.'''
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_cgpa = float(input("Enter your CGPA: "))
print(f"My name is {student_name}. I am {student_age} years old and my CGPA is {student_cgpa}.") 

#Task 17 
'''Accept temperature in Celsius and convert it into Fahrenheit. Formula: F = (C × 9/5) + 32 Display the result using an f-string with two decimal places.'''
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
 
#Task 18
''' Accept an integer and determine whether it is even or odd using the % operator. Example: Enter number: 25 Output: 25 is Odd'''
number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
 









