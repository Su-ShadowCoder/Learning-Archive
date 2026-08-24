
# ============================================================
# 🟡 Exercise 20 — Validate security events
# ============================================================

# Valid events
# {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"}
# {"username": "admin", "ip": "10.0.0.5", "status": "Success"}

# Requirements

# Your function must:

# Return True if the event contains all three required fields:
# username
# ip
# status
# Only accept these statuses:
# "Success"
# "Failed"
# If a required key is missing, handle the resulting exception with try/except.
# Use a specific exception.
# Don't use except Exception.
# Don't print inside the function.

# events = [
#     {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
#     {"username": "shadow", "status": "Failed"},
#     {"username": "", "ip": "192.168.1.20", "status": "Failed"},
#     {"username": "shadow", "ip": "192.168.1.20"},
#     {"username": "shadow", "ip": "192.168.1.20", "status": "UNKNOWN"}
# ]

# Answer


# single event validater
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

# print(validate_security_event(events[0]))
# print(validate_security_event(events[1]))
# print(validate_security_event(events[2]))
# print(validate_security_event(events[3]))
# print(validate_security_event(events[4]))
# print(validate_security_event(events[5]))


# ============================================================
# 🟡 EXERCISE 21 — Validate a collection of security events
# ============================================================

events1 = [
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
    {"username": "shadow", "status": "Failed"},
    {"username": "", "ip": "192.168.1.20", "status": "Failed"},
    {"ip": "172.16.5.10", "status": "Failed"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "backup", "ip": "10.0.0.8"},
    {"username": "ahmed", "ip": "172.16.5.15", "status": "UNKNOWN"},
]

# Create:
# def validate_security_event(event):
#
# You already completed this function in Exercise 20.
# Recreate/reuse it.
#
# Create:
# def separate_valid_events(events):
#
# Requirements:
# - Check every event with validate_security_event()
# - Put valid events into one list
# - Put invalid events into another list
# - Return both lists in a dictionary:
#
# {
#     "valid": [...],
#     "invalid": [...]
# }
#
# Do not hardcode which events are valid/invalid.
# Do not print inside the function.

# Answer

import pprint

# Validate single event
def validate_security_event(event):
    try:
        if event["username"] and event["ip"] and event["status"]:
            if event["status"] == "Success" or event["status"] == "Failed":
                return True
        return False
    except KeyError:
        return False




# sort the events in two dict list, one in valid and one in invalid
def sort_valid_events(events):
    valid = []
    invalid = []
    for event in events:
        validated_event = validate_security_event(event)
        if validated_event == True:
            valid.append(event)
        else:
            invalid.append(event)
    return valid, invalid



pprint.pprint(sort_valid_events(events1))




# ============================================================
# 🔥 EXERCISE 22 — Analyze valid security events
# ============================================================

# Use the valid events produced by Exercise 21.
#
# Create:
# def analyze_valid_events(events):
#
# Return:
#
# {
#     "total_events": 4,
#     "failed_events": 3,
#     "successful_events": 1,
#     "failed_users": {
#         "shadow": 1,
#         "guest": 1,
#         "..."
#     }
# }
#
# Requirements:
# - Count total valid events
# - Count Failed events
# - Count Success events
# - Count how many times each failed username appears
# - Do not hardcode usernames
# - Use dictionaries for counting
#
# Only analyze events passed into the function.
# Do not validate them again inside this function.

# Answer

# ============================================================
# 🔥 EXERCISE 23 — Detect suspicious users
# ============================================================

events = [
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "ahmed", "ip": "172.16.5.15", "status": "Failed"},
]

# Create:
# def find_suspicious_users(events, threshold):
#
# A user is suspicious if they have FAILED more than
# 'threshold' times.
#
# Example:
#
# find_suspicious_users(events, 2)
#
# Expected:
#
# {
#     "shadow": 3
# }
#
# Requirements:
# - Only count Failed events
# - Count failures per username
# - Return only users whose count is greater than threshold
# - Do not hardcode usernames
# - Do not use collections.Counter
#
# Test with at least:
# threshold = 1
# threshold = 2
# threshold = 3

# Answer

# ============================================================
# 🔥 EXERCISE 24 — Mini security-event pipeline
# ============================================================

events = [
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
    {"username": "shadow", "status": "Failed"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "", "ip": "192.168.1.30", "status": "Failed"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
]

# Build:
# def security_event_report(events):
#
# Your function must:
#
# 1. Validate every event using validate_security_event()
# 2. Separate valid and invalid events
# 3. Analyze the valid events
# 4. Detect suspicious users
# 5. Return one final dictionary
#
# The final result should contain:
#
# {
#     "total_received": ...,
#     "valid_events": ...,
#     "invalid_events": ...,
#     "failed_attempts": ...,
#     "successful_attempts": ...,
#     "failed_users": {...},
#     "suspicious_users": {...}
# }
#
# Use a threshold of 2 for suspicious users.
#
# IMPORTANT:
# Reuse your previous functions.
# Do NOT put all the logic into one giant function.
# Do NOT hardcode usernames, counts, or IPs.
# Do NOT print inside your functions.
#
# The final function should RETURN the report.
#
# Print the final returned dictionary outside the function.

# Answer
