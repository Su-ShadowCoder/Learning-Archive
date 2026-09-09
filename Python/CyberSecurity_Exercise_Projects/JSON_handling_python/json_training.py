# # Exercise 1 — json.dumps()
# # import json

# # event1 = {
# #     "username": "shadow",
# #     "ip": "192.168.1.20",
# #     "status": "Failed"
# # }

# # # # Convert the Python dictionary into JSON.
# # # # Store the result in a variable called json_event.
# # import json


# # json_event1 = json.dumps(event1)

# # # print(json_event1)
# # # print(type(json_event1))

# # # should this not be a object because a object is a dict right and this is a dict.

# # event_f = json.loads(json_event1)

# # print(event_f)
# # print(type(event_f))

# # # print(json_event)
# # print(type(json_event))
# # Goal

# # You should discover that the resulting type is:

# # <class 'str'>

# # That's important.

# # You took:

# # Python dict
# #     ↓
# # json.dumps()
# #     ↓
# # JSON string









# # Exercise 2 — json.loads()

# # Now go the other direction.

# # import json

# # event2 = {
# #     "username": "shadow",
# #     "ip": "192.168.1.20",
# #     "status": "Failed"}


# # # # Convert the JSON string into a Python object.
# # # # Store it in a variable called event.

# # # # YOUR CODE HERE


# # # print(event)
# # # print(type(event))
# # # print(event["username"])

# # # You should end up with a Python dict.

# # # So:

# # # JSON string
# # #     ↓
# # # json.loads()
# # #     ↓
# # # Python dict

# # import json

# # j_event2 = json.dumps(event2)

# # print(j_event2)
# # print(type(j_event2))

# # p_dict1 = json.loads(j_event2)

# # print(type(p_dict1))


# # Exercise 3 — Understand loads vs dumps

# # Don't write code yet.

# # Tell yourself what each one does:

# # json.dumps()

# # versus:

# # json.loads()

# # The names are intentionally related:

# # dump → put Python data into JSON

# # load → bring JSON data into Python

# # And the s means string.

# # So:

# # json.dumps()

# # = dump to string

# # json.loads()

# # = load from string






# # Exercise 4 — Security Events

# # Now we're getting closer to your SOC work.

# # import json

# events = [
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "admin",
#         "ip": "10.0.0.5",
#         "status": "Success"
#     },
#     {
#         "username": "guest",
#         "ip": "172.16.5.10",
#         "status": "Failed"
#     }
# ]

# import json

# j_events3 = []
# for event in events:
#     j_events3.append(json.dumps(event))

# print(j_events3)
# print(type(j_events3[0]))
# print(type(j_events3))






# Exercise 5 — JSON back to Python

# Continue from the previous exercise:

# # Take json_events and convert it back into Python.

# # YOUR CODE HERE


# print(events_again)
# print(type(events_again))

# for event in events_again:
#     print(event["username"], event["status"])

# You should be able to recover the original Python structure.



# events1 = [
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "admin",
#         "ip": "10.0.0.5",
#         "status": "Success"
#     },
#     {
#         "username": "guest",
#         "ip": "172.16.5.10",
#         "status": "Failed"
#     }
# ]

# import json

# json_s_events1 = json.dumps(events1)

# events1_j1 = json.loads(json_s_events1)

# # print(type(events1_j1))
# # print(events1_j1)


# for event in events1_j1:
#     print(event["username"], event["status"])





# # Exercise 6 — JSON Data Types

# # This one is important.

# # import json

# security_data = '''{
#     "username": "shadow",
#     "failed_attempts": 5,
#     "account_locked": true,
#     "ip_addresses": ["192.168.1.20", "10.0.0.15"],
#     "last_login": null
# }
# '''


# # # Load the JSON into Python.

# import json

# secdata1_j2p = json.loads(security_data)

# print(secdata1_j2p)



# # print(type(data["username"]))
# # print(type(data["failed_attempts"]))
# # print(type(data["account_locked"]))
# # print(type(data["ip_addresses"]))
# # print(type(data["last_login"]))

# # Before running it, predict the five Python types.


# # string 
# # int
# # boolean
# # list
# # NONE





# Exercise 7 — Access Nested JSON

# Now we're moving into the type of structures you'll actually see in APIs/logging systems.

# import json

# security_data = '''
# {
#     "event_id": 1001,
#     "source": {
#         "username": "shadow",
#         "ip": "192.168.1.20"
#     },
#     "authentication": {
#         "status": "Failed",
#         "method": "password"
#     }
# }
# '''

# # # Load the JSON.

# # # YOUR CODE HERE


# # # Print:
# # # shadow
# # # 192.168.1.20
# # # Failed
# # # password


# import json

# secdata1_j2p = json.loads(security_data)

# # print(secdata1_j2p)


# print(secdata1_j2p["source"]["username"])
# print(secdata1_j2p['source']['ip'])
# print(secdata1_j2p['authentication']['status'])
# print(secdata1_j2p['authentication']['method'])







# # YOUR CODE HERE

# Think carefully about the structure.

# You have:

# data
#  ├── event_id
#  ├── source
#  │    ├── username
#  │    └── ip
#  └── authentication
#       ├── status
#       └── method





# Exercise 8 — JSON + Your Functions

# This is where we start connecting today's material to Exercise 25.

# import json

# json_events = '''
# [
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "admin",
#         "ip": "10.0.0.5",
#         "status": "Success"
#     },
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     }
# ]
# '''

# # Step 1:
# # Convert json_events into Python data.


# # Step 2:
# # Create a function that receives the Python events.



# import json

# json_events1 = '''
# [
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "admin",
#         "ip": "10.0.0.5",
#         "status": "Success"
#     },
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     }
# ]
# '''

# events1_j2p = json.loads(json_events1)
# # print(events1_j2p)

# def check_failed_events(events):
#     failed_events = []
#     for event in events:
#         if event['status'] == "Failed":
#             failed_events.append(event)
#     failed_attempts = len(failed_events)
#     return failed_events, failed_attempts


# def main():
#     print(check_failed_events(events1_j2p)[0])
#     print(check_failed_events(events1_j2p)[1])

# if __name__=='__main__':
#     main()

# # Step 3:
# # Call your function and print the result.

# # YOUR CODE HERE

# Expected result:

# 2


# Exercise 9 — JSON → Python → Analysis

# Now combine the concepts.

# import json

# json_events = '''
# [
#     {"username": "shadow", "status": "Failed"},
#     {"username": "admin", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "guest", "status": "Failed"},
#     {"username": "backup", "status": "Success"}
# ]
# '''

# # Convert JSON into Python.
# # YOUR CODE HERE


# # Create a function that counts failed attempts per user.
# #
# # Expected:
# #
# # {
# #     "shadow": 2,
# #     "guest": 1
# # }


# def failed_users(events):

#     failed = {}

#     # YOUR CODE HERE

#     return failed


# # Call the function.
# # YOUR CODE HERE

# This exercise should feel very familiar because you're reusing the dictionary-counting logic from Exercise 25.

# That's intentional.

# json_events1 = '''
# [
#     {"username": "shadow", "status": "Failed"},
#     {"username": "admin", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "guest", "status": "Failed"},
#     {"username": "backup", "status": "Success"}
# ]
# '''

# import json

# eventdata1_j2p = json.loads(json_events1)

# # print(eventdata1_j2p)

# # get {username: attempts, etc}
# def extract_usernames_attempts(events):
#     all_failed_events = []
#     failed_usernames_attempts = {}

#     # all failed events
#     for event in eventdata1_j2p:
#         if event['status'] == "Failed":
#             all_failed_events.append(event)
    
#     # failed usernames attempts
#     for event in all_failed_events:
#         key = event['username']
#         if key not in failed_usernames_attempts:
#             failed_usernames_attempts[key] = 1
#         else:
#             failed_usernames_attempts[key] += 1

#     return failed_usernames_attempts

# def main():
#     print(extract_usernames_attempts(eventdata1_j2p))


# if __name__=="__main__":
#     main()








# 🔥 Exercise 10 — Mini SOC JSON Challenge

# Don't do this one until you've attempted the previous exercises.

# import json
# import pprint


# # 7. Create a function that finds suspicious users.
# #
# #    A suspicious user is someone with MORE THAN
# #    2 failed attempts.


# # 8. Create a final report dictionary containing:
# #
# #    "total_events"
# #    "failed_attempts"
# #    "successful_attempts"
# #    "failed_users"
# #    "failed_ips"
# #    "suspicious_users"


# # 9. Pretty-print the final report.


# Expected conceptual result

# Don't use this as a solution while doing it, but your final report should represent: holey what a contradiction, if i dont use this a solution then what example do i know what you want, the you should have made just requirment what you want. 

# total_events       → 6
# failed_attempts    → 4
# successful_attempts → 2

# failed_users:
#     shadow → 3
#     guest  → 1

# failed_ips:
#     192.168.1.20 → 3
#     172.16.5.10  → 1

# suspicious_users:
#  shadow → 3

# JSON is a standardized text format for representing structured data so that different programs can store and exchange it.

# import pprint
# import json

# security_log = '''
# [
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "admin",
#         "ip": "10.0.0.5",
#         "status": "Success"
#     },
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "guest",
#         "ip": "172.16.5.10",
#         "status": "Failed"
#     },
#     {
#         "username": "shadow",
#         "ip": "192.168.1.20",
#         "status": "Failed"
#     },
#     {
#         "username": "backup",
#         "ip": "10.0.0.8",
#         "status": "Success"
#     }
# ]
# '''

# ## converting json to python
# eventdata1_j2p = json.loads(security_log)
# # print(eventdata1_j2p)

# # #    "total_events"
# def total_events(events):
#     return len(events)
# # print(total_events(eventdata1_j2p))

# # #    "failed_attempts"
# def failed_attempts(events):
#     failed_counts = 0
#     for event in events:
#         if event["status"] == "Failed":
#             failed_counts += 1
#     return failed_counts
# # print(failed_attempts(eventdata1_j2p))

# # #    "successful_attempts"
# def successful_attempts(events):
#     success_attempts = 0
#     for event in events:
#         if event['status'] == 'Success':
#             success_attempts += 1
#     return success_attempts
# # print(successful_attempts(eventdata1_j2p))

# # #    "failed_users"
# def failed_users(events):
#     failed_user_attempts = {}
#     for event in events:
#         if event['status'] == 'Failed':
#             username_value = event['username']
#             if username_value not in failed_user_attempts:
#                 failed_user_attempts[username_value] = 1
#             else:
#                 failed_user_attempts[username_value] += 1
#     return failed_user_attempts
# # print(failed_users(eventdata1_j2p))

# # #    "failed_ips"
# def failed_ips(events):
#     failed_ips_attempts = {}
#     for event in events:
#         if event['status'] == 'Failed':
#             ip_value = event['ip']
#             if ip_value not in failed_ips_attempts:
#                 failed_ips_attempts[ip_value] = 1
#             else:
#                 failed_ips_attempts[ip_value] += 1
#     return failed_ips_attempts
# # print(failed_ips(eventdata1_j2p))

# # #    "suspicious_users"
# def suspicious_users(events):
#     failed_attempt_user = {}
#     for event in events:
#         if event['status'] == "Failed":
#             user_value = event['username']
#             if user_value not in failed_attempt_user:
#                 failed_attempt_user[user_value] = 1
#             else:
#                 failed_attempt_user[user_value] += 1
    
#     sus_user_result = {}
#     for key, value in failed_attempt_user.items():
#         if value > 2:
#             sus_user_result[key] = value
    
#     return sus_user_result
# # print(suspicious_users(eventdata1_j2p))

# ## 'final report' 
# def full_report(events):
#     value1 = total_events(events)
#     value2 = failed_attempts(events)
#     value3 = successful_attempts(events)
#     value4 = failed_users(events)
#     value5 = failed_ips(events)
#     value6 = suspicious_users(events)

#     result = {
#         "total_events": value1,
#         "failed_attempts": value2,
#         "successful_attempts": value3,
#         "failed_users": value4,
#         "failed_ips": value5,
#         "suspicious_users": value6
#     }

#     return result



# def main():
#     pprint.pprint(full_report(eventdata1_j2p), sort_dicts=False)


# if __name__=='__main__':
#     main()


# # you should have mad it clear that the stuf you wanted to represent was not exactly how it is you have represented i was stuf without the whole pprint doing what you wanted. also , you havent specified to check for invalid events, so i dint use try except, also another one is that i kept using the same code for a certain part i could have done it with another def and using that def for the rest of the funcitons. 

# # also  today did things from exercise 7 to everthing else

