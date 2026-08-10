# Exercise 1 — Extract the username

# You receive:

# log = "FAILED LOGIN user=shadow"

# Your task:

# Create a function:

# extract_username(log)

# It should return:

# shadow


# Requirements
# Use string manipulation.
# Don't hardcode "shadow" inside the function.
# Return the username.
# Print the result outside the function.

# Don't worry about making this incredibly sophisticated. We're practicing manipulating a string into useful data.

# log = "FAILED LOGIN user=shadow"


# def get_username(log0):
#     temp_l = log0.strip("FAILED LOGIN")
#     username = temp_l[5:]
#     return username

# print(get_username(log))

# This method feels klinky, is there a way like specifically target the "username=" so i can like find like how you find something in a browser?

# trying the exercise again:



# log1 = "FAILED LOGIN user=shadow"


# # def get_username(log):
# #     logt_list = log.split()
# #     unclean_username = logt_list[2]
# #     splitted_username = unclean_username.split("user=")
# #     username = splitted_username[1]
# #     return username

# # print(get_username(log1))

# # 3rd time

# def get_username(log):
#     username = log.split("user=")[1]
#     return username

# print(get_username(log1))


# Exercise 2 — Extract the IP address

# You receive:

# log = "FAILED LOGIN user=shadow ip=192.168.1.20"

# Create:

# extract_ip(log)

# It should return:

# 192.168.1.20

# Again:

# function
# parameter
# string manipulation
# return
# print outside the function

# log1 = "FAILED LOGIN user=shadow ip=192.168.1.20"

# def extract_ip(log):
#     ip = log.split("ip=")[1]
#     return ip

# print(extract_ip(log1))



# Exercise 3 — Classify the login

# You receive these logs:

# logs = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=guest",
#     "SUCCESS LOGIN user=backup"
# ]

# Create:

# classify_log(log)

# It should return:

# "Success"

# or

# "Failed"

# depending on the log.

# Then use a loop to process every log.

# Expected:

# Success
# Failed
# Failed
# Success

# This one is important because you're combining:

# function
#    +
# parameter
#    +
# string searching
#    +
# conditional
#    +
# return
#    +
# loop


# logs1 = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=guest",
#     "SUCCESS LOGIN user=backup"
# ]

# def classify_log(logs):
#     login_state_list = []
#     for log in logs:
#         if "SUCCESS LOGIN" in log:
#             login_state_list.append("Success")
#         elif "FAILED LOGIN" in log:
#             login_state_list.append("Failed")
#         else:
#             login_state_list.append("Error?!")
#     return "\n".join(login_state_list)
            
# print(classify_log(logs1))





# Exercise 4 — Count failed logins

# Now take the same list:

# logs = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=guest",
#     "SUCCESS LOGIN user=backup",
#     "FAILED LOGIN user=shadow"
# ]

# Create:

# count_failed(logs)

# It should return:

# 3

# Don't print from inside the function.

# This is deliberately similar to the SOC exercise you already did.

# The difference is that now you're working with raw strings rather than dictionaries.


# logs1 = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=guest",
#     "SUCCESS LOGIN user=backup",
#     "FAILED LOGIN user=shadow"
# ]


# def count_failed(logs):
#     failed_counter = 0
#     for log in logs1:
#         if "FAILED LOGIN" in log:
#             failed_counter += 1
#     return failed_counter


# print(count_failed(logs1))



# 🔥 Exercise 5 — Find the users who failed

# Same data:

# logs = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=guest",
#     "SUCCESS LOGIN user=backup",
#     "FAILED LOGIN user=shadow"
# ]

# Create a function:

# failed_users(logs)

# It should return a list containing:

# ["shadow", "guest", "shadow"]

# Notice something important here.

# Previously you learned:

# return username

# But if there are multiple results, you can't return the first one and expect the rest to magically appear.

# You'll need to think about:

# create empty list
#         ↓
# loop through logs
#         ↓
# find failed log
#         ↓
# extract username
#         ↓
# add username to list
#         ↓
# return list after loop

# Don't copy that into your code. That's the conceptual roadmap I'm giving you.


# logs2 = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=guest",
#     "SUCCESS LOGIN user=backup",
#     "FAILED LOGIN user=shadow"
# ]

# def failed_users(logs):
#     failed_users_names = []
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             failed_users_names.append(log.split("user=")[1])
#     return failed_users_names

# print(failed_users(logs2))








# # 🎯 Final challenge — Mini SOC analysis

# # You receive:

# # logs = [
# #     "SUCCESS LOGIN user=admin ip=10.0.0.5",
# #     "FAILED LOGIN user=shadow ip=192.168.1.20",
# #     "FAILED LOGIN user=guest ip=172.16.5.10",
# #     "SUCCESS LOGIN user=backup ip=10.0.0.8",
# #     "FAILED LOGIN user=shadow ip=192.168.1.20"
# # ]

# # Write a program that determines:

# # How many failed logins occurred
# # Which users had failed logins
# # Which IP addresses were associated with failed logins

# # Expected information:

# # Failed attempts: 3

# # Failed users:
# # shadow
# # guest
# # shadow

# # Failed IPs:
# # 192.168.1.20
# # 172.16.5.10
# # 192.168.1.20
# # One restriction

# # Don't try to make one giant function.

# logs3 = [
#     "SUCCESS LOGIN user=admin ip=10.0.0.5",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=guest ip=172.16.5.10",
#     "SUCCESS LOGIN user=backup ip=10.0.0.8",
#     "FAILED LOGIN user=shadow ip=192.168.1.20"
# ]

# def failed_login_counter(logs):
#     failed_counter = 0
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             failed_counter += 1 
#     return f"Failed attempts: {failed_counter}"

# # print(failed_login_counter(logs3))



# def failed_login_users(logs):
#     # a list of the strings where every string has been divided into elements
#     log_list = []
#     # a list for failed user names
#     failed_user_lst = []
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             log_list.append(log.split("user=")[1])
#     for element in log_list:
#         failed_user_lst.append(element.split()[0])

#     return f"Failed users:\n{"\n".join(failed_user_lst)}"

# # print(failed_login_users(logs3))



# def failed_login_ip_addrs(logs):
#     log_list = []
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             log_list.append(log.split("ip=")[1])
   
#     return f"Failed IPs:\n{"\n".join(log_list)}"

# # print(failed_login_ip_addrs(logs3))

# # yeah again i used uknow possition, i when it comes to choosing the split. i could have used find method, but i thought maybe that is too extra. 

# # Final program


# def logs_analysis(logs):
#     return f"Log Analysis:\n\n{failed_login_counter(logs)}\n\n{failed_login_users(logs)}\n\n{failed_login_ip_addrs(logs)}"

# print(logs_analysis(logs3))


