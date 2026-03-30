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
# def main():
#     user = {
#         "name": "abdullah",
#         "age": 20
#     }

#     user["name"] = "ibrahim"

#     print(user)





# if __name__ == "__main__":
#     main()

# # TASK:
# # - Change "name" instead of "age"


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

# TASK:
# - Test: name, age, city
# abdullah@pc:~/python-projects/Python_exercises_refresh$ /bin/python3 "/home/abdullah/python-projects/Python_exercises_refresh/dict & main() - practice - 03-26.py"
# Enter key: name
# Found: abdullah
# abdullah@pc:~/python-projects/Python_exercises_refresh$ /bin/python3 "/home/abdullah/python-projects/Python_exercises_refresh/dict & main() - practice - 03-26.py"
# Enter key: age
# Found: 20
# abdullah@pc:~/python-projects/Python_exercises_refresh$ /bin/python3 "/home/abdullah/python-projects/Python_exercises_refresh/dict & main() - practice - 03-26.py"
# Enter key: city
# # Not found

# # ------------------------------------------
# # EXERCISE 5 — Default value logic
# # ------------------------------------------
# def main():
#     user = {
#         "name": "abdullah"
#     }

#     key = input("Enter key: ")

#     user["age"] = 31
#     user["city"] = "Amsterdam"

#     if key in user:
#         print(user[key])
#     else:
#         print("Default: unknown")

# if __name__ == "__main__":
#     main()

# # TASK:
# # - Add more keys
# # - Try missing keys

# abdullah@pc:~/python-projects/Python_exercises_refresh$ /bin/python3 "/home/abdullah/python-projects/Python_exercises_refresh/dict & main() - practice - 03-26.py"
# Enter key: city
# Amsterdam
# abdullah@pc:~/python-projects/Python_exercises_refresh$ /bin/python3 "/home/abdullah/python-projects/Python_exercises_refresh/dict & main() - practice - 03-26.py"
# Enter key: age
# 31
# abdullah@pc:~/python-projects/Python_exercises_refresh$ /bin/python3 "/home/abdullah/python-projects/Python_exercises_refresh/dict & main() - practice - 03-26.py"
# Enter key: occupation
# Default: unknown
# abdullah@pc:~/python-projects/Python_exercises_refresh$ 

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

#     logs["INFO"] *= 2

#     if "ERROR" in logs:
#         print("ERROR")

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

#     # adding new user
#     users["michael"] = "xyz123"

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

# TASK:
# - Run multiple times
# - Observe attempt counter increase per user

# first there is no pasward. and the counter doesnt work properly. it stops at one because there is no loop and guard for the loop. afte count 1 it just stops. 


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

#     user["country"] = "Narnia"

#     print(user["name"])
#     print(user["age"])
#     print(user["country"])

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

#     users["bruce"] = "hellow"

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

#     users["wayne"] = "batman"
#     users["clark"] = "kent"

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
#     users["abdullah"] = "oldpass"

#     print(users["abdullah"])

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

    
#     users["clark"] = "supaman"
#     attempts["clark"] = 0
    

#     while True:
#         username = input("Enter username: ")
#         if username in users:
#             print("User found")
#             attempts[username] += 1
#             print("Attempts:", attempts[username])
#             break
#         else: 
#             attempts[username] = attempts.get(username,  0) + 1
#             print(f"User not found")
#             print(f"Attempts: {attempts[username]}")
#             if attempts[username] == 3:
#                 break


# if __name__ == "__main__":
#     main()

# # TASK:
# # - Run multiple times and watch attempt count increase
# # - Add a new user and extend both dictionaries



# # ////////////////////////////////////////////////////////////////////

# ================================
# MAIN() SIMPLE PRACTICE EXERCISES
# ================================

# --------------------------------
# EXERCISE 1 — Basic main()
# --------------------------------
# TASK:
# - Create a main() function that prints "Hello from main"
# - Call it with the if __name__ == "__main__" guard
# - Then comment out the guard and observe what changes
# //


# def hello():
#     print("Hello from main")

# def main():
#     hello()

# if __name__ == "__main__":
#     main()

# Nothing happens because nothing is being executed to run something via code. 


# --------------------------------
# EXERCISE 2 — Input inside main()
# --------------------------------
# TASK:
# - Create a main() that asks for your name and prints a greeting
# - Then try moving input() outside main() and observe what breaks


# def ask_name():
#     usr_name =  input("Please enter your name:\n")
#     print(f"Hellow, {usr_name}!")

# ask_name()


# def main():
#     # ask_name()

# if __name__ == "__main__":
#     main()

# before you ciritsize me i did my job ad  put it outisde look at commented stuff i would have doen it right if you didnt tell me too.  

# --------------------------------
# EXERCISE 3 — Multiple prints
# --------------------------------
# TASK:
# - Create a main() that prints Step 1, Step 2, Step 3, Step 4
# - Remove the main() call and observe nothing executes


# def main():
#     steps_print()

# def steps_print():
#     for numb in range(1, 5):
#         print(f"Step {numb}")


# if __name__ == "__main__":
#     # main()

# did as i was supposed too. 

# --------------------------------
# EXERCISE 4 — Direct call vs main()
# --------------------------------
# TASK:
# - Create a main() function that prints something
# - Call it directly without the if __name__ guard
# - Think: what is the difference and what is missing?

def main():
    print_something()

def print_something():
    print("Hellow")

main()

# --------------------------------
# EXERCISE 5 — Import behavior test
# --------------------------------
# TASK:
# - Create file1.py with a main() and the if __name__ guard
# - Create file2.py that imports file1 and prints "file2 running"
# - Run file2.py and observe that file1's main() does NOT run



# # !!!!After this learn how to convert Raw data in different forms!!!!

# # check python exercises for the rest of the excercises. 

