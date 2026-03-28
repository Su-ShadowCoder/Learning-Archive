# Basic Python Practice (10 Exercises)


# ------------------------------------------------------------------------
# 1. Hello program

# Write a program that prints:

# Hello world
# ------------------------------------------------------------------------

# print("Hello, World!")


# ------------------------------------------------------------------------
# 2. Ask the user's name

# Ask the user for their name and print:

# Hello Abdullah

# Use an f-string.
# ------------------------------------------------------------------------

# get_username = input(f"What's your name?\n")
# print(f"Hello, {get_username}.")

# ------------------------------------------------------------------------
# 3. Age question

# Ask the user for their age and print:

# You are 25 years old
# ------------------------------------------------------------------------


# get_user_age = int(input(f"What is your age?\n"))
# print(f"You are {get_user_age} years old.")

# ------------------------------------------------------------------------
# 4. Simple calculator

# Ask the user for two numbers and print their sum.

# Example:

# Enter number 1: 5
# Enter number 2: 7
# Result: 12

# Hint: int()
# ------------------------------------------------------------------------


# x = int(input("What's x?\n"))
# y = int(input("What's y?\n"))

# z = x + y 

# print(f"The sum of x and y = {z}.")

# ------------------------------------------------------------------------
# 5. Even or odd

# Ask the user for a number and print:

# This number is even

# or

# This number is odd

# Hint: %
# ------------------------------------------------------------------------


# usr_inp = int(input("Please enter a number to verify\nwhether the number is odd or even:\n"))

# if usr_inp % 2 == 0:
#     print(f"The number you have entered is an Even number!")
# else:
#     print("The number you have entered is a Odd number!")


# ------------------------------------------------------------------------
# 6. Password check

# Create a variable:

# password = "python123"

# Ask the user for a password.

# If correct → print:

# Access granted

# Else:

# Access denied
# ------------------------------------------------------------------------

# password check
# ask for password
# if correct print: Access granted, else access denied. 

# usr_atn = input("Authentication check; Please enter the password:\n")

# if usr_atn == "python123":
#     print("Access granted")
# else:
#     print("Access denied")


# ------------------------------------------------------------------------
# 7. Temperature check

# Ask the user for a temperature.

# Print:

# Cold

# if below 10

# Warm

# if between 10 and 25

# Hot

# if above 25
# ------------------------------------------------------------------------

# usr_temp = int(input("Please enter the temperature\n"))

# if usr_temp < 10:
#     print("Cold")
# elif 10 <= usr_temp <= 25:
#     print("Warm")
# else:
#     print("Hot")


# ------------------------------------------------------------------------
# 8. Counting loop

# Write a loop that prints numbers from 1 to 10.

# Output:

# 1
# 2
# 3
# ...
# 10
# ------------------------------------------------------------------------

# for element in range(1, 11):
#     print(element)


# ------------------------------------------------------------------------
# 9. Multiplication table

# Ask the user for a number and print the multiplication table from 1 to 10.

# Example for 3:

# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30
# ------------------------------------------------------------------------

# tables

# ask for user number to multiply
# looping trough 1 to 10 
# every loop should multiply what the user has entered, the proces should be multiplicated so it  prints out as a table. 


# usr_numb = int(input("Please enter a number to print a multiplication table:\n"))

# for element in range(1, 11):
#     answer = element * usr_numb
#     print(f"{usr_numb} x {element} = {answer}")


# ------------------------------------------------------------------------
# 10. Guess the number

# Create a variable:

# secret = 7

# Ask the user to guess the number.

# If correct:

# Correct!

# If wrong:

# Try again
# ------------------------------------------------------------------------

# secret = 7

# while True:
#     usr_gss = int(input("Please enter a number to guess the correct number:\n"))
#     if usr_gss == secret:
#         print("Correct!")
#         break
#     else:
#         print("Try again")

# ///////////////////////////////////////////////////////



# Level 2 Python Practice (10 Exercises)


# ------------------------------------------------------------------------
# 1. Count even numbers in a list

# Given:
# numbers = [1, 2, 3, 4, 5, 6]

# Count how many numbers are even and print the result.

# ------------------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6]

# # so go trough the collection and iterate trough it whether that element is a even, and if that element is then count it. and print the total even numbers. 
# even_count = 0
# # go trough the collection
# for element in numbers:
#     # check if element is even
#     if element % 2 == 0:
#         even_count += 1
# print(even_count)
# add element to a new collection
# be aware of the even-collection whether in or out of the nest most likely out of it. soit updates troughout every iteration of the numbers collection.
# print the result which is the even-collection. 


# ------------------------------------------------------------------------
# 2. Sum of a list

# Given:
# numbers = [10, 20, 30, 40]

# Calculate the total sum manually (do NOT use sum()) and print it.

# ------------------------------------------------------------------------

# numbers = [10, 20, 30, 40]

# sum_lst = 0

# for element in numbers:
#     sum_lst += element

# print(sum_lst)


# ------------------------------------------------------------------------
# 3. Find the largest number

# Given:
# numbers = [3, 7, 2, 9, 5]

# Find and print the largest number.

# ------------------------------------------------------------------------

# numbers = [3, 7, 2, 9, 5]
# temp = numbers[0]
# for element in numbers:
#     if element > temp:
#         temp = element
# print(temp)

# ------------------------------------------------------------------------
# 4. Count occurrences

# Given:
# numbers = [1, 2, 2, 3, 2, 4]

# Ask the user for a number and count how many times it appears in the list.

# ------------------------------------------------------------------------

# usr_numb = int(input("Enter a number:\n"))

# numbers = [1, 2, 2, 3, 2, 4]

# count = 0

# for element in numbers:
#     if usr_numb == element:
#         count += 1

# print(count)

# ------------------------------------------------------------------------
# 5. Reverse a string (manual)

# Given:
# text = "python"

# Reverse the string WITHOUT using slicing (no [::-1]) and print it.

# ------------------------------------------------------------------------

# text = "python"
# revs = ""

# for element in text:
#     revs = element + revs
# print(revs)


# ------------------------------------------------------------------------
# 6. Password attempts (limit)

# Password is:
# password = "python123"

# Ask the user to enter the password.
# The user gets ONLY 3 attempts.

# If correct:
# Access granted

# If all 3 fail:
# Access blocked

# ------------------------------------------------------------------------
# password = "python123"

# count = 0

# while count != 3:
#     usr_pswrd = input("Please enter the password:\n")
#     if usr_pswrd == password:
#         print("Access granted")
#         break
#     else:
#         count += 1
#         if count == 3:
#             print("Access blocked")
# ------------------------------------------------------------------------
# 7. Number range filter

# Given:
# numbers = [5, 12, 17, 3, 9, 21]

# Print only the numbers between 10 and 20.

# ------------------------------------------------------------------------

# numbers = [5, 12, 17, 3, 9, 21]

# for element in numbers:
#     if 10 <= element <= 20:
#         print(element)


# ------------------------------------------------------------------------
# 8. Simple log checker

# Given:
# logs = ["INFO", "ERROR", "WARNING", "ERROR", "INFO"]

# Count how many times "ERROR" appears and print the result.

# ------------------------------------------------------------------------

# logs = ["INFO", "ERROR", "WARNING", "ERROR", "INFO"]
# count = 0
# for l_msg in logs:
#     if l_msg == "ERROR":
#         count += 1
# print(f"{count} \"ERROR\" messages has appeared in the logs!")

# ------------------------------------------------------------------------
# 9. Multiplication table (nested loop)

# Print a multiplication table from 1 to 5.

# Example:
# 1 x 1 = 1
# ...
# 5 x 5 = 25

# ------------------------------------------------------------------------

# for n_range in range(1, 6):
#     for table_n in range(1, 6):
#         if n_range == table_n:
#             x = n_range * table_n
#             print(f"{n_range} x {table_n} = {x}.")


# ------------------------------------------------------------------------
# 10. Guess the number (with hints)

# secret = 7

# Ask the user to guess the number.

# If the guess is too high:
# print "Too high"

# If too low:
# print "Too low"

# If correct:
# print "Correct!"

# ------------------------------------------------------------------------

# secret = 7

# usr =  int(input("Guess the number, please enter a number:\n"))

# while True:
#     if usr == secret:
#         print("Correct!")
#         break
#     elif usr < secret:
#         print("Too low")
#     else:
#         print("Too high")
# ------------------------------------------------------------------------




# /////////////////////////////////////////
# Small Challenge:
# /////////////////////////////////////////

# 6. Password attempts (limit)

# Password is:
# password = "python123"

# Ask the user to enter the password.
# The user gets ONLY 3 attempts.

# If correct:
# Access granted

# If all 3 fail:
# Access blocked


# Requirements
# Your program must:

# Start in ACTIVE

# Count attempts

# On correct password → switch to AUTHENTICATED

# On 3 failures → switch to LOCKED

# Stop execution when not ACTIVE

# //////////////////////////////////////////////////////////


# def password_authentication(password, attempt_numb):
    
#     active = "ACTIVE"
#     locked = "LOCKED"
#     authenticated = "AUTHENTICATED"

#     attempt_count = 0
#     current_state = active
    
#     while current_state == active:
#         print(f"Attempt counter: {attempt_count}")
#         print(f"Status: {current_state}")
#         usr = input(f"Authentication Query;\nPlease enter the password for authorization:\n")
#         if usr == password:
#             current_state = authenticated
#             print(authenticated)
#         else:
#             attempt_count += 1

#             if attempt_count == attempt_numb:
#                 current_state = locked
#                 print(current_state)
#             else:
#                 print("Try again!")
    
#     return current_state


# password_authentication("python123", 3)
# ////////////////////////////////////////////////

