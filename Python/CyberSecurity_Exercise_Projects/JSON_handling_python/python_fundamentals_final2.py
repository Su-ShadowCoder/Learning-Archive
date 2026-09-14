# ============================================================
# PYTHON FUNDAMENTALS — EXERCISES 31–50
# ============================================================
#
# PURPOSE:
# Complete the remaining Python fundamentals.
#
# You have already completed Exercises 1–30.
# These exercises focus on fundamentals that still need
# deliberate coverage or stronger practice.
#
# Do not look for the "shortest" solution.
# Focus on understanding why your code works.
# ============================================================


# ============================================================
# EXERCISE 31 — while Loops
# ============================================================
#
# Create a variable named attempts starting at 0.
#
# Requirements:
# 1. Use a while loop.
# 2. Continue looping while attempts is less than 5.
# 3. Print the current attempt number each iteration.
# 4. Increase attempts by one each iteration.
# 5. Print a final message after the loop finishes.
#
# Do not use a for loop.


# ============================================================
# EXERCISE 32 — break and continue
# ============================================================
#
# Use this list:
#
# events = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "LOGIN_FAILED",
#     "SYSTEM_UPDATE",
#     "LOGIN_FAILED",
#     "LOGIN_SUCCESS"
# ]
#
# Requirements:
# 1. Loop through the events.
# 2. Ignore "SYSTEM_UPDATE" using continue.
# 3. Print every remaining event.
# 4. Stop the loop completely when you encounter the
#    second "LOGIN_FAILED" event.
# 5. Use both continue and break.


# ============================================================
# EXERCISE 33 — String Indexing and Slicing
# ============================================================
#
# Create:
#
# username = "shadow"
#
# Requirements:
# 1. Print the first character.
# 2. Print the last character.
# 3. Print the first three characters.
# 4. Print the last three characters.
# 5. Print the string in reverse.
# 6. Print the length of the username.
#
# Do not manually write the characters you are extracting.


# ============================================================
# EXERCISE 34 — String Methods and Formatting
# ============================================================
#
# Create:
#
# username = "  Shadow  "
# status = "failed"
#
# Requirements:
# 1. Remove the surrounding whitespace from username.
# 2. Convert username to lowercase.
# 3. Convert status to uppercase.
# 4. Create a message containing both values.
# 5. The final message should clearly communicate that
#    Shadow has a failed login.
# 6. Use an f-string for the final message.


# ============================================================
# EXERCISE 35 — Type Conversion
# ============================================================
#
# You receive these values as strings:
#
# failed_attempts = "5"
# threshold = "3"
# account_locked = "False"
#
# Requirements:
# 1. Convert failed_attempts into an integer.
# 2. Convert threshold into an integer.
# 3. Convert account_locked into an actual Boolean.
# 4. Compare failed_attempts against threshold.
# 5. Print the resulting values.
# 6. Print the type of each converted value.
#
# Do not simply hard-code True or False for account_locked.
# Practice converting the string representation yourself.


# ============================================================
# EXERCISE 36 — Lists: Indexing, Slicing, and Modification
# ============================================================
#
# Create:
#
# ips = [
#     "192.168.1.10",
#     "192.168.1.20",
#     "10.0.0.15",
#     "172.16.5.10",
#     "10.0.0.20"
# ]
#
# Requirements:
# 1. Print the first IP.
# 2. Print the last IP.
# 3. Print the first three IPs.
# 4. Replace the second IP with another IP.
# 5. Add a new IP to the end.
# 6. Remove one IP.
# 7. Print the final list.


# ============================================================
# EXERCISE 37 — Tuples
# ============================================================
#
# Create a tuple named:
#
# event_types
#
# containing:
# - "LOGIN"
# - "LOGOUT"
# - "PASSWORD_CHANGE"
# - "FILE_ACCESS"
#
# Requirements:
# 1. Print the tuple.
# 2. Print the first item.
# 3. Print the last item.
# 4. Check whether "LOGIN" exists in the tuple.
# 5. Print the number of items.
# 6. Attempt to explain in a comment why you cannot directly
#    change one item inside the tuple.


# ============================================================
# EXERCISE 38 — Set Operations
# ============================================================
#
# Create:
#
# failed_ips = {
#     "192.168.1.10",
#     "192.168.1.20",
#     "10.0.0.15"
# }
#
# successful_ips = {
#     "192.168.1.20",
#     "10.0.0.20",
#     "172.16.5.10"
# }
#
# Requirements:
# 1. Find the IPs appearing in both sets.
# 2. Find all IPs appearing in either set.
# 3. Find IPs appearing only in failed_ips.
# 4. Add a new IP to failed_ips.
# 5. Remove an IP from successful_ips.
# 6. Print the resulting sets.


# ============================================================
# EXERCISE 39 — List Comprehension
# ============================================================
#
# Use:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Requirements:
# 1. Create a new list containing only even numbers.
# 2. Use a list comprehension.
# 3. Create another list containing each number multiplied by 2.
# 4. Use a list comprehension.
# 5. Print both lists.
#
# Do not use a normal for loop for the two requested lists.


# ============================================================
# EXERCISE 40 — Dictionary and Set Comprehensions
# ============================================================
#
# Use:
#
# usernames = ["shadow", "guest", "ahmed"]
#
# Requirements:
# 1. Create a dictionary comprehension where each username
#    is a key and the value is the length of the username.
# 2. Create a set comprehension containing the lengths of
#    the usernames.
# 3. Print both results.
#
# The purpose is to practice the syntax and behavior of
# dictionary and set comprehensions.


# ============================================================
# EXERCISE 41 — Sorting Data
# ============================================================
#
# Create:
#
# failed_attempts = {
#     "shadow": 7,
#     "guest": 2,
#     "ahmed": 5,
#     "admin": 9
# }
#
# Requirements:
# 1. Sort the dictionary items by failed-attempt count.
# 2. Produce the result from lowest to highest.
# 3. Produce the result from highest to lowest.
# 4. Use sorted().
# 5. Use key= to determine what is being sorted.
# 6. Print both results.
#
# Do not manually arrange the users.


# ============================================================
# EXERCISE 42 — lambda
# ============================================================
#
# Use:
#
# events = [
#     {"username": "shadow", "failed": 7},
#     {"username": "guest", "failed": 2},
#     {"username": "ahmed", "failed": 5},
#     {"username": "admin", "failed": 9}
# ]
#
# Requirements:
# 1. Sort the events by failed attempts.
# 2. Use sorted().
# 3. Use a lambda function as the key.
# 4. Sort from highest to lowest.
# 5. Print the resulting list.
#
# The goal is specifically to understand what the lambda is
# receiving and returning.


# ============================================================
# EXERCISE 43 — map()
# ============================================================
#
# Use:
#
# usernames = ["shadow", "guest", "ahmed", "admin"]
#
# Requirements:
# 1. Use map() to convert every username to uppercase.
# 2. Convert the resulting map object into a list.
# 3. Print the resulting list.
# 4. Do not use a list comprehension for this exercise.


# ============================================================
# EXERCISE 44 — filter()
# ============================================================
#
# Use:
#
# events = [
#     {"username": "shadow", "status": "Failed"},
#     {"username": "guest", "status": "Success"},
#     {"username": "ahmed", "status": "Failed"},
#     {"username": "admin", "status": "Success"}
# ]
#
# Requirements:
# 1. Use filter() to select only failed events.
# 2. Convert the result into a list.
# 3. Print the resulting list.
# 4. Do not use a list comprehension.


# ============================================================
# EXERCISE 45 — File Writing
# ============================================================
#
# Create a text file named:
#
# security_log.txt
#
# Requirements:
# 1. Open the file for writing.
# 2. Write at least three security log lines.
# 3. Close the file safely.
# 4. Use with open() rather than manually calling close().
#
# Each line should contain information such as:
# username, event type, and status.


# ============================================================
# EXERCISE 46 — File Reading
# ============================================================
#
# Using security_log.txt from Exercise 45:
#
# Requirements:
# 1. Open the file for reading.
# 2. Read its contents.
# 3. Print the contents.
# 4. Read the file using a with statement.
# 5. Do not manually call close().


# ============================================================
# EXERCISE 47 — File Processing
# ============================================================
#
# Using security_log.txt:
#
# Requirements:
# 1. Read the file line by line.
# 2. Count how many lines contain "FAILED".
# 3. Count how many lines contain "SUCCESS".
# 4. Store the counts in a dictionary named log_counts.
# 5. Print log_counts.
# 6. Build the counts dynamically.
#
# Do not manually enter the final counts.


# ============================================================
# EXERCISE 48 — Modules and Imports
# ============================================================
#
# Requirements:
# 1. Import the math module.
# 2. Use one function from math.
# 3. Import the random module.
# 4. Use one function from random.
# 5. Print the results.
#
# Then:
# 6. Import only one specific function from a module.
# 7. Use that function without writing the module name before it.
#
# The purpose is to understand both:
#
# import module
#
# and:
#
# from module import function


# ============================================================
# EXERCISE 49 — Exception Handling
# ============================================================
#
# Create a program that asks for a number.
#
# Requirements:
# 1. Use input() to receive the value.
# 2. Convert the value into an integer.
# 3. Handle invalid input with try/except.
# 4. If the user enters something that cannot become an
#    integer, print an appropriate message.
# 5. If the conversion succeeds, print the number.
# 6. Use the appropriate exception rather than catching
#    every possible exception.


# ============================================================
# EXERCISE 50 — Python Fundamentals Integration
# ============================================================
#
# This is the final fundamentals checkpoint.
#
# Use this security-event dataset:
#
# events = [
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed",
#         "attempts": "3"
#     },
#     {
#         "username": "guest",
#         "ip": "10.0.0.15",
#         "status": "Success",
#         "attempts": "1"
#     },
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed",
#         "attempts": "4"
#     },
#     {
#         "username": "ahmed",
#         "ip": "172.16.5.10",
#         "status": "Failed",
#         "attempts": "5"
#     },
#     {
#         "username": "guest",
#         "ip": "10.0.0.15",
#         "status": "Failed",
#         "attempts": "2"
#     }
# ]
#
# Requirements:
#
# 1. Create a function that processes the events.
#
# 2. Convert the "attempts" value from a string into an integer.
#
# 3. Count the total number of events.
#
# 4. Count successful events.
#
# 5. Count failed events.
#
# 6. Count failed events per username.
#
# 7. Collect unique IP addresses associated with failed events.
#
# 8. Identify users whose total failed attempts are greater
#    than 1.
#
# 9. Create a report dictionary containing all relevant
#    results.
#
# 10. Use appropriate data structures:
#     - dictionary
#     - list
#     - set
#
# 11. Use at least one helper function where appropriate.
#
# 12. Use try/except around the integer conversion.
#
# 13. Do not manually enter the final counts.
#
# 14. Print the completed report.
#
# 15. Keep the code readable with meaningful variable names.
#
# 16. Do not use external libraries.
#
# 17. After completing the program, add comments explaining
#     what each major processing step does.
#
# ============================================================
# FUNDAMENTALS CHECKPOINT
# ============================================================
#
# After Exercise 50, you should be able to explain:
#
# - why you chose each data structure
# - what each loop is doing
# - what each function receives
# - what each function returns
# - why you used a set in certain places
# - why you used a dictionary in certain places
# - what try/except protects
# - how the data changes as it moves through the program
#
# Do not move on simply because the code runs.
# Make sure you understand the code you wrote.
# ============================================================