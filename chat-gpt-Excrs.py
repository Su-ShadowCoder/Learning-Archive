




# ///////////////////////////////////////////////////////////////////////

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
users = {
    "abdullah": "python123",
    "alice": "abc123",
    "bob": "secure999"
}


# -------------------------------
# 2. Attempt tracking (YOU USE THIS)
# -------------------------------
attempts = {
    "abdullah": 0,
    "alice": 0,
    "bob": 0
}


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

# ////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////

# ==========================================
# EXERCISE — LOGIN SYSTEM (BUILD FROM SCRATCH)
# ==========================================

# REQUIREMENTS:

# 1. Create a dictionary called "users"
#    - Add at least 3 usernames with passwords

# 2. Create a dictionary called "attempts"
#    - Each user starts with 0 attempts

# 3. Ask the user for a username

# 4. If the username does NOT exist:
#    - print "User not found"
#    - stop program

# 5. If the username exists:
#    - allow the user to enter password multiple times

# 6. Rules for password checking:
#    - if password is correct:
#        -> print "AUTHENTICATED"
#        -> stop program
#    - if password is wrong:
#        -> increase attempt count for that user
#        -> print remaining attempts

# 7. Lockout rule:
#    - if attempts reach 3:
#        -> print "LOCKED OUT"
#        -> stop program

# 8. Use a loop (while or for) to control attempts

# 9. (Optional challenge)
#    - Print attempt history after each try


def main():
    # WRITE YOUR CODE HERE
    pass


if __name__ == "__main__":
    main()

# ////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////
# ==========================================
# EXERCISE — DICTIONARY DESIGN (NO TEMPLATE GIVEN)
# ==========================================

# RULE:
# You must decide the structure of the dictionaries yourself.

# GOAL:
# Build a small system using ONLY dictionaries, input, conditions, and loops.

# ==========================================
# REQUIREMENTS
# ==========================================

# 1. Create a dictionary that stores USERS
#    - You choose the structure
#    - Must include at least 3 users
#    - Each user must have at least ONE piece of data (you decide what)

# 2. Create a SECOND dictionary that tracks something per user
#    Examples (pick ONE idea only):
#    - login attempts
#    - number of actions
#    - score
#    - warnings
#    - activity count

# 3. Ask the user for a key (username or identifier)

# 4. If the key does NOT exist:
#    - print a message
#    - stop program

# 5. If the key exists:
#    - enter a loop

# 6. Inside the loop:
#    - ask for input (you decide what kind of input)
#    - update the second dictionary based on that input
#    - print current state after each update

# 7. Add a STOP condition:
#    - user can exit manually OR
#    - system stops after a limit you define

# 8. You MUST use:
#    - dictionary lookup
#    - dictionary update
#    - at least one loop
#    - at least one condition

# ==========================================
# OPTIONAL CHALLENGE (HIGHER LEVEL THINKING)
# ==========================================

# - Add a "status" system per user (ACTIVE / BLOCKED / etc.)
# - Change status based on behavior inside the loop
# - Make the program behave differently depending on status


def main():
    # DESIGN EVERYTHING YOURSELF
    pass


if __name__ == "__main__":
    main()


