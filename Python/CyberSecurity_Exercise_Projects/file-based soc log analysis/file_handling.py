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


