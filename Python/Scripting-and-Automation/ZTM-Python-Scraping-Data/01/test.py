# refresshing enumerate 

# Exercise 1 — Beginner: enumerate()

# events = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "LOGIN_FAILED",
#     "LOGIN_SUCCESS"
# ]

# for index, event in enumerate(events):
#     print(index, event)



# Exercise 2 — Intermediate: enumerate() + if

# for index, event in enumerate(events):
#     if "LOGIN_FAILED" in event:
#         print(index, event)

# Exercise 3 — Advanced: understand the (index, object) pair

# users = ["bob", "alice", "admin", "bob"]

# for user in enumerate(users):

#     index, clean_user = user

#     if clean_user == "bob":
#         print(f"{index} {clean_user} -> FOUND")
#     else:
#         print(f"{index} {clean_user} -> NOT FOUND")



# test 1 is 13, test 2 is "age", test 3 is 

# def get_age(users)
#     for user in users:
#         return user["age"]

# test 4. 

# it gives the reverse of the ordered results or not ordered results if possible

# test 5.

events = [
    {"event": "LOGIN", "failed": 5},
    {"event": "LOGIN", "failed": 12},
    {"event": "LOGIN", "failed": 3}
]

def sort_events(events):
    