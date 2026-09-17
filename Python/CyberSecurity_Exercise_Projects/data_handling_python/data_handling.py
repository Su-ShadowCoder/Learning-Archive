
# # ============================================================
# # 🟡 Exercise 20 — Validate security events
# # ============================================================

# # Valid events
# # {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"}
# # {"username": "admin", "ip": "10.0.0.5", "status": "Success"}

# # Requirements

# # Your function must:

# # Return True if the event contains all three required fields:
# # username
# # ip
# # status
# # Only accept these statuses:
# # "Success"
# # "Failed"
# # If a required key is missing, handle the resulting exception with try/except.
# # Use a specific exception.
# # Don't use except Exception.
# # Don't print inside the function.

# # events = [
# #     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
# #     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
# #     {"username": "shadow", "status": "Failed"},
# #     {"username": "", "ip": "192.168.1.20", "status": "Failed"},
# #     {"username": "shadow", "ip": "192.168.1.20"},
# #     {"username": "shadow", "ip": "192.168.1.20", "status": "UNKNOWN"}
# # ]

# # Answer


# # single event validater
# # def validate_security_event(event):
# #     try:
# #         if event["username"] and event["ip"] and event["status"]:
# #             if event['status'] == "Success" or event['status'] == "Failed":
# #                 return True
# #             else:
# #                 return False
# #         else:
# #                     return False

# #     except KeyError:
# #         return False

# # print(validate_security_event(events[0]))
# # print(validate_security_event(events[1]))
# # print(validate_security_event(events[2]))
# # print(validate_security_event(events[3]))
# # print(validate_security_event(events[4]))
# # print(validate_security_event(events[5]))


# # ============================================================
# # 🟡 EXERCISE 21 — Validate a collection of security events
# # ============================================================

# events1 = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.20", "status": "Failed"},
#     {"ip": "172.16.5.10", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8"},
#     {"username": "ahmed", "ip": "172.16.5.15", "status": "UNKNOWN"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.20", "status": "Failed"},
#     {"ip": "172.16.5.10", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8"},
#     {"username": "ahmed", "ip": "172.16.5.15", "status": "UNKNOWN"}
# ]

# # Create:
# # def validate_security_event(event):
# #
# # You already completed this function in Exercise 20.
# # Recreate/reuse it.
# #
# # Create:
# # def separate_valid_events(events):
# #
# # Requirements:
# # - Check every event with validate_security_event()
# # - Put valid events into one list
# # - Put invalid events into another list
# # - Return both lists in a dictionary:
# #
# # {
# #     "valid": [...],
# #     "invalid": [...]
# # }
# #
# # Do not hardcode which events are valid/invalid.
# # Do not print inside the function.

# # Answer

# import pprint

# # # Validate single event
# # def validate_security_event(event):
# #     try:
# #         if event["username"] and event["ip"] and event["status"]:
# #             if event["status"] == "Success" or event["status"] == "Failed":
# #                 return True
# #         return False
# #     except KeyError:
# #         return False


# # # sort the events in two dict list, one in valid and one in invalid
# # def sort_valid_events(events):
# #     valid = []
# #     invalid = []
# #     for event in events:
# #         validated_event = validate_security_event(event)
# #         if validated_event == True:
# #             valid.append(event)
# #         else:
# #             invalid.append(event)
# #     return valid, invalid



# # ============================================================
# # 🔥 EXERCISE 22 — Analyze valid security events
# # ============================================================

# # Use the valid events produced by Exercise 21.
# #
# # Create:
# # def analyze_valid_events(events):
# #
# # Return:
# #
# # {
# #     "total_events": 4,
# #     "failed_events": 3,
# #     "successful_events": 1,
# #     "failed_users": {
# #         "shadow": 1,
# #         "guest": 1,
# #         "..."
# #     }
# # }
# #
# # Requirements:
# # - Count total valid events
# # - Count Failed events
# # - Count Success events
# # - Count how many times each failed username appears
# # - Do not hardcode usernames
# # - Use dictionaries for counting
# #
# # Only analyze events passed into the function.
# # Do not validate them again inside this function.

# # Answer

# # from previous sort valid events method. valid for that method = events for analyze valid events. 

# import pprint
# from functions import validate_security_event, sort_valid_events

# events1 = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.20", "status": "Failed"},
#     {"ip": "172.16.5.10", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8"},
#     {"username": "ahmed", "ip": "172.16.5.15", "status": "UNKNOWN"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.20", "status": "Failed"},
#     {"ip": "172.16.5.10", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8"},
#     {"username": "ahmed", "ip": "172.16.5.15", "status": "UNKNOWN"}
# ]

# # counts the totals events 
# def count_total_events(events):
#     return len(events)

# # Counts all valid events that are Failed events
# def count_failed_events(events):
#     sorted_ev = sort_valid_events(events)
#     return len(sorted_ev[1])


# # Counts all valid events that are Successful events
# def count_success_events(events):
#     sorted_ev = sort_valid_events(events)
#     return len(sorted_ev[0])


# # Represents how many times a failed login user has attempted to attempt. 
# def failed_users_attempts(events):
#     sorted_evs = sort_valid_events(events)
#     valid_evs = sorted_evs[0]
#     failed_attempts = []
#     for event in valid_evs:
#         if event["status"] == "Failed":
#             failed_attempts.append(event)
    
#     # print(failed_attempts)


#     unclean_results = {}
#     for event in failed_attempts:
#         username_value = event["username"]
#         if username_value not in unclean_results:
#             unclean_results[username_value] = 1
#         else:
#             unclean_results[username_value] += 1
#     return unclean_results

# # give complete analysis
# def analyze_valid_events(events):
#     value1 = count_total_events(events)
#     value2 = count_failed_events(events)
#     value3 = count_success_events(events)
#     value4 = failed_users_attempts(events)
    
#     analyze_result = {
#         "total_events": value1,
#         "failed_events": value2,
#         "successful_events": value3,
#         "failed_users": value4
#     }
    
#     return analyze_result


# def main():
#     # pprint.pprint(analyze_valid_events(events1), sort_dicts=False)
#     # print(failed_users_attempts(events1))
#     pass


# if __name__=="__main__":
#     main()



# # ============================================================
# # 🔥 EXERCISE 23 — Detect suspicious users
# # ============================================================



# # Create:
# # def find_suspicious_users(events, threshold):
# #
# # A user is suspicious if they have FAILED more than
# # 'threshold' times.
# #
# # Example:
# #
# # find_suspicious_users(events, 2)
# #
# # Expected:
# #
# # {
# #     "shadow": 3
# # }
# #
# # Requirements:
# # - Only count Failed events
# # - Count failures per username
# # - Return only users whose count is greater than threshold
# # - Do not hardcode usernames
# # - Do not use collections.Counter
# #
# # Test with at least:
# # threshold = 1
# # threshold = 2
# # threshold = 3


# events2 = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "ahmed", "ip": "172.16.5.15", "status": "Failed"},
# ]

# # Answer

# def find_sus_users(events, threshold):

#     failed_events = []
#     for event in events:
#         if event["status"] == "Failed":
#             failed_events.append(event)
#     # print(failed_events)


#     unclean_results = {}
#     for event in failed_events:
#         username_value = event["username"]
#         if username_value not in unclean_results:
#             unclean_results[username_value] = 1
#         else:
#             unclean_results[username_value] += 1
#     # print(unclean_results)


#     results = {}
#     for sus in unclean_results:
#         if unclean_results[sus] >= threshold:
#             results[sus] = unclean_results[sus]
#     return results

# # print(find_sus_users(events2, 3))




# # ============================================================
# # 🔥 EXERCISE 24 — Mini security-event pipeline
# # ============================================================

# events3 = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.30", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
# ]

# # Build:
# # def security_event_report(events):
# #
# # Your function must:
# #
# # 1. Validate every event using validate_security_event()
# # 2. Separate valid and invalid events
# # 3. Analyze the valid events
# # 4. Detect suspicious users
# # 5. Return one final dictionary
# #
# # The final result should contain:
# #
# # {
# #     "total_received": ...,
# #     "valid_events": ...,
# #     "invalid_events": ...,
# #     "failed_attempts": ...,
# #     "successful_attempts": ...,
# #     "failed_users": {...},
# #     "suspicious_users": {...}
# # }
# #

# def failed_attempts(events):
#     result = 0
#     valid_events = sort_valid_events(events)[0]
#     for event in valid_events:
#         if event["status"] == "Failed":
#             result += 1
#     return result



# def successful_attempts(events):
#     result = 0
#     valid_events = sort_valid_events(events)[0]
#     for event in valid_events:
#         if event["status"] == "Success":
#             result += 1
#     return result





# def security_event_report(events, threshold):
# #       "total_received": ...,
#     value1 = count_total_events(events)
# #       "valid_events": ...,
#     value2 = count_success_events(events)
# #       "invalid_events": ...,
#     value3 = count_failed_events(events)
# #       "failed_attempts": ...,
#     value4 = failed_attempts(events)
# #       "successful_attempts": ...,
#     value5 = successful_attempts(events)
# #       "failed_users": {...},
#     value6 = failed_users_attempts(events)
# #       "suspicious_users": {...}
#     sorted_events22 = sort_valid_events(events)[0]
#     # print(sorted_events22)
#     value7 = find_sus_users(sorted_events22, threshold)

#     final_result = {
#         "total_received": value1,
#         "valid_events": value2,
#         "invalid_events": value3,
#         "failed_attempts": value4,
#         "successful_attempts": value5,
#         "failed_users": value6,
#         "suspicious_users": value7
#     }

#     return final_result



# def main():
#     pprint.pprint(security_event_report(events3, 2), sort_dicts=False)
#     # print(failed_users_attempts(events3))
#     pass


# if __name__=="__main__":
#     main()


# # funcitons in the a different file called functions:


# # validates single event
# def validate_security_event(event):
#     try:
#         if event["username"] and event["ip"] and event["status"]:
#             if event['status'] == "Success" or event['status'] == "Failed":
#                 return True
#             else:
#                 return False
#         else:
#                     return False

#     except KeyError:
#         return False


# # sort the events in two dict list, one in valid and one in invalid
# def sort_valid_events(events):

#     valid = []
#     invalid = []
#     for event in events:
#         validated_event = validate_security_event(event)
#         if validated_event == True:
#             valid.append(event)
#         else:
#             invalid.append(event)
#     return valid, invalid


# # counts the totals events 
# def count_total_events(events):
#     return len(events)


# # Counts all valid events that are Failed events
# def count_failed_events(events):
#     sorted_ev = sort_valid_events(events)
#     return len(sorted_ev[1])


# # Counts all valid events that are Successful events
# def count_success_events(events):
#     sorted_ev = sort_valid_events(events)
#     return len(sorted_ev[0])


# events3 = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.30", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
# ]

# # Represents how many times a failed login user has attempted to attempt. 
# def failed_users_attempts(events):
#     sorted_evs = sort_valid_events(events)
#     valid_evs = sorted_evs[0]
#     failed_attempts = []
#     for event in valid_evs:
#         if event["status"] == "Failed":
#             failed_attempts.append(event)

#     unclean_results = {}
#     for event in failed_attempts:
#         username_value = event["username"]
#         if username_value not in unclean_results:
#             unclean_results[username_value] = 1
#         else:
#             unclean_results[username_value] += 1
#     return unclean_results


# # give complete analysis
# def analyze_valid_events(events):

#     value1 = count_total_events(events)
#     value2 = count_failed_events(events)
#     value3 = count_success_events(events)
#     value4 = failed_users_attempts(events)
    
#     analyze_result = {
#         "total_events": value1,
#         "failed_events": value2,
#         "successful_events": value3,
#         "failed_users": value4
#     }
    
#     return analyze_result


# # find suspisious users in events with a threshold
# def find_sus_users(events, threshold):
#     failed_events = []
#     for event in events:
#         if event["status"] == "Failed":
#             failed_events.append(event)
#     # print(failed_events)


#     unclean_results = {}
#     for event in failed_events:
#         username_value = event["username"]
#         if username_value not in unclean_results:
#             unclean_results[username_value] = 1
#         else:
#             unclean_results[username_value] += 1
#     # print(unclean_results)


#     results = {}
#     for sus in unclean_results:
#         if unclean_results[sus] >= threshold:
#             results[sus] = unclean_results[sus]
#     return results

##########################################################################

# ============================================================
# 🔥 EXERCISE 25 — Security Event Pipeline Checkpoint
# ============================================================

# ------------------------------------------------------------
# Create:
#
# def security_event_summary(events):
#
# ------------------------------------------------------------

# Requirements:
#
# 1. Validate every event.
#
# 2. Invalid events must NOT be included in the analysis.
#
# 3. Produce a dictionary containing:
#
# {
#     "total_received": ...,
#     "valid_events": ...,
#     "invalid_events": ...,
#     "failed_attempts": ...,
#     "successful_attempts": ...,
#     "failed_users": {...},
#     "failed_ips": {...},
#     "suspicious_users": {...}
# }
#
#

import pprint

events1 = [
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "shadow", "status": "Failed"},
    {"username": "ahmed", "ip": "172.16.5.15", "status": "Failed"},
    {"username": "", "ip": "172.16.5.20", "status": "Failed"},
    {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "root", "ip": "10.0.0.10", "status": "UNKNOWN"},
]

# i would like to tell you that i am making all the function again because i want to make sure that i can make al the functions again, as i am doing this exercise after a couple days. today is 1 sept. 


#     "total_received": ...,
def total_events_received(events):
    return len(events)

# print(total_events_received(events1))

#     "valid_events": ...,
#     "invalid_events": ...,

def validating_event(event):
    state = None
    try:
        if event["username"] and event["ip"] and event["status"]:
            if event["status"] == "Failed" or event["status"] == "Success":
                state = True
            else:
                state = False
        else:
            state = False
    except KeyError:
        state = False
    return state

def sort_validated_events(events):
    valid_event = []
    invalid_event = []

    for event in events:
        if validating_event(event):
            valid_event.append(event)
        else:
            invalid_event.append(event)
    
    return valid_event, invalid_event

# pprint.pprint(sort_validated_events(events1), sort_dicts=False)

# return # "failed_attempts": ..., , # "successful_attempts": ...,
def result_attempt_counts(events):
    valid_events = sort_validated_events(events)[0]
    fail_count = 0
    success_count = 0
    for event in valid_events:
        if event["status"] == "Failed":
            fail_count += 1
        else:
            success_count += 1

    return fail_count, success_count

# print(result_attempt_counts(events1))



# failed users attempts
def failed_users_attempts(events):
    valid_events = sort_validated_events(events)[0]
    failed_users = {}

    for event in valid_events:
        if event["status"] == "Failed":
            username_value = event['username']
            if username_value not in failed_users:
                failed_users[username_value] = 1
            else:
                failed_users[username_value] += 1
    return failed_users

# pprint.pprint(failed_users_attempts(events1))


#failed ips attempts
def failed_ips_attempts(events):
    valid_event = sort_validated_events(events)[0]
    f_ips_attempts = {}
    for event in valid_event:
        if event['status'] == 'Failed':
            f_ip_value = event['ip']
            if f_ip_value not in f_ips_attempts:
                f_ips_attempts[f_ip_value] = 1
            else:
                f_ips_attempts[f_ip_value] += 1 
    return f_ips_attempts

# pprint.pprint(failed_ips_attempts(events1))

#     "suspicious_users": {...}
def find_suspicious_users(events, threshold_n):
    temp_events = failed_users_attempts(events)
    sussy_baka = {}
    for k, v in temp_events.items():
        if v > threshold_n :
            sussy_baka[k] = v

    return sussy_baka

# print(find_suspicious_users(events1, 2))




def security_analysis_report(events):
    report = {
    "total_received": total_events_received(events),
    "valid_events": sort_validated_events(events)[0],
    "invalid_events": sort_validated_events(events)[1],
    "failed_attempts": result_attempt_counts(events)[0],
    "successful_attempts": result_attempt_counts(events)[1],
    "failed_users": failed_users_attempts(events),
    "failed_ips": failed_ips_attempts(events),
    "suspicious_users": find_suspicious_users(events, 2)
    }

    return report



def main():
    pprint.pprint(security_analysis_report(events1), sort_dicts=False)


if __name__=="__main__":
    main()


# give me evaluation like am i done witht he whole thing, i do had to search up and ask an ai about the whole k, v in dicts.items(): part, are sure i am done compleytely?