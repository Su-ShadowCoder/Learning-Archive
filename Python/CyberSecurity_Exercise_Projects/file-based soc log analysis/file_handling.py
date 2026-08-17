# 1. 
# Then write Python that:

# Opens the file.
# Reads its contents.
# Prints the contents.

# login_logs_f = open("login_logs.txt")
# print(login_logs_f.read())

# with open("login_logs.txt") as login_logs_file:
#     print(login_logs_file.read())

# 2. 
# proccess every line of the text instead of one whole text

# i think of implementing a loop but we will have to see about that in sha Allah.


# with open("login_logs.txt") as f:
#     for line in f:
#         print(line)



# 3. 


# def extract_failed_login_attempts_file(file):
#     failed_attempts = 0
#     with open(file) as f:
#         for line in f:
#             if "FAILED" in line:
#                 failed_attempts += 1
#     return failed_attempts

# print(extract_failed_login_attempts_file("login_logs.txt"))



# # 4. 

# def extract_failed_login_user_f(file):
#     temp_list = []
#     with open(file) as f:
#         for line in f:
#             if "FAILED" in line:
#                 temp_list.append(line.split("user=")[1])
#     return "\n".join(temp_list)

# print(extract_failed_login_user_f("login_logs.txt"))


# 5. 

# def count_failed_users(file):
#     dict_failed_users = {}
#     with open(file) as f:
#         for line in f:
#             if "FAILED" in line:
#                 key = line.split("user=")[1].strip("\n")
#                 if key not in dict_failed_users:
#                     dict_failed_users[key] = 1
#                 else:
#                     dict_failed_users[key] += 1
#     return dict_failed_users



# print(count_failed_users("login_logs.txt"))

# 6. 


# def count_failed_users(file):
#     temp_dict = {}
#     with open(file)  as f:
#         for line in f:
#             if "FAILED user=" in line:
#                 key = line.split("user=")[1].strip()
#                 if key not in temp_dict:
#                     temp_dict[key] = 1
#                 else:
#                     temp_dict[key] += 1
#     return temp_dict

# print(count_failed_users("logs2.txt"))


# # 7. 


# # extract failed avents from selected or entered file

# def extract_failed_events(file):
#     extracted_failed_events = []
#     with open(file) as f:
#         for event in f:
#             if "FAILED LOGIN" in event:
#                 splitted_line = event.split("user=")[1]
#                 value_user = splitted_line.split()[0]
#                 value_ip = event.split("ip=")[1].strip()
#                 this_dict = {"username": value_user, "ip": value_ip}
#                 extracted_failed_events.append(this_dict)
#     return extracted_failed_events

# print(extract_failed_events("logs3.txt"))


# # Expected return value
# # [
# #     {"username": "shadow", "ip": "192.168.1.20"},
# #     {"username": "guest", "ip": "172.16.5.10"},
# #     {"username": "shadow", "ip": "192.168.1.20"}
# # ]


# 🟡 Exercise 8 — Defensive parsing with try/except

# Create:

# def extract_failed_ips(file):

# The function receives a filename containing:

# SUCCESS LOGIN user=admin ip=10.0.0.5
# FAILED LOGIN user=shadow ip=192.168.1.20
# FAILED LOGIN user=guest
# FAILED LOGIN user=ahmed ip=172.16.5.10
# SUCCESS LOGIN user=backup ip=10.0.0.8

# Expected result
# [
#     "192.168.1.20",
#     "172.16.5.10"
# ]


# def extract_failed_ips(file):
#         failed_ips_list = []
#         with open(file) as f:
#             for event in f:
#                 try:
#                     if "FAILED LOGIN" in event:
#                         failed_ips_list.append(event.split("ip=")[1].strip())
#                 except Exception as error:
#                     print("Missing ip for an event in this file!")
#         return failed_ips_list

# print(extract_failed_ips("logs8.txt"))
                



# 🟡 Exercise 9 — Analyze structured events

# Use this Python data:

# events1 = [
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
# ]

# Create:

# def find_failed_users(events):

# Expected result
# ["shadow", "guest", "shadow"]

# Don't use the file. We're deliberately switching from raw text → structured data.


# def find_failed_users(events):
#     failed_users = []
#     for event in events:
#         if event["status"] == "Failed":
#             failed_users.append(event["username"])
#     return failed_users

# print(find_failed_users(events1))


# 🔥 Exercise 10 — Detect repeated attackers

# Use the same events data.

# Create:

# def find_repeated_failed_users(events):
# Requirements

# Return a dictionary containing only users who failed more than once.

# For the provided data:

# {
#     "shadow": 2
# }

# Do not include:

# "guest": 1

# because guest only failed once.

# Don't hardcode usernames.

# events1 = [
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
# ]


# def find_repeated_failed_users(events):
#     repeated_failed_users = {}
#     for event in events:
#         if event["status"] == "Failed":
#             key = event["username"]
#             if key not in repeated_failed_users:
#                 repeated_failed_users[key] = 1
#             else:
#                 repeated_failed_users[key] += 1
    
    
#     result = {}
#     for username in repeated_failed_users:
#         if repeated_failed_users[username] >= 2:
#             value = repeated_failed_users[username]
#             result.update({username: value}) 

#     return result

# print(find_repeated_failed_users(events1))



# 🔥 Exercise 11 — Mini SOC analysis

# Now combine what you've learned.

# You receive:


# Create:

# def analyze_security_events(events):

# It must return a dictionary containing:

# {
#     "failed_attempts": 5,
#     "failed_users": ["shadow", "guest", "shadow", "ahmed", "shadow"],
#     "repeated_failed_users": {
#         "shadow": 3
#     }
# }

# events1 = [
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
#     {"username": "ahmed", "ip": "172.16.5.15", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
# ]

# # count the failed attemps

# def extract_failed_attempts(events):
#     failed_attempts = 0
#     for event in events:
#         if event["status"] == "Failed":
#             failed_attempts += 1
#     return failed_attempts

# # print(extract_failed_attempts(events1))

# # clock in the failes users

# def extract_failed_users(events):
#     failed_login_users = []
#     for event in events:
#         if event["status"] == "Failed":
#             failed_login_users.append(event["username"])
#     return failed_login_users

# # print(extract_failed_users(events1))

# # clock in the repeated failed users

# def repeated_failed_users(events):
#     # check for users who makes more that one failed attempt
#     failed_users = extract_failed_users(events)
#     # count the failed attempt from that multi failed attempt user
#     temp_user = {}
#     for user in failed_users:
#         if user not in temp_user:
#             temp_user[user] = 1
#         else:
#             temp_user[user] += 1
#     multi_failed_user = {}
#     for user in temp_user:
#         if temp_user[user] >= 2:
#             multi_failed_user.update({user: temp_user[user]})
#             # value = temp_user[user]
#             # multi_failed_user[user: value]

#     return multi_failed_user

# # print(repeated_failed_users(events1))




# # meshh all of this togheter. this is the mistake i made in the privious exercise and made it too difficult for my self. by  not planning this and not making different functions and give it a name and the use it. so i could use that and put it properly in a dict. 

# # {
# #     "failed_attempts": 5,
# #     "failed_users": ["shadow", "guest", "shadow", "ahmed", "shadow"],
# #     "repeated_failed_users": {
# #         "shadow": 3
# #     }
# # }

# # all the info together
# # - first whole dict and in it:
#     # - failed attempt : value
#     # - failed users : list of failed user
#     # - repeated failed users dict of; key : value

# def analyze_security_events(events):
#     failed_attempts = extract_failed_attempts(events)
#     failed_users = extract_failed_users(events)
#     repeated_failed = repeated_failed_users(events)
#     analysis = {
#         "failed_attempts": failed_attempts,
#         "failed_users": failed_users,
#         "repeated_failed_users" : repeated_failed
#     }
#     return analysis

# print(analyze_security_events(events1))


# 🟡 Exercise 12 — Handle a missing file

# Create:

# def read_security_log(file):

# The function receives a filename.

# Requirements
# Try to open the file.
# Read its contents.
# Return the contents.
# If the file doesn't exist, handle that error with try/except.
# The function must not crash.
# If the file doesn't exist, return exactly:
# File not found
# Do not print inside the function.

# Test it with an existing file:
# Then deliberately test a file that doesn't exist:
# One restriction

# Don't use:

# except Exception:



# def read_security_log(file):
#     try:
#         with open(file) as f:
#             reading_log = f.read()
#             return reading_log
#     except FileNotFoundError:
#         return f"The file you are trying access doesn't exist"


# print(read_security_log("file-that-does-not-exist.txt|"))
# print(read_security_log("logs8.txt"))


# 🟡 Exercise 13 — Handle two different file errors

# Create:

# def read_security_log(file):

# The function receives a filename.

# Requirements

# Try to open and read the file.

# Your function must handle two different situations:

# 1. The file doesn't exist

# Return exactly:

# File not found

# 2. The file exists, but you don't have permission to read it

# Return exactly:

# Permission denied

# If neither error occurs, return the contents of the file.

# Restrictions
# Use try/except.
# Use specific exceptions.
# Don't use:
# except Exception:
# Don't print inside the function.


# def read_security_log(file):
#     try:
#         with open(file) as f:
#             content_log = f.read()
#         return content_log
#     except FileNotFoundError:
#         return 'File not found'
#     except PermissionError:
#         return 'Permission denied'

# print(read_security_log('logs8.txt'))

# print(read_security_log('log822.txt'))


# 🔥 Exercise 14 — Defensive log parsing

# Create:

# def extract_failed_users(file):

# The function receives a log file containing lines such as:

# SUCCESS LOGIN user=admin ip=10.0.0.5
# FAILED LOGIN user=shadow ip=192.168.1.20
# FAILED LOGIN ip=172.16.5.10
# FAILED LOGIN user=ahmed ip=172.16.5.15
# SUCCESS LOGIN user=backup ip=10.0.0.8

# Notice that one failed event is malformed:

# FAILED LOGIN ip=172.16.5.10

# It has no user= field.

# Requirements

# Your function must:

# Open the file.
# Process it line by line.
# Only process lines containing:
# FAILED LOGIN
# Extract the username from valid failed-login lines.
# If a failed-login line is missing the username, handle the resulting exception instead of crashing.
# Skip the malformed event and continue processing the remaining lines.
# Return a list containing the valid failed usernames.

# Expected result:

# [
#     "shadow",
#     "ahmed"
# ]

# logs14.txt
# SUCCESS LOGIN user=admin ip=10.0.0.5
# FAILED LOGIN user=shadow ip=192.168.1.20
# FAILED LOGIN ip=172.16.5.10
# FAILED LOGIN user=ahmed ip=172.16.5.15
# SUCCESS LOGIN user=backup ip=10.0.0.8


# def extract_failed_users(file):
#     failed_user = []
#     exceptions = []
#     with open(file) as f:
#         for line in f:
#             if "FAILED LOGIN" in line:
#                 try:
#                     split_line = line.split("user=")
#                     unclean_username = split_line[1]
#                     username = unclean_username.split()[0]
#                     failed_user.append(username)
#                 except IndexError:
#                     exceptions.append(f"This line: {line.strip()} is missing information!")
#     return f"{failed_user}\n{exceptions}"

# print(extract_failed_users("logs14.txt"))

# 🔥 Exercise 15 — Multiple malformed fields

# Create:

# def extract_failed_events(file):

# Your file will contain:

# SUCCESS LOGIN user=admin ip=10.0.0.5
# FAILED LOGIN user=shadow ip=192.168.1.20
# FAILED LOGIN ip=172.16.5.10
# FAILED LOGIN user=ahmed
# FAILED LOGIN user=guest ip=172.16.5.11
# SUCCESS LOGIN user=backup ip=10.0.0.8

# There are two malformed failed-login events:

# FAILED LOGIN ip=172.16.5.10

# is missing user=.

# And:

# FAILED LOGIN user=ahmed

# is missing ip=.

# Requirements

# Your function must:

# Open the file.
# Process it line by line.
# Only process "FAILED LOGIN" events.
# Extract both the username and IP.
# If a failed event is missing either user= or ip=, handle the error.
# Skip the malformed event.
# Continue processing the remaining lines.
# Return a list of dictionaries.

# Expected result:

# [
#     {"username": "shadow", "ip": "192.168.1.20"},
#     {"username": "guest", "ip": "172.16.5.11"}
# ]

# log15.txt





#  Final # get a list of dicts that contains failed login attempt users with their ips = with try except

# component # get username

# def extract_failed_usernames(file):
#     usernames = []
#     errors = []
#     try:
#         with open(file) as f:
#             for line in f:
#                 try:
#                     if "FAILED LOGIN" in line:
#                         split_line_part1 = line.split("user=")[1]
#                         split_line_part2 = split_line_part1.split()[0].strip()
#                         usernames.append(split_line_part2)
#                 except IndexError:
#                     errors.append(f"username not found in line: '{line}'.")  
#     except FileNotFoundError:
#         errors.append("File not found!")
    
#     return usernames
# component # get ip

# def extract_failed_ips(file):
#     ips = []
#     errors = []
#     try:
#         with open(file) as f:
#             for line in f:
#                 try:
#                     if "FAILED LOGIN" in line:
#                         split_line_part1 = line.split("ip=")[1].strip()
#                         ips.append(split_line_part1)
#                 except IndexError:
#                         errors.append(f"ip not found in line: '{line}'.")
#     except FileNotFoundError:
#         errors.append("File not found!")
    
#     return ips

# checking:
    # print(extract_failed_usernames("log15.txt"))
    # print(extract_failed_ips("log15.txt"))


# key1 = username
# key2 = ip 

# oepsie well it seems that i have to mesh it together because if i dont do that then it would be difficult to make sure that th username and ip belongs to each other.

def extract_failed_events(file):
    events = []
    errors = []
    try:
        with open(file) as f:
            for line in f:
                try:
                    
                    
                    if "FAILED LOGIN" in line:
                        split_line_part1 = line.split("ip=")[1].strip()
                        ip = split_line_part1

                        split_line_part1 = line.split("user=")[1]
                        split_line_part2 = split_line_part1.split()[0].strip()
                        usernames = split_line_part2

                        # dict
                        event = {
                            "usernames": usernames,
                            "ip": ip
                        }

                        events.append(event)


                except IndexError:
                        errors.append(f"Data not found in: '{line}'.")
    
    except FileNotFoundError:
        errors.append("File not found!")

    return events


print(extract_failed_events("log15.txt"))



# if i am being honest, i realy was riding blind here, so now i learned if there are multiple condidition that has to be fuffillend in on check, then do it in one if line, and the exception will catch it if any of the condition are not checked. i could i have done elif. or another if. but this felt better i dont know why, but hey i got it after uselessly making 2 whole functions. 

