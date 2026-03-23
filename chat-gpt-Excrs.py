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
# ///////////////////////////////////////////////////////////////////////


# ==========================================
# DICTIONARY PRACTICE — Beginner → Intermediate
# ==========================================

# ------------------------------------------
# EXERCISE 1 — Create and read values
# ------------------------------------------
def main():
    user = {
        "name": "abdullah",
        "age": 20
    }

    print(user["name"])
    print(user["age"])

if __name__ == "__main__":
    main()

# TASK:
# - Add "city"
# - Print "city"


# ------------------------------------------
# EXERCISE 2 — Add new key
# ------------------------------------------
def main():
    user = {
        "name": "abdullah"
    }

    user["age"] = 20

    print(user)

if __name__ == "__main__":
    main()

# TASK:
# - Add "country"
# - Print only "country"


# ------------------------------------------
# EXERCISE 3 — Update value
# ------------------------------------------
def main():
    user = {
        "name": "abdullah",
        "age": 20
    }

    user["age"] = 21

    print(user)

if __name__ == "__main__":
    main()

# TASK:
# - Change "name" instead of "age"


# ------------------------------------------
# EXERCISE 4 — Check if key exists
# ------------------------------------------
def main():
    user = {
        "name": "abdullah",
        "age": 20
    }

    key = input("Enter key: ")

    if key in user:
        print("Found:", user[key])
    else:
        print("Not found")

if __name__ == "__main__":
    main()

# TASK:
# - Test: name, age, city


# ------------------------------------------
# EXERCISE 5 — Default value logic
# ------------------------------------------
def main():
    user = {
        "name": "abdullah"
    }

    key = input("Enter key: ")

    if key in user:
        print(user[key])
    else:
        print("Default: unknown")

if __name__ == "__main__":
    main()

# TASK:
# - Add more keys
# - Try missing keys


# ------------------------------------------
# EXERCISE 6 — Counting values
# ------------------------------------------
def main():
    logs = {
        "INFO": 3,
        "ERROR": 1,
        "WARNING": 2
    }

    logs["ERROR"] += 1

    print(logs)

if __name__ == "__main__":
    main()

# TASK:
# - Increase "INFO" twice
# - Print only "ERROR"


# ------------------------------------------
# EXERCISE 7 — Simple login system
# ------------------------------------------
def main():
    users = {
        "abdullah": "python123",
        "alice": "abc123"
    }

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    main()

# TASK:
# - Add a new user
# - Test correct and incorrect login


# ------------------------------------------
# EXERCISE 8 — Attempt counter per user
# ------------------------------------------
def main():
    users = {
        "abdullah": "python123",
        "alice": "abc123"
    }

    attempts = {
        "abdullah": 0,
        "alice": 0
    }

    username = input("Username: ")

    if username in users:
        attempts[username] += 1
        print("Attempts:", attempts[username])

if __name__ == "__main__":
    main()

# TASK:
# - Run multiple times
# - Observe attempt counter increase per user


# ///////////////////////////////////////////////////////////////////////
# ================================
# DICTIONARY PRACTICE (WITH main())
# ================================


# --------------------------------
# EXERCISE 1 — Basic dictionary in main
# --------------------------------
def main():
    user = {
        "name": "abdullah",
        "age": 20
    }

    print(user["name"])
    print(user["age"])

if __name__ == "__main__":
    main()

# TASK:
# - Add a new key: "country"
# - Print it inside main()


# --------------------------------
# EXERCISE 2 — User lookup
# --------------------------------
def main():
    users = {
        "abdullah": "python123",
        "alice": "abc123"
    }

    username = input("Enter username: ")

    if username in users:
        print("User exists")
    else:
        print("User not found")

if __name__ == "__main__":
    main()

# TASK:
# - Try different usernames
# - Add a third user to the dictionary


# --------------------------------
# EXERCISE 3 — Get value from dictionary
# --------------------------------
def main():
    users = {
        "abdullah": "python123",
        "alice": "abc123"
    }

    username = input("Enter username: ")

    if username in users:
        print("Password is:", users[username])
    else:
        print("User not found")

if __name__ == "__main__":
    main()

# TASK:
# - Add more users
# - Try valid and invalid usernames


# --------------------------------
# EXERCISE 4 — Update dictionary value
# --------------------------------
def main():
    users = {
        "abdullah": "python123",
        "alice": "abc123"
    }

    users["alice"] = "newpass999"

    print(users)

if __name__ == "__main__":
    main()

# TASK:
# - Change abdullah's password instead
# - Print only abdullah’s password


# --------------------------------
# EXERCISE 5 — Simple attempt counter per user
# --------------------------------
def main():
    users = {
        "abdullah": "python123",
        "alice": "abc123"
    }

    attempts = {
        "abdullah": 0,
        "alice": 0
    }

    username = input("Enter username: ")

    if username in users:
        print("User found")

        attempts[username] += 1
        print("Attempts:", attempts[username])
    else:
        print("User not found")

if __name__ == "__main__":
    main()

# TASK:
# - Run multiple times and watch attempt count increase
# - Add a new user and extend both dictionaries


# ////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////
# ================================
# MAIN() SIMPLE PRACTICE EXERCISES
# ================================

# --------------------------------
# EXERCISE 1 — Basic main()
# --------------------------------
def main():
    print("Hello from main")

if __name__ == "__main__":
    main()

# TASK:
# - Run it
# - Then comment out the last two lines
#   and observe that nothing runs


# --------------------------------
# EXERCISE 2 — Input inside main()
# --------------------------------
def main():
    name = input("Enter your name: ")
    print("Hello", name)

if __name__ == "__main__":
    main()

# TASK:
# - Move input() outside main() (try it)
# - Observe why structure breaks


# --------------------------------
# EXERCISE 3 — Multiple prints
# --------------------------------
def main():
    print("Step 1")
    print("Step 2")
    print("Step 3")

if __name__ == "__main__":
    main()

# TASK:
# - Add a 4th print line
# - Then remove main() call and observe nothing executes


# --------------------------------
# EXERCISE 4 — Direct call vs main()
# --------------------------------
def main():
    print("This is main")

main()

# TASK:
# - Compare this with previous examples
# - Think: what is missing here conceptually?


# --------------------------------
# EXERCISE 5 — Import behavior test
# --------------------------------

# file1.py
def main():
    print("Running file1")

if __name__ == "__main__":
    main()


# file2.py
import file1
print("file2 running")

# TASK:
# - Run file2.py
# - Observe:
#   main() in file1 does NOT run automatically

# ////////////////////////////////////////////////////////////////////




# ///////////////////////////////////////////////////////////////////////

# ================================
# Exercise: Multi-User Login System
# ================================

# You must build a login system with:
# - multiple users
# - per-user password checking
# - per-user attempt tracking
# - account lock after 3 failed attempts


# -------------------------------
# 1. User database (DO NOT CHANGE)
# -------------------------------
users = {
    "abdullah": "python123",
    "alice": "abc123",
    "bob": "secure999"
}


# -------------------------------
# 2. Attempt tracking (YOU USE THIS)
# -------------------------------
attempts = {
    "abdullah": 0,
    "alice": 0,
    "bob": 0
}


# -------------------------------
# 3. Your task:
# -------------------------------
# Build a login system that:

# A) Asks for a username
# B) If username not found:
#    - print "User not found"
#    - ask again

# C) If username exists:
#    - ask for password

# D) If password is correct:
#    - print "Access granted"
#    - stop program

# E) If password is wrong:
#    - increase that user's attempt counter by 1
#    - print remaining attempts

# F) If a user reaches 3 failed attempts:
#    - print "Account locked"
#    - that user cannot log in anymore


# -------------------------------
# 4. Extra challenge (optional)
# -------------------------------
# Create a "locked_users" list or dict
# and prevent locked users from trying again


# -------------------------------
# 5. Rules
# -------------------------------
# - You MUST use loops
# - You MUST use dictionaries
# - You MUST track attempts per user
# - Do NOT use global single attempt counter
# - Each user has independent login state

# ////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////

# ==========================================
# EXERCISE — LOGIN SYSTEM (BUILD FROM SCRATCH)
# ==========================================

# REQUIREMENTS:

# 1. Create a dictionary called "users"
#    - Add at least 3 usernames with passwords

# 2. Create a dictionary called "attempts"
#    - Each user starts with 0 attempts

# 3. Ask the user for a username

# 4. If the username does NOT exist:
#    - print "User not found"
#    - stop program

# 5. If the username exists:
#    - allow the user to enter password multiple times

# 6. Rules for password checking:
#    - if password is correct:
#        -> print "AUTHENTICATED"
#        -> stop program
#    - if password is wrong:
#        -> increase attempt count for that user
#        -> print remaining attempts

# 7. Lockout rule:
#    - if attempts reach 3:
#        -> print "LOCKED OUT"
#        -> stop program

# 8. Use a loop (while or for) to control attempts

# 9. (Optional challenge)
#    - Print attempt history after each try


def main():
    # WRITE YOUR CODE HERE
    pass


if __name__ == "__main__":
    main()

# ////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////
# ==========================================
# EXERCISE — DICTIONARY DESIGN (NO TEMPLATE GIVEN)
# ==========================================

# RULE:
# You must decide the structure of the dictionaries yourself.

# GOAL:
# Build a small system using ONLY dictionaries, input, conditions, and loops.

# ==========================================
# REQUIREMENTS
# ==========================================

# 1. Create a dictionary that stores USERS
#    - You choose the structure
#    - Must include at least 3 users
#    - Each user must have at least ONE piece of data (you decide what)

# 2. Create a SECOND dictionary that tracks something per user
#    Examples (pick ONE idea only):
#    - login attempts
#    - number of actions
#    - score
#    - warnings
#    - activity count

# 3. Ask the user for a key (username or identifier)

# 4. If the key does NOT exist:
#    - print a message
#    - stop program

# 5. If the key exists:
#    - enter a loop

# 6. Inside the loop:
#    - ask for input (you decide what kind of input)
#    - update the second dictionary based on that input
#    - print current state after each update

# 7. Add a STOP condition:
#    - user can exit manually OR
#    - system stops after a limit you define

# 8. You MUST use:
#    - dictionary lookup
#    - dictionary update
#    - at least one loop
#    - at least one condition

# ==========================================
# OPTIONAL CHALLENGE (HIGHER LEVEL THINKING)
# ==========================================

# - Add a "status" system per user (ACTIVE / BLOCKED / etc.)
# - Change status based on behavior inside the loop
# - Make the program behave differently depending on status


def main():
    # DESIGN EVERYTHING YOURSELF
    pass


if __name__ == "__main__":
    main()

