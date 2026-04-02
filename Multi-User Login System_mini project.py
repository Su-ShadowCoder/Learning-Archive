# ================================
# Exercise: Multi-User Login System
# ================================

# You must build a login system with:
# - multiple users
# - per-user password checking
# - per-user attempt tracking
# - account lock after 3 failed attempts


# -------------------------------
# 1. User database (DO NOT CHANGE)
# -------------------------------
# users = {
#     "abdullah": "python123",
#     "alice": "abc123",
#     "bob": "secure999"
# }


# -------------------------------
# 2. Attempt tracking (YOU USE THIS)
# -------------------------------
# attempts = {
#     "abdullah": 0,
#     "alice": 0,
#     "bob": 0
# }


# -------------------------------
# 3. Your task:
# -------------------------------
# Build a login system that:

# A) Asks for a username
# B) If username not found:
#    - print "User not found"
#    - ask again

# C) If username exists:
#    - ask for password

# D) If password is correct:
#    - print "Access granted"
#    - stop program

# E) If password is wrong:
#    - increase that user's attempt counter by 1
#    - print remaining attempts

# F) If a user reaches 3 failed attempts:
#    - print "Account locked"
#    - that user cannot log in anymore


# -------------------------------
# 4. Extra challenge (optional)
# -------------------------------
# Create a "locked_users" list or dict
# and prevent locked users from trying again


# -------------------------------
# 5. Rules
# -------------------------------
# - You MUST use loops
# - You MUST use dictionaries
# - You MUST track attempts per user
# - Do NOT use global single attempt counter
# - Each user has independent login state



# Multi user login system
def main():
    multi_login_system()

# users
users = {
    "abdullah": "python123",
    "alice": "abc123",
    "bob": "secure999"
}

users_count = {
    "abdullah": 0,
    "alice": 0,
    "bob": 0
}

def multi_login_system():
    authentication = False
    authenticated = False
    account_blocked = False
    login_state = True
    users_blocked = {}
    while login_state:
        usr_name = input("Please enter username to log in:\n").lower()
        if usr_name in users_blocked:
                print("Your account has been blocked.\nPlease contact the Admin!")
        elif usr_name not in users:
            print(f"{usr_name} was not found.\nPlease enter a valid username.")
        elif usr_name in users:
            usr_password = input(f"Hello {usr_name},\nPlease enter your Password:\n").lower()
            dict_usr_key = usr_name
            # print(users.get(dict_usr_key)) tried to check key look up
            if usr_password == users.get(dict_usr_key):
                print(f"ACCESS GRANTED!\nWelcome back {usr_name}!")
                login_state = authenticated
            elif usr_password != users.get(dict_usr_key):
                if users_count[dict_usr_key] != 2:
                    print(f"ACCESS DENIED!\nPlease try again {usr_name}!")
                    users_count[usr_name] += 1
                    if users_count.get(dict_usr_key) == 1:
                        print(f"{users_count.get(dict_usr_key)} failed attempt\nWARNING\nAt 3 failed attempts, your account will be temporarily blocked!")
                    else:
                        print(f"{users_count.get(dict_usr_key)} failed attempts\nWARNING\nAt 3 failed attempts, your account will be temporarily blocked!")
                else:
                    print(f"Account:{dict_usr_key} has been blocked!\nPlease contact the Admin!")
                    users_blocked[dict_usr_key] = users.get(dict_usr_key)
                    users.pop(dict_usr_key)
                    print(users_blocked)

if __name__ == "__main__":
    main()
