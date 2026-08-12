# Exercise 5

# events = [
#     {"username": "admin", "status": "Success", "ip": "10.0.0.5"},
#     {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
#     {"username": "guest", "status": "Failed", "ip": "172.16.5.10"}
# ]

# def extract_failed_login_counts(logs):
#     failed_counter = 0
#     for log in logs:
#         if log["status"] == "Failed":
#             failed_counter += 1
#     return failed_counter


# print(extract_failed_login_counts(events)) checked


# # 🟡 Exercise 6

# events1 = [
#     {"username": "admin", "status": "Success", "ip": "10.0.0.5"},
#     {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
#     {"username": "guest", "status": "Failed", "ip": "172.16.5.10"}
# ]

# def extract_failed_ips(events):
#     temp_list = []
#     for event in events:
#         if event["status"] == "Failed":
#             temp_list.append(event["ip"])
#     return temp_list

# print(extract_failed_ips(events1))


# 🔥 Final challenge


events2 = [
    {"username": "admin", "status": "Success", "ip": "10.0.0.5"},
    {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"},
    {"username": "guest", "status": "Failed", "ip": "172.16.5.10"},
    {"username": "backup", "status": "Success", "ip": "10.0.0.8"},
    {"username": "shadow", "status": "Failed", "ip": "192.168.1.20"}
]


# failed attempt

def extract_failed_attempts(events):
    failed_attempts = 0
    for event in events:
        if event["status"] == "Failed":
            failed_attempts += 1
    return f"\nFailed attempts: {failed_attempts}"

# check 

# failed users

def extract_failed_users(events):
    temp_list = []
    for event in events:
        if event["status"] == "Failed":
            temp_list.append(event["username"])
    return f"\nUsers:\n{"\n".join(temp_list)}"

# check dont froget to joinmethod them

# failed ips

def extract_failed_ips(events):
    temp_list = []
    for event in events:
        if event["status"] == "Failed":
            temp_list.append(event["ip"])
    return f"IP's:\n{"\n".join(temp_list)}"

# check dont forget to joinmethod them

# combining and dont forget to name is main and execute the prime function in main()
def failed_events_analysis(events):
    return f"Executing failed login analysis:\n{extract_failed_attempts(events)}\n{extract_failed_users(events)}\n\n{extract_failed_ips(events)}\n\nData extraction done!"

# print(failed_events_analysis(events2))

def main():
    print(failed_events_analysis(events2))
    return failed_events_analysis(events2)


if __name__=="__main__":
    main()


