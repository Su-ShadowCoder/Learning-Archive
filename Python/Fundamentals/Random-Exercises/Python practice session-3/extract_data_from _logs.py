# 🟡 Exercise 1 — Extract information

# You receive:

# log = "FAILED LOGIN user=ahmed ip=10.0.0.15"

# Create:

# def extract_username(log):

# It should return:

# ahmed

# Then print the result.

# No hints. Decide yourself which string method(s) you need.


# log1 = "FAILED LOGIN user=ahmed ip=10.0.0.15"


# def extract_username(log):
#     #first make list to put the splitted string
#     #then split the string, dont specify it. so you get every spaced substring element. then you specify behind which element you want
#     # then you strip that user=.
#     # and return that stuff
#     # never mind that is for if there are mutliple logs which is not the case. 
#     unclean_username = log.split()[2]
#     username = unclean_username.strip("user=")
#     return username

# print(extract_username(log1))






# 🟡 Exercise 2 — Find failed users

# You receive:

# logs = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=ahmed",
#     "SUCCESS LOGIN user=backup",
#     "FAILED LOGIN user=shadow"
# ]

# Create:

# def failed_users(logs):

# Return:

# ["shadow", "ahmed", "shadow"]

# Then print the result.

# Again, you decide the algorithm.



# logs1 = [
#     "SUCCESS LOGIN user=admin",
#     "FAILED LOGIN user=shadow",
#     "FAILED LOGIN user=ahmed",
#     "SUCCESS LOGIN user=backup",
#     "FAILED LOGIN user=shadow"
# ]



# def extract_failed_user_logins(logs):
#     failed_username_list = []
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             unclean_username = log.split("user=")
#             failed_username_list.append(unclean_username[1])
#     return failed_username_list

# print(extract_failed_user_logins(logs1))




# 🟡 Exercise 3 — Count them

# Using the same logs, create:

# def count_failed(logs):

# Return:

# 3

# Don't print inside the function.




# def extract_failed_counter_data(logs):
#     fail_counter = 0
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             fail_counter += 1
#     return fail_counter

# print(extract_failed_counter_data(logs1))






# 🔥 Exercise 4 — Slightly harder

# Now you receive:

# logs = [
#     "SUCCESS LOGIN user=admin ip=10.0.0.5",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=ahmed ip=172.16.5.10",
#     "SUCCESS LOGIN user=backup ip=10.0.0.8",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=guest ip=172.16.5.15"
# ]

# Write:

# def failed_login_ips(logs):

# It should return:

# [
#     "192.168.1.20",
#     "172.16.5.10",
#     "192.168.1.20",
#     "172.16.5.15"
# ]
# Important

# Don't worry about making it elegant.

# I want to see your reasoning, even if your solution is clunky.


# logs4 = [
#     "SUCCESS LOGIN user=admin ip=10.0.0.5",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=ahmed ip=172.16.5.10",
#     "SUCCESS LOGIN user=backup ip=10.0.0.8",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=guest ip=172.16.5.15"
# ]


# def extract_failed_login_ips(logs):
#     failed_ip_list = []
#     for log in logs:
#         if "FAILED LOGIN" in log:
#             failed_ip_list.append(log.split()[3])
#     return failed_ip_list

# print(extract_failed_login_ips(logs4))




# 🎯 Final challenge — You decide the structure

# You receive:

# logs = [
#     "SUCCESS LOGIN user=admin ip=10.0.0.5",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=ahmed ip=172.16.5.10",
#     "SUCCESS LOGIN user=backup ip=10.0.0.8",
#     "FAILED LOGIN user=shadow ip=192.168.1.20",
#     "FAILED LOGIN user=guest ip=172.16.5.15"
# ]

# Write a program that produces:

# Failed attempts: 4

# Failed users:
# shadow
# ahmed
# shadow
# guest

# Failed IPs:
# 192.168.1.20
# 172.16.5.10
# 192.168.1.20
# 172.16.5.15

# Restriction: Don't make one giant function.

logs5 = [
    "SUCCESS LOGIN user=admin ip=10.0.0.5",
    "FAILED LOGIN user=shadow ip=192.168.1.20",
    "FAILED LOGIN user=ahmed ip=172.16.5.10",
    "SUCCESS LOGIN user=backup ip=10.0.0.8",
    "FAILED LOGIN user=shadow ip=192.168.1.20",
    "FAILED LOGIN user=guest ip=172.16.5.15"
]

def extract_failed_attempts(logs):
    failed_counter = 0
    for log in logs:
        if "FAILED LOGIN" in log:
            failed_counter += 1
    return failed_counter

# print(extract_failed_attempts(logs5)) checked

def extract_failed_login_users(logs):
    temp_list = []
    for log in logs:
        if "FAILED LOGIN" in log:
            temp_list.append(log.split("user=")[1])
    username = []
    for line in temp_list:
        username.append(line.split()[0])
    return "\n".join(username)

# print(extract_failed_login_users(logs5)) checked

def extract_Failed_ips(logs):
    pass
    failed_ip_list = []
    for log in logs:
        if "FAILED LOGIN" in log:
            failed_ip_list.append(log.split("ip=")[1])
    return "\n".join(failed_ip_list)

# print(extract_Failed_ips(logs5)) checked

def final_logs_analysis(logs):
    return f"Welcome to the super Log Analysator!\n\nFailed attempts:\n{extract_failed_attempts(logs)}\n\nFailed users:\n{extract_failed_login_users(logs)}\n\nFailed IPs:\n{extract_Failed_ips(logs)}"

# print(final_logs_analysis(logs5)) checked


def main():
    print(final_logs_analysis(logs5))



if __name__== "__main__":
    main()

