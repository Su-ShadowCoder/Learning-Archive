# ============================================================
# PYTHON FUNDAMENTALS — EXERCISES 1–10
# ============================================================

# Final check and validation for my competence in python fundamentals.
# i might do more exercise for something to make it final when it comes to python. 

# ============================================================
# EXERCISE 1 — Variables & Types
# ============================================================

# Create variables for:
# - a username
# - an age
# - a failed login count
# - whether the account is locked
#
# Print each value and its type.


# YOUR CODE HERE

# username = "hackerman101"
# age = 31
# failed_login_attempts = 3
# account_status = "Locked"

# ============================================================
# EXERCISE 2 — Operators
# ============================================================

# Given:

# successful_logins = 17
# failed_logins = 5

# Calculate:
# - total login attempts
# - difference between successful and failed logins
# - percentage of attempts that failed
#
# Print all three results.


# YOUR CODE HERE

# total_login_attempts = successful_logins + failed_logins
# print(total_login_attempts)

# difference = successful_logins - failed_logins
# print(difference)

# fail_precentage = (failed_logins/total_login_attempts) * 100
# print(fail_precentage)


# ============================================================
# EXERCISE 3 — Strings
# ============================================================

# username = "shadow"
# ip = "192.168.1.20"

# Create a message containing both values.
#
# Then:
# - print the message in uppercase
# - print the length of the username
# - check whether "shadow" appears in the message


# YOUR CODE HERE

# print(f"{username}\n{ip}".upper())
# print(f"{len(username)}")
# if "shadow" in username:
#     print(f"There is 'shadow' in username.")

# ============================================================
# EXERCISE 4 — String Manipulation
# ============================================================

# raw_username = "   ShadowCoder   "

# Create a cleaned version of the username.
#
# It should:
# - remove unnecessary whitespace
# - be lowercase
#
# Print the original and cleaned versions.


# YOUR CODE HERE

# print(raw_username)
# print(raw_username.strip().upper())

# ============================================================
# EXERCISE 5 — Comparisons & Boolean Logic
# ============================================================

# failed_attempts = 4
# account_locked = True

# # Create conditions that determine:
# # - whether the user has too many failed attempts
# # - whether the account is currently locked
# # - whether BOTH conditions are true
# #
# # Print the results.


# # YOUR CODE HERE

# if failed_attempts == 4:
#     print(True)
# if account_locked:
#     print(True)
# if failed_attempts and account_locked == True:
#     print(True)


# ============================================================
# EXERCISE 6 — if / elif / else
# ============================================================

# failed_attempts = 7

# # Determine the login risk:
# #
# # 0–2    -> "LOW"
# # 3–5    -> "MEDIUM"
# # 6–10   -> "HIGH"
# # 11+    -> "CRITICAL"
# #
# # Print the resulting risk level.


# # YOUR CODE HERE

# if failed_attempts <= 2:
#     print("LOW")
# elif failed_attempts <= 5:
#     print("MEDIUM")
# elif failed_attempts <= 10:
#     print("HIGH")
# else:
#     print("CRITICAL")


# ============================================================
# EXERCISE 7 — Nested Conditions
# ============================================================

# username = "shadow"
# failed_attempts = 4
# account_locked = False

# # Determine whether the user should be allowed to attempt
# # another login.
# #
# # A user may attempt another login only if:
# # - the account is not locked
# # - AND failed attempts are fewer than 5
# #
# # Print the result.


# # YOUR CODE HERE

# if account_locked == False:
#     if failed_attempts < 5:
#         print(f"'{username}' is allowed to attempt another login.")


# ============================================================
# EXERCISE 8 — for Loop
# ============================================================

# login_attempts = [
#     "Success",
#     "Failed",
#     "Failed",
#     "Success",
#     "Failed"
# ]

# # Loop through the attempts.
# #
# # Print each attempt.
# #
# # Then count how many failed attempts there are.


# # YOUR CODE HERE

# failed_attempts = 0

# for attempt in login_attempts:
#     print(attempt)
    
#     if "Failed" in attempt:
#         failed_attempts += 1

# print(failed_attempts) 


# ============================================================
# EXERCISE 9 — for Loop + if
# ============================================================

# events1 = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "FILE_ACCESS",
#     "LOGIN_FAILED",
#     "PASSWORD_CHANGE",
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED"
# ]

# # Loop through the events.
# #
# # Print only the login failures.
# #
# # Also count how many login failures occurred.


# # YOUR CODE HERE

# # wait didnt i do exactly that in the previous exercise?

# c = 0

# for event in events1:
#     if event == "LOGIN_FAILED":
#         print(event)
#         c += 1

# print(c)


# ============================================================
# EXERCISE 10 — while Loop
# ============================================================



# Simulate login failures. like dude you have to give me more context man, you cannot just leave me here dry like that. what does that even mean in what capacity. 
#
# Keep increasing failed_attempts until it reaches 3.
#
# Print each attempt number.
#
# Once 3 failures are reached, print:
# "ACCOUNT LOCKED"


# YOUR CODE HERE

# cor_password = 455
# failed_attempts = 0

# locked_numb  = 3

# message1 = "ACCOUNT LOCKED"

# status = True

# while status == True:
#     usr_password_inp = int(input("Please enter your password:\n"))
#     if usr_password_inp != cor_password:
#         failed_attempts += 1
#     if failed_attempts == locked_numb:
#         print(message1)
#         break
#     if usr_password_inp == cor_password:
#         print("LOGGIN SUCCESSFUL!")
#         break


# ============================================================
# BOOLEAN LOGIC + REQUIREMENT TRANSLATION — TARGETED DRILL
# ============================================================


# ============================================================
# EXERCISE A — Boolean Conditions
# ============================================================

# failed_attempts = 4
# account_locked = False

# # Create Boolean expressions for:
# #
# # 1. Whether failed_attempts is greater than 3
# # 2. Whether failed_attempts is less than 5
# # 3. Whether the account is locked
# # 4. Whether the account is NOT locked
# # 5. Whether BOTH:
# #       - failed_attempts is greater than 3
# #       - account is not locked
# #
# # Store each result in a variable.
# # Print all five results.


# # YOUR CODE HERE

# value1 = failed_attempts > 3
# value2 = failed_attempts < 5
# account_locked = True
# account_not_locked = True
# both = value1 and account_locked

# print(value1)
# print(value2)
# print(account_locked)
# print(account_not_locked)
# print(both)


# ============================================================
# EXERCISE B — Thresholds vs Exact Values
# ============================================================

# failed_attempts = 6

# # Determine whether the account should be considered
# # "HIGH RISK".
# #
# # Requirement:
# # - HIGH RISK means failed_attempts is 5 or greater.
# #
# # Print the result as True or False.
# #
# # Do NOT check for one exact number.


# # YOUR CODE HERE

# if failed_attempts >= 5:
#     print(True)




# ============================================================
# EXERCISE C — AND / OR
# ============================================================

# username = "shadow"
# failed_attempts = 7
# account_locked = False

# # A login attempt should be blocked if:
# #
# # - the account is locked
# # OR
# # - failed_attempts is 5 or greater
# #
# # Create the Boolean condition.
# #
# # Print whether the login attempt should be blocked.


# # YOUR CODE HERE

# if failed_attempts >= 5:
#     account_locked = True

# print(account_locked)


# ============================================================
# EXERCISE D — Multiple Requirements
# ============================================================

# failed_attempts = 2
# account_locked = False
# is_admin = True

# # An account should receive a security warning if:
# #
# # - failed_attempts is 3 or greater
# # AND
# # - the account is not locked
# #
# # OR
# #
# # - the account belongs to an admin
# #
# # Create the condition.
# #
# # Print the result.


# # YOUR CODE HERE


# if failed_attempts >= 3 and account_locked == False:
#     print("warning")
# if is_admin == True:
#     print("warning")





# ============================================================
# EXERCISE E — Translate the Requirement
# ============================================================

# ip = "192.168.1.20"
# failed_attempts = 8
# account_locked = False

# # A suspicious login event is one where:
# #
# # - the IP is "192.168.1.20"
# # AND
# # - failed_attempts is greater than 5
# # AND
# # - the account is not locked
# #
# # Create ONE Boolean condition representing the entire rule.
# #
# # Print the result.


# # YOUR CODE HERE

# suspicious_log = False

# if ip and failed_attempts > 5 and account_locked == False:
#     suspicious_log = True

# print(suspicious_log)

# ============================================================
# EXERCISE F — Negation
# ============================================================

# account_locked = False
# maintenance_mode = True

# # A system is available for login only when:
# #
# # - the account is NOT locked
# # AND
# # - maintenance mode is NOT active
# #
# # Create the condition.
# #
# # Print the result.


# # YOUR CODE HERE
# sys_available = False

# if account_locked == False and maintenance_mode == False:
#     sys_available = True

# print(sys_available)

# # ============================================================
# # EXERCISE G — Boolean Reasoning
# # ============================================================

# failed_attempts = 4
# account_locked = False

# # Without running the code, determine what each expression
# # should evaluate to.
# #
# # Then write Python code that evaluates them.
# #
# # 1. failed_attempts > 3
# # 2. failed_attempts > 5
# # 3. account_locked
# # 4. not account_locked
# # 5. failed_attempts > 3 and not account_locked
# # 6. failed_attempts > 5 or account_locked
# #
# # Print all six results.


# # YOUR CODE HERE
# # based on the info above 
# # True
# # False
# # False
# # True
# # True
# # False

# if failed_attempts > 3:
#     print(True)
# else:
#     print(False)

# if failed_attempts > 5:
#     print(True)
# else:
#     print(False)

# if account_locked:
#     print(True)
# else:
#     print(False)

# if account_locked == False:
#     print(False)
# else:
#     print(True)

# if failed_attempts > 3 and account_locked == False:
#     print(True)
# else:
#     print(False)

# if failed_attempts > 5 or account_locked == True:
#     print(True)
# else:
#     print(False)



# # ============================================================
# # EXERCISE H — Security Rule
# # ============================================================

# username = "guest"
# failed_attempts = 3
# account_locked = False
# ip_trusted = False

# # Allow login only if ALL of these are true:
# #
# # - account is not locked
# # - failed_attempts is fewer than 5
# # - IP is trusted
# #
# # Create the Boolean condition.
# #
# # Print whether login is allowed.


# # YOUR CODE HERE

# authorization = False

# if account_locked == False and failed_attempts < 5 and ip_trusted == True:
#     authorization = True

# print(authorization)

# ============================================================
# PYTHON FUNDAMENTALS — EXERCISES 11–20
# ============================================================


# ============================================================
# EXERCISE 11 — Lists: Accessing Data
# ============================================================

# failed_ips = [
#     "192.168.1.20",
#     "10.0.0.15",
#     "172.16.5.10",
#     "192.168.1.20",
#     "10.0.0.15"
# ]

# 1. Print the first IP address.
# 2. Print the last IP address.
# 3. Print the third IP address.
# 4. Print how many IP addresses are in the list.


# YOUR CODE HERE

# print(failed_ips[0])
# print(len(failed_ips))
# print(failed_ips[4])
# print(failed_ips[2])
# print(len(failed_ips))

# ============================================================
# EXERCISE 12 — Lists: Modifying Data
# ============================================================

# blocked_ips = [
#     "192.168.1.20",
#     "10.0.0.15",
#     "172.16.5.10"
# ]

# # 1. Add "192.168.1.50" to the list.
# # 2. Remove "10.0.0.15".
# # 3. Change "172.16.5.10" to "172.16.5.99".
# # 4. Print the final list.


# # YOUR CODE HERE

# blocked_ips.append("192.168.1.50")
# blocked_ips.remove("10.0.0.15")
# blocked_ips[1] = "172.16.5.99"

# print(blocked_ips)

# ============================================================
# EXERCISE 13 — Lists + Loops
# ============================================================

# events = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "FILE_ACCESS",
#     "LOGIN_FAILED",
#     "PASSWORD_CHANGE",
#     "LOGIN_FAILED"
# ]

# # Loop through the list.
# #
# # Count:
# # - successful logins
# # - failed logins
# # - all other events
# #
# # Print the three counts.


# # YOUR CODE HERE

# count_successful = 0
# count_failed = 0
# count_other = 0

# for event in events:
#     if event == "LOGIN_SUCCESS":
#         count_successful += 1
#     if event == "LOGIN_FAILED":
#         count_failed += 1
#     if event != "LOGIN_SUCCESS" and event != "LOGIN_FAILED":
#         count_other += 1

# print(count_successful, count_failed, count_other)

# ============================================================
# EXERCISE 14 — List Filtering
# ============================================================

# events = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "FILE_ACCESS",
#     "LOGIN_FAILED",
#     "PASSWORD_CHANGE",
#     "LOGIN_FAILED"
# ]

# Create a new list containing ONLY the failed login events.
#
# Do not modify the original list.
#
# Print the new list.


# YOUR CODE HERE



# ============================================================
# EXERCISE 15 — List Slicing
# ============================================================

# security_events = [
#     "LOGIN_FAILED",
#     "LOGIN_SUCCESS",
#     "FILE_ACCESS",
#     "PASSWORD_CHANGE",
#     "LOGIN_FAILED",
#     "LOGOUT",
#     "LOGIN_FAILED"
# ]

# # Create new lists containing:
# #
# # 1. The first three events
# # 2. The last three events
# # 3. Every second event
# #
# # Print all three new lists.
# #
# # Use list slicing.


# # YOUR CODE HERE

# new_list1 = []
# new_list2 = []
# new_list3 = []

# new_list1 = security_events[0:3]
# print(new_list1)

# new_list2 = security_events[-3:]
# print(new_list2)

# new_list3 = security_events[::2]
# print(new_list3)

# ============================================================
# EXERCISE 16 — Tuples
# ============================================================

# login_event = (
#     "shadow",
#     "192.168.1.20",
#     "LOGIN_FAILED"
# )

# # 1. Access and print the username.
# # 2. Access and print the IP address.
# # 3. Access and print the event type.
# # 4. Print the number of items in the tuple.


# # YOUR CODE HERE

# print(login_event[0])
# print(login_event[1])
# print(login_event[2])
# print(len(login_event))

# ============================================================
# EXERCISE 17 — Tuple Unpacking
# ============================================================

# event = (
#     "shadow",
#     "192.168.1.20",
#     "LOGIN_FAILED"
# )

# # Unpack the tuple into three variables:
# #
# # username
# # ip
# # status
# #
# # Then print the three variables.


# # YOUR CODE HERE

# (username, ip, status) = event

# print(username)
# print(ip)
# print(status)

# ============================================================
# EXERCISE 18 — Sets: Removing Duplicates
# ============================================================

# login_ips = [
#     "192.168.1.20",
#     "10.0.0.15",
#     "192.168.1.20",
#     "172.16.5.10",
#     "10.0.0.15",
#     "192.168.1.20"
# ]

# # Create a set containing only the unique IP addresses.
# #
# # Print the set.
# #
# # Do not manually remove the duplicates.


# # YOUR CODE HERE

# nondup_ip = list(dict.fromkeys(login_ips))
# print(nondup_ip)

# ============================================================
# EXERCISE 19 — Sets: Membership
# ============================================================

# known_malicious_ips = {
#     "192.168.1.20",
#     "10.10.10.50",
#     "172.16.5.99"
# }

# incoming_ip = "192.168.1.20"

# # Determine whether incoming_ip exists in the set.
# #
# # Store the Boolean result in a variable.
# #
# # Print the result.


# # YOUR CODE HERE

# incoming_ip_status = False

# if incoming_ip in known_malicious_ips:
#     incoming_ip_status = True
# print(incoming_ip_status)

# # ============================================================
# # EXERCISE 20 — Security Event Collection Challenge
# # ============================================================

# events = [
#     {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
#     {"username": "guest", "status": "Success", "ip": "10.0.0.15"},
#     {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
#     {"username": "ahmed", "status": "Failed", "ip": "172.16.5.10"},
#     {"username": "guest", "status": "Failed", "ip": "10.0.0.15"},
# ]

# # Analyze the events.
# #
# # Produce:
# #
# # 1. A list containing all failed events.
# # 2. A set containing all unique IP addresses.
# # 3. A set containing all usernames that had at least one
# #    failed login.
# # 4. A count of successful logins.
# # 5. A count of failed logins.
# #
# # Print all five results.
# #
# # Use:
# # - lists
# # - sets
# # - loops
# # - conditionals
# #
# # Do not modify the original events list.


# # YOUR CODE HERE

# failed_events = []
# unique_ips = ()
# failed_username = []
# count_successful = 0
# count_failed = 0

# all_ip = []

# for event in events:
#     if event['status'] == 'Failed':
#         failed_events.append(event)
#         count_failed += 1
#         username_value = event['username']
#         failed_username.append(username_value)
#     if event['status'] == "Success":
#         count_successful += 1
#     ip_value = event['ip']
#     all_ip.append(ip_value)

# unique_ips = list(dict.fromkeys(all_ip))
# failed_username = list(dict.fromkeys(failed_username))

# print(failed_events)
# print(unique_ips)
# print(failed_username)
# print(count_successful)
# print(count_failed)

# ============================================================
# RETAKE — EXERCISES 14, 18, AND 20
# ============================================================


# ============================================================
# EXERCISE 14 — List Filtering
# ============================================================

# events = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "FILE_ACCESS",
#     "LOGIN_FAILED",
#     "PASSWORD_CHANGE",
#     "LOGIN_FAILED"
# ]

# # Create a NEW list containing ONLY the failed login events.
# #
# # Requirements:
# # - The new list must contain only "LOGIN_FAILED" entries.
# # - Do not modify the original events list.
# # - Print the new list.


# # YOUR CODE HERE

# newlist1 = []

# for event in events:
#     if event == "LOGIN_FAILED":
#         newlist1.append(event)

# print(newlist1)



# ============================================================
# EXERCISE 18 — Sets: Removing Duplicates
# ============================================================

# login_ips = [
#     "192.168.1.20",
#     "10.0.0.15",
#     "192.168.1.20",
#     "172.16.5.10",
#     "10.0.0.15",
#     "192.168.1.20"
# ]

# Create a SET containing only the unique IP addresses.
#
# Requirements:
# - The final result must be a set.
# - Duplicate IP addresses must occur only once.
# - Do not manually remove duplicates.
# - Print the set.
#
# Do not convert the final result back into a list.


# YOUR CODE HERE

# new_set = set(login_ips)
# print(new_set)

# # ============================================================
# # EXERCISE 20 — Security Event Collection Challenge
# # ============================================================

# events = [
#     {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
#     {"username": "guest", "status": "Success", "ip": "10.0.0.15"},
#     {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
#     {"username": "ahmed", "status": "Failed", "ip": "172.16.5.10"},
#     {"username": "guest", "status": "Failed", "ip": "10.0.0.15"},
# ]

# # Analyze the events.
# #
# # Produce and print:
# #
# # 1. A LIST containing all failed events.
# # 2. A SET containing all unique IP addresses.
# # 3. A SET containing all usernames that had at least one
# #    failed login.
# # 4. An integer count of successful logins.
# # 5. An integer count of failed logins.
# #
# # Requirements:
# # - Use a loop.
# # - Use conditionals.
# # - Do not modify the original events list.
# # - Make sure the final results have the exact collection types
# #   requested above.
# #
# # Check every requirement before submitting your code.


# # YOUR CODE HERE


# all_failed_events = []

# unique_ip_set = []

# username_failed = []

# count_successful = 0

# count_failed = 0

# for event in events:
#     ip_value = event['ip']
#     unique_ip_set.append(ip_value)
#     if event['status'] == "Failed":
#         all_failed_events.append(event)
#         count_failed += 1
#         username_value = event['username']
#         username_failed.append(username_value)
#     else:
#         count_successful += 1


# unique_ip_set = set(unique_ip_set)
# username_failed_set = set(username_failed)

# print(all_failed_events)
# print(unique_ip_set)
# print(username_failed_set)
# print(count_successful)
# print(count_failed)


# ============================================================
# PYTHON FUNDAMENTALS — EXERCISES 21–30
# ============================================================


# ============================================================
# EXERCISE 21 — Create and Access a Dictionary
# ============================================================

# Create a dictionary named user_account containing:
# - username
# - email
# - failed_attempts
# - account_locked

# Requirements:
# 1. Assign suitable values to all four keys.
# 2. Print the value of username.
# 3. Print the value of failed_attempts.
# 4. Print the complete dictionary.
# 5. Print the number of key-value pairs.

# user_account = {
#     'username': 'shadow',
#     'email': 'hello@live.com',
#     'failed_attempts': 1,
#     'account_locked': False
# }

# print(user_account['username'])

# print(user_account['failed_attempts'])

# print(user_account)

# print(len(user_account))


# ============================================================
# EXERCISE 22 — Modify Dictionary Values
# ============================================================

# Using the user_account dictionary from Exercise 21:

# Requirements:
# 1. Change failed_attempts to a different number.
# 2. Change account_locked to True.
# 3. Add a new key named last_login.e
# 4. Add a new key named ip_address.
# 5. Print the updated dictionary.

# user_account['failed_attempts'] = 3

# user_account['account_locked'] = True

# user_account['last_login'] = None

# user_account['ip_address'] = None

# print(user_account)

# you didnt specify to add value to it. 

# ============================================================
# EXERCISE 23 — Dictionary Membership
# ============================================================

# Create a dictionary named security_event containing:
# - username
# - ip
# - status
# - event_type

# Requirements:
# 1. Check whether the key "username" exists.
# 2. Check whether the key "timestamp" exists.
# 3. Print a Boolean result for each check.
# 4. Do not add or remove any keys.

# security_event = {
#     'username': 'shadow',
#     'ip': '192.168.127.1',
#     'status': 'high risk',
#     'event_type': 'security alert'
# }

# key = 'username'
# key1 = 'timestamp'

# print(key in  security_event)
# print(key1 in security_event)



# ============================================================
# EXERCISE 24 — Loop Through Dictionary Keys and Values
# ============================================================

# Using the security_event dictionary:

# Requirements:
# 1. Loop through the dictionary's keys.
# 2. Print each key.
# 3. Loop through the dictionary's values.
# 4. Print each value.
# 5. Loop through the dictionary's key-value pairs.
# 6. Print each key together with its corresponding value.


# for key, value in security_event.items():
#     print(key)
# for key, value in security_event.items():
#     print(value)
# for key, value in security_event.items():
#     print(key, value)



# ============================================================
# EXERCISE 25 — Count Statuses with a Dictionary
# ============================================================

events1 = [
    {"username": "shadow", "status": "Failed"},
    {"username": "guest", "status": "Success"},
    {"username": "shadow", "status": "Failed"},
    {"username": "ahmed", "status": "Failed"},
    {"username": "guest", "status": "Failed"},
    {"username": "shadow", "status": "Success"}
]

status_counts = {'Failed': 0,
'Success': 0}
failed= 0
success= 0
for event in events1:
    if event['status'] == 'Failed':
        status_counts['Failed'] += 1
    if event['status'] == 'Success':
        status_counts['Success'] += 1

print(status_counts)


# Requirements:
# 1. Create a dictionary named status_counts.
# 2. Loop through events.
# 3. Count how many times each status appears.
# 4. Store the counts in status_counts.
# 5. Do not manually enter the final counts.
# 6. Print status_counts.

# status_counts = {}
# temp_list = []

# for event in events1:
#     if event['status'] == 'Failed':
#         temp_list.append(event)
        

# print(temp_list)


# for event in temp_list:
#     username_value = event['username']
#     if event['username'] not in status_counts:
#         status_counts[username_value] = 1
#     else:
#         status_counts[username_value] += 1

# print(status_counts)

# i think your question is wrong, to add dicts to dicts or oemthing 



# ============================================================
# EXERCISE 26 — Count Failed Attempts per User
# ============================================================

# Using the same events list from Exercise 25:

# Requirements:
# 1. Create a dictionary named failed_attempts_by_user.
# 2. Count only events whose status is "Failed".
# 3. Use the username as the dictionary key.
# 4. Use the number of failed attempts as the dictionary value.
# 5. Print failed_attempts_by_user.

failed_attempts_by_user = {}

# well well well look what the cat dragged in. 

# ============================================================
# EXERCISE 27 — Nested Dictionary Access
# ============================================================

# Create a dictionary named security_report with this structure:
#
# - summary
#   - total_events
#   - failed_events
#   - successful_events
# - system
#   - hostname
#   - ip_address
#   - operating_system
# - administrator
#   - username
#   - role

# Requirements:
# 1. Assign suitable values to every field.
# 2. Print the total number of events.
# 3. Print the system hostname.
# 4. Print the administrator username.
# 5. Print the administrator role.
# 6. Print the complete nested dictionary.

security_report = {
    'summary': 
    {'total_events': 5, 
    'failed_events': 3, 
    'successful_event': 2},
    'system': 
    {'hostname':'homepc',
    'ip_address': '192.168.127.1',
    'operating_system': 'Linux'},
    'administrator': 
    {'username': 'shadow',
    'role': 'analyst'}
}

# print(security_report['summary']['total_events'])
# print(security_report['system']['hostname'])
# print(security_report['administrator']['username'])
# print(security_report['administrator']['role'])
# print(security_report)

# ============================================================
# EXERCISE 28 — Update Nested Dictionary Values
# ============================================================

# Using security_report from Exercise 27:

# Requirements:
# 1. Increase summary["failed_events"] by one.
# 2. Increase summary["total_events"] by one.
# 3. Change the administrator's role.
# 4. Change the system's IP address.
# 5. Add a new field named status inside system.
# 6. Print the updated nested dictionary.

security_report['summary']['failed_events'] += 1
security_report['summary']['total_events'] += 1
security_report['administrator']['role'] = 'CISO'
security_report['system']['ip_address'] = '10.10.10'
security_report['system']['Distrubution'] = 'Kali'
print(security_report)

# ============================================================
# EXERCISE 29 — Safely Access Dictionary Data
# ============================================================

# event = {
#     "username": "shadow",
#     "status": "Failed",
#     "ip": "192.168.1.20"
# }

# # Requirements:
# # 1. Retrieve the value of "username" safely.
# # 2. Retrieve the value of "timestamp" safely without causing a KeyError.
# # 3. Use a fallback value when "timestamp" does not exist.
# # 4. Print both retrieved values.
# # 5. Do not add "timestamp" to the dictionary.

# x = event.get("username")
# print(x)
# y = event.get("timestamp", "15:30")
# print(y)

# ============================================================
# EXERCISE 30 — Mini Security Report
# ============================================================

# events = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "10.0.0.15", "status": "Success"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "ahmed", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "guest", "ip": "10.0.0.15", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Success"}
# ]

# Requirements:
# 1. Create a dictionary named report.
# 2. Count the total number of events.
# 3. Count successful events.
# 4. Count failed events.
# 5. Count failed attempts per username.
# 6. Collect unique IP addresses associated with failed events.
# 7. Collect usernames associated with failed events.
# 8. Store all results inside report using meaningful keys.
# 9. Use a dictionary, list, or set for each result where appropriate.
# 10. Build the results dynamically using loops and conditionals.
# 11. Do not manually enter the final counts or values.
# 12. Print the complete report.


# events1 = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "10.0.0.15", "status": "Success"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "ahmed", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "guest", "ip": "10.0.0.15", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Success"}
# ]

# #code:



# # 2. Count the total number of events.
# def count_total_events(events):
#     return len(events)

# # 3. Count successful events.
# def count_successful_events(events):
#     successful_event = 0
#     for event in events:
#         if event['status'] == 'Success':
#             successful_event += 1
#     return successful_event

# # 4. Count failed events.
# def count_failed_events(events):
#     failed_events = 0
#     for event in events:
#         if event['status'] == 'Failed':
#             failed_events += 1
#     return failed_events

# # 5. Count failed attempts per username.
# def failed_attempts_username(events):
    
#     all_failed_users = []
#     for event in events:
#         if event['status'] == 'Failed':
#             all_failed_users.append(event)

#     username_per_attempts = {}
#     for event in all_failed_users:
#         username_value = event['username']
#         if username_value not in username_per_attempts:
#             username_per_attempts[username_value] = 1
#         else:
#             username_per_attempts[username_value] += 1
    
#     return username_per_attempts

# # 6. Collect unique IP addresses associated with failed events.
# def all_unique_failed_ips(events):
    
#     all_failed_users = []
#     for event in events:
#         if event['status'] == 'Failed':
#             all_failed_users.append(event)

#     all_ips = set()
#     for event in all_failed_users:
#         ip_value = event['ip']
#         all_ips.add(ip_value)

#     return all_ips

# # 7. Collect usernames associated with failed events.
# def all_failed_usernames(events):
#     all_failed_users = []
#     for event in events:
#         if event['status'] == 'Failed':
#             all_failed_users.append(event)

#     unique_failed_users = set()
#     for event in all_failed_users:
#         username_value = event['username']
#         unique_failed_users.add(username_value)
#     return unique_failed_users


# #you didnt specify alone or not. but i will go on to not do duplicates becuase you asked based on associated with  failed events. 

# # 8. Store all results inside report using meaningful keys.


# # 9. Use a dictionary, list, or set for each result where appropriate.

# # 10. Build the results dynamically using loops and conditionals.

# def report(events):
#     value1 = count_total_events(events)
#     value2 = count_successful_events(events)
#     value3 = count_failed_events(events)
#     value4 = failed_attempts_username(events)
#     value5 = all_unique_failed_ips(events)
#     value6 = all_failed_usernames(events)


#     report = {
#         'total_events': value1,
#         'successful_events': value2,
#         'failed_events': value3,
#         'failed_usernames_attempts': value4,
#         'relative_failed_unqiue_ips': value5,
#         'relative_failed_unqiue_usernames': value6
#     }
#     return report

# def main():
#     print(report(events1))


# if __name__ == '__main__':
#     main()


#######################################
# ============================================================
# EXERCISE 24 — Loop Through Dictionary Keys and Values
# ============================================================

# Using the security_event dictionary:

# Requirements:
# 1. Loop through the dictionary's keys.
# 2. Print each key.
# 3. Loop through the dictionary's values.
# 4. Print each value.
# 5. Loop through the dictionary's key-value pairs.
# 6. Print each key together with its corresponding value.


# for key, value in security_event.items():
#     print(key)
# for key, value in security_event.items():
#     print(value)
# for key, value in security_event.items():
#     print(key, value)


#####################################################

# events1 = [
#     {"username": "shadow", "status": "Failed"},
#     {"username": "guest", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "ahmed", "status": "Failed"},
#     {"username": "guest", "status": "Failed"},
#     {"username": "shadow", "status": "Success"}
# ]

# status_counts = {'Failed': 0,
# 'Success': 0}
# failed= 0
# success= 0
# for event in events1:
#     if event['status'] == 'Failed':
#         status_counts['Failed'] += 1
#     if event['status'] == 'Success':
#         status_counts['Success'] += 1

# print(status_counts)

# ######################################################

# security_report = {
#     'summary': 
#     {'total_events': 5, 
#     'failed_events': 3, 
#     'successful_event': 2},
#     'system': 
#     {'hostname':'homepc',
#     'ip_address': '192.168.127.1',
#     'operating_system': 'Linux'},
#     'administrator': 
#     {'username': 'shadow',
#     'role': 'analyst'}
# }

# # print(security_report['summary']['total_events'])
# # print(security_report['system']['hostname'])
# # print(security_report['administrator']['username'])
# # print(security_report['administrator']['role'])
# # print(security_report)

# # ============================================================
# # EXERCISE 28 — Update Nested Dictionary Values
# # ============================================================

# # Using security_report from Exercise 27:

# # Requirements:
# # 1. Increase summary["failed_events"] by one.
# # 2. Increase summary["total_events"] by one.
# # 3. Change the administrator's role.
# # 4. Change the system's IP address.
# # 5. Add a new field named status inside system.
# # 6. Print the updated nested dictionary.

# security_report['summary']['failed_events'] += 1
# security_report['summary']['total_events'] += 1
# security_report['administrator']['role'] = 'CISO'
# security_report['system']['ip_address'] = '10.10.10'
# security_report['system']['Distrubution'] = 'Kali'
# print(security_report)

# # you said yourselff that exercise 26 was ok or something like that 

#########################################################################

