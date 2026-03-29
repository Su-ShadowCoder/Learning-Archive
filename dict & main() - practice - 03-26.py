# ==========================================
# DICTIONARY PRACTICE — Beginner → Intermediate
# ==========================================

# ------------------------------------------
# EXERCISE 1 — Create and read values
# ------------------------------------------
# def main():
#     user = {
#         "name": "abdullah",
#         "age": 30,
#         "city": "Amsterdam"
#     }

#     print(user["name"])
#     print(user["age"])
#     print(user["city"])

# if __name__ == "__main__":
#     main()

# TASK:
# - Add "city"
# - Print "city"


# # ------------------------------------------
# # EXERCISE 2 — Add new key
# # ------------------------------------------
# def main():
#     user = {
#         "name": "abdullah",
#         "country": None
#     }

#     user["age"] = 20

#     # print(user)
#     print(user["country"])

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add "country"
# # - Print only "country"


# # ------------------------------------------
# # EXERCISE 3 — Update value
# # ------------------------------------------
def main():
    user = {
        "name": "abdullah",
        "age": 20
    }

    user["age"] = 21

    print(user)





if __name__ == "__main__":
    main()

# TASK:
# - Change "name" instead of "age"


# # ------------------------------------------
# # EXERCISE 4 — Check if key exists
# # ------------------------------------------
# def main():
#     user = {
#         "name": "abdullah",
#         "age": 20
#     }

#     key = input("Enter key: ")

#     if key in user:
#         print("Found:", user[key])
#     else:
#         print("Not found")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Test: name, age, city


# # ------------------------------------------
# # EXERCISE 5 — Default value logic
# # ------------------------------------------
# def main():
#     user = {
#         "name": "abdullah"
#     }

#     key = input("Enter key: ")

#     if key in user:
#         print(user[key])
#     else:
#         print("Default: unknown")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add more keys
# # - Try missing keys


# # ------------------------------------------
# # EXERCISE 6 — Counting values
# # ------------------------------------------
# def main():
#     logs = {
#         "INFO": 3,
#         "ERROR": 1,
#         "WARNING": 2
#     }

#     logs["ERROR"] += 1

#     print(logs)

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Increase "INFO" twice
# # - Print only "ERROR"


# # ------------------------------------------
# # EXERCISE 7 — Simple login system
# # ------------------------------------------
# def main():
#     users = {
#         "abdullah": "python123",
#         "alice": "abc123"
#     }

#     username = input("Username: ")
#     password = input("Password: ")

#     if username in users and users[username] == password:
#         print("Access granted")
#     else:
#         print("Access denied")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add a new user
# # - Test correct and incorrect login


# # ------------------------------------------
# # EXERCISE 8 — Attempt counter per user
# # ------------------------------------------
# def main():
#     users = {
#         "abdullah": "python123",
#         "alice": "abc123"
#     }

#     attempts = {
#         "abdullah": 0,
#         "alice": 0
#     }

#     username = input("Username: ")

#     if username in users:
#         attempts[username] += 1
#         print("Attempts:", attempts[username])

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Run multiple times
# # - Observe attempt counter increase per user


# # ///////////////////////////////////////////////////////////////////////
# # ================================
# # DICTIONARY PRACTICE (WITH main())
# # ================================


# # --------------------------------
# # EXERCISE 1 — Basic dictionary in main
# # --------------------------------
# def main():
#     user = {
#         "name": "abdullah",
#         "age": 20
#     }

#     print(user["name"])
#     print(user["age"])

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add a new key: "country"
# # - Print it inside main()


# # --------------------------------
# # EXERCISE 2 — User lookup
# # --------------------------------
# def main():
#     users = {
#         "abdullah": "python123",
#         "alice": "abc123"
#     }

#     username = input("Enter username: ")

#     if username in users:
#         print("User exists")
#     else:
#         print("User not found")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Try different usernames
# # - Add a third user to the dictionary


# # --------------------------------
# # EXERCISE 3 — Get value from dictionary
# # --------------------------------
# def main():
#     users = {
#         "abdullah": "python123",
#         "alice": "abc123"
#     }

#     username = input("Enter username: ")

#     if username in users:
#         print("Password is:", users[username])
#     else:
#         print("User not found")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add more users
# # - Try valid and invalid usernames


# # --------------------------------
# # EXERCISE 4 — Update dictionary value
# # --------------------------------
# def main():
#     users = {
#         "abdullah": "python123",
#         "alice": "abc123"
#     }

#     users["alice"] = "newpass999"

#     print(users)

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Change abdullah's password instead
# # - Print only abdullah’s password


# # --------------------------------
# # EXERCISE 5 — Simple attempt counter per user
# # --------------------------------
# def main():
#     users = {
#         "abdullah": "python123",
#         "alice": "abc123"
#     }

#     attempts = {
#         "abdullah": 0,
#         "alice": 0
#     }

#     username = input("Enter username: ")

#     if username in users:
#         print("User found")

#         attempts[username] += 1
#         print("Attempts:", attempts[username])
#     else:
#         print("User not found")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Run multiple times and watch attempt count increase
# # - Add a new user and extend both dictionaries


# # ////////////////////////////////////////////////////////////////////


# # ////////////////////////////////////////////////////////////////////
# # ================================
# # MAIN() SIMPLE PRACTICE EXERCISES
# # ================================

# # --------------------------------
# # EXERCISE 1 — Basic main()
# # --------------------------------
# def main():
#     print("Hello from main")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Run it
# # - Then comment out the last two lines
# #   and observe that nothing runs


# # --------------------------------
# # EXERCISE 2 — Input inside main()
# # --------------------------------
# def main():
#     name = input("Enter your name: ")
#     print("Hello", name)

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Move input() outside main() (try it)
# # - Observe why structure breaks


# # --------------------------------
# # EXERCISE 3 — Multiple prints
# # --------------------------------
# def main():
#     print("Step 1")
#     print("Step 2")
#     print("Step 3")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add a 4th print line
# # - Then remove main() call and observe nothing executes


# # --------------------------------
# # EXERCISE 4 — Direct call vs main()
# # --------------------------------
# def main():
#     print("This is main")

# main()

# # TASK:
# # - Compare this with previous examples
# # - Think: what is missing here conceptually?


# # --------------------------------
# # EXERCISE 5 — Import behavior test
# # --------------------------------

# # file1.py
# def main():
#     print("Running file1")

# if __name__ == "__main__":
#     main()


# # file2.py
# import file1
# print("file2 running")

# # TASK:
# # - Run file2.py
# # - Observe:
# #   main() in file1 does NOT run automatically

# # ////////////////////////////////////////////////////////////////////

# # !!!!After this learn how to convert Raw data in different forms!!!!

# # check python exercises for the rest of the excercises. 

