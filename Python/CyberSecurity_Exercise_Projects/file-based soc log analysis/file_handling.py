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

def count_failed_users(file):
    dict_failed_users = {}
    with open(file) as f:
        for line in f:
            if "FAILED" in line:
                key = line.split("user=")[1].strip("\n")
                if key not in dict_failed_users:
                    dict_failed_users[key] = 1
                else:
                    dict_failed_users[key] += 1
    return dict_failed_users



print(count_failed_users("login_logs.txt"))
