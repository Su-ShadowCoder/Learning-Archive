# Great idea. If it's been a while, don't jump into advanced topics. Spend 30–60 minutes refreshing the fundamentals with small exercises.

# Try to solve these without looking up the answers. If you get stuck after 10–15 minutes, ask for a hint.

# Exercise 1 — Variables and Printing

# Create variables:

# Your name
# Your age
# Your favorite programming language

# Print them in one sentence.

# name = "abdullah ibn isa"

# age = 32

# fav_pgm_lang = "Python"

# print(f"Hi, i am {name}, i am {age} year old.\nAnd my favorite programming language is {fav_pgm_lang}")


# Exercise 2 — User Input

# Ask the user:

# Name
# Age

# Print:
# Hello Abdullah! Next year you will be 25 years old.

# Make a code where it asks the user name and age, 
# then make it greet the user with name then make it say how old the user would be next year. 

# user_name = input(f"Please Enter your name:\n")
# user_age = int(input(f"Please enter your age:\n"))

# greeting_user = f"Hello {user_name}!"
# added_year = f"Next year you will be {user_age + 1} years old."

# print(f"{greeting_user} {added_year}")

# Exercise 3 — Simple Calculator

# Ask the user for two numbers.

# Print:

# Sum
# Difference
# Product
# Quotient

# Example:

# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0


# make the code ask for 2 inputs(int), and print from those two numbers the following parameters that is in accordance with the example here above. 

# a = int(input("Enter first number:\n"))
# b = int(input("Enter second number:\n"))

# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b

# print(f"""
# Addition: {addition}
# Subtraction: {subtraction}
# Multiplication: {multiplication}
# Division: {division}""")

# Exercise 4 — Even or Odd

# Ask for a number.

# Print either:

# The number is even.

# or

# The number is odd.

# ask user number in int 
# the use the user input to validate if you have a 1 over or not by using division. by making use of the modulo operator %.
# if the answer after comparing with the user number is zero, then print number is even else number is odd. 


# user_numb_inp = int(input("Please enter a number to validate if the number you have entered is an even or odd:\n"))

# if user_numb_inp % 2 == 0:
#     print(f"The number: {user_numb_inp} is even!")
# else:
#     print(f"The number: {user_numb_inp} is odd!")



# Exercise 5 — Positive, Negative, or Zero

# Ask for a number.

# Output:

# Positive

# or

# Negative

# or

# Zero

# 1 ask user int input. 2 assign positive for positive numbers. 3 assign negative for negative number, and zero is zero, print after the outcome

# user_numb_inp = int(input("Please enter a number:\n"))

# if user_numb_inp == 0:
#     print("Zero")
# elif user_numb_inp > 0:
#     print("Positive")
# else:
#     print("Negative")

# \\\\\\\\\\\\\\\\\\\\\\




















# \\\\\\\\\\\\\\\\\\\
Exercise 6 — Grade Checker

Ask for a score (0–100).

Print:

A (90+)
B (80–89)
C (70–79)
D (60–69)
F (<60)

Use only if, elif, and else.

Exercise 7 — Countdown

Using a while loop, print:

5
4
3
2
1
Lift off!
Exercise 8 — Multiplication Table

Ask the user for a number.

Print its multiplication table up to 10.

Example:

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

Use a for loop.

Exercise 9 — Guess the Secret Number

Set

secret = 8

Keep asking until the user guesses correctly.

Output:

Too high!
Too low!
Correct!

Concepts:

while
if
Exercise 10 — List Practice

Create:

fruits = ["apple", "banana", "orange", "grape"]

Do the following:

Print the first item.
Print the last item.
Add "mango".
Remove "banana".
Print every fruit using a loop.
Bonus Challenge — Mini ATM

Display:

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Start with:

balance = 1000

The user chooses an option and the balance updates accordingly. You can ignore invalid input for now.