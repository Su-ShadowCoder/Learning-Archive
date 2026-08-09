# exercise 1

# events1 = [
#     {"username": "admin", "status": "Success"},
#     {"username": "shadow", "status": "Success"},
#     {"username": "guest", "status": "Failed"},
#     {"username": "backup", "status": "Failed"}
# ]

# def find_first_failed(events):
#     failed_result = []
#     success_result = []
#     for event in events:
#         if event['status'] == "Failed":
#             return event["username"]
            
#     return "No failed logins"


# print(find_first_failed(events1))



# exercise 2
# files = [
#     "report.pdf",
#     "photo.jpg",
#     "notes.txt",
#     "malware.exe",
#     "backup.zip"
# ]


# def contains_executable(files0):
#     for file in files0:
#         if file.endswith(".exe"):
#             return True
#     return False

# check_files = contains_executable(files)

# print(check_files)

# safe_files = [
#     "report.pdf",
#     "photo.jpg",
#     "notes.txt"
# ]

# check_safe_files = contains_executable(safe_files)
# print(check_safe_files)

# exercise 3

events = [
    {"username": "admin", "status": "Success"},
    {"username": "shadow", "status": "Failed"},
    {"username": "guest", "status": "Failed"},
    {"username": "backup", "status": "Success"}
]

def count_failed(events0):
    fail_count = 0
    for event in events0:
        if event['status'] == "Failed":
            fail_count += 1
    return fail_count

check_events_failcount = count_failed(events)

print(check_events_failcount)

