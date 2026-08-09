# Exercise 1 — Cleaning log input

# You receive:

# "   FAILED LOGIN ATTEMPT   "

# Store it in a variable called log.

# Tasks:

# Print the original string.
# Remove the spaces at the beginning and end.
# Store the cleaned result in a new variable.
# Print the cleaned result.

# Don't look up .strip() yet. Try to remember it.


# log = "   FAILED LOGIN ATTEMPT   "

# print(log)

# clean_log = log.strip()

# print(clean_log)

# i was looking at what you said in what we will cover, so all i needed was seeing the list of things we will cover and i directly knew which ones to use. i saw strip. and knew how to use it, except for print log.strip() directly one time because i forgot that you had to like first give a new var for it. 

# Exercise 2 — Normalizing usernames

# Information:

# Username: Shadow

# Store it in:

# username

# Tasks:

# Convert it to lowercase.
# Convert it to uppercase.
# Print both results.

# username = 'Shadow'

# username_lowc = username.lower()

# username_upperc = username.upper()

# print(username_lowc + "\n" + username_upperc)


# Exercise 3 — Detecting an event

# You receive:

# "Failed Login Attempt"

# Store it in:

# event

# Task:

# Check whether "Failed" occurs in the event.

# Your output should be a Boolean:

# True


# event = "Failed Login Attempt"

# def check_fail_event(x):
#     temp_lst = x.split()
#     if "Failed" in temp_lst:
#         return True

# event_output = check_fail_event(event)

# print(check_fail_event(event))

# print(event_output)

# this was lot more difficult i hadd to go to w3schools pytons stuff to check a couple examples
# i did forget in wat manner again you could print out where it is in the memory. 
# but after experimenting logic was pretty easy and intuitive. 

# Exercise 4 — File analysis

# You receive:

# "invoice.exe"

# Store it in:

# filename

# Task:

# Check whether the filename ends with .exe.

# Return/print the Boolean result.

# filename = "invoice.exe"

# def check_exe_filetype(x):
#     temp_l = x.strip()
#     if ".exe" in temp_l:
#         return True

# print(check_exe_filetype(filename))

# much more easier once i did the previous exercious. like molten choclate. 

# ⭐ Cyber Exercise — Log classification

# You receive these logs:

# log1 = "SUCCESSFUL LOGIN user=admin"
# log2 = "FAILED LOGIN user=shadow"
# log3 = "FAILED LOGIN user=guest"

# # For each log, determine whether it contains "FAILED".

# # You should get:

# # False
# # True
# # True

# # Use a loop.


# log_list_1 = [log1, log2, log3]

# def failed_loglist_checker(log_list):
#     for log in log_list:
#         temp_l = log.split()
#         if "FAILED" in temp_l:
#             print(True)
#         else:
#             print(False)

# check_log_l_1 = failed_loglist_checker(log_list_1)

# print(check_log_l_1)

# i had problems with return as it directly went out of the function once i did return. and also none keeps popping up?

# 🔥 Mini Challenge

# Don't worry about making a function yet.

# You receive:

# log1 = "   FAILED LOGIN user=shadow   "

# Your program should:

# Remove the unnecessary spaces.
# Convert the log to lowercase.
# Check whether "failed" is present.
# Print the final Boolean.

# Expected:

# True

# def log_cleaner(log):
#     stripped_log = log.strip("  ")
#     print(stripped_log)
#     low_log = stripped_log.lower()
#     print(low_log)
#     temp_log_l = low_log.split()
#     print(temp_log_l)
#     if "failed" in temp_log_l:
#         return True


# log1_check = log_cleaner(log1)

# print(log1_check)

# that is a nasty trick question you did there i compared it with "FAILED" only to realise you required me to lower the log. very nasty i must say. 

# Exercise 1

# log1 = "WARNING: Multiple failed login attempts detected"

# def contains_warning(log):
#     return "WARNING" in log

# log1_check = contains_warning(log1)

# print(log1_check)

# Exercise 2

# file1 = "invoice.exe"
# file2 = "report.pdf"
# file3 = "malware.exe.backup"
# file4 = "script.EXE"

# file_list_1 = [file1, file2, file3, file4]

# def is_executable(file_list):
#     for file in file_list:
#         if file.endswith(".exe"):
#             return True

# file_list1_check = is_executable(file_list_1)

# print(file_list1_check)