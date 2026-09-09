# ============================================================
# PYTHON FUNDAMENTALS — EXERCISES 1–10
# ============================================================

# Final check and validation for my competence in python fundamentals.
# i might do more exercise for something to make it final when it comes to python. 

# ============================================================
# EXERCISE 1 — Variables & Types
# ============================================================

# Create variables for:
# - a username
# - an age
# - a failed login count
# - whether the account is locked
#
# Print each value and its type.


# YOUR CODE HERE



# ============================================================
# EXERCISE 2 — Operators
# ============================================================

# Given:

successful_logins = 17
failed_logins = 5

# Calculate:
# - total login attempts
# - difference between successful and failed logins
# - percentage of attempts that failed
#
# Print all three results.


# YOUR CODE HERE



# ============================================================
# EXERCISE 3 — Strings
# ============================================================

username = "shadow"
ip = "192.168.1.20"

# Create a message containing both values.
#
# Then:
# - print the message in uppercase
# - print the length of the username
# - check whether "shadow" appears in the message


# YOUR CODE HERE



# ============================================================
# EXERCISE 4 — String Manipulation
# ============================================================

raw_username = "   ShadowCoder   "

# Create a cleaned version of the username.
#
# It should:
# - remove unnecessary whitespace
# - be lowercase
#
# Print the original and cleaned versions.


# YOUR CODE HERE



# ============================================================
# EXERCISE 5 — Comparisons & Boolean Logic
# ============================================================

failed_attempts = 4
account_locked = False

# Create conditions that determine:
# - whether the user has too many failed attempts
# - whether the account is currently locked
# - whether BOTH conditions are true
#
# Print the results.


# YOUR CODE HERE



# ============================================================
# EXERCISE 6 — if / elif / else
# ============================================================

failed_attempts = 7

# Determine the login risk:
#
# 0–2    -> "LOW"
# 3–5    -> "MEDIUM"
# 6–10   -> "HIGH"
# 11+    -> "CRITICAL"
#
# Print the resulting risk level.


# YOUR CODE HERE



# ============================================================
# EXERCISE 7 — Nested Conditions
# ============================================================

username = "shadow"
failed_attempts = 4
account_locked = False

# Determine whether the user should be allowed to attempt
# another login.
#
# A user may attempt another login only if:
# - the account is not locked
# - AND failed attempts are fewer than 5
#
# Print the result.


# YOUR CODE HERE



# ============================================================
# EXERCISE 8 — for Loop
# ============================================================

login_attempts = [
    "Success",
    "Failed",
    "Failed",
    "Success",
    "Failed"
]

# Loop through the attempts.
#
# Print each attempt.
#
# Then count how many failed attempts there are.


# YOUR CODE HERE



# ============================================================
# EXERCISE 9 — for Loop + if
# ============================================================

events = [
    "LOGIN_SUCCESS",
    "LOGIN_FAILED",
    "FILE_ACCESS",
    "LOGIN_FAILED",
    "PASSWORD_CHANGE",
    "LOGIN_SUCCESS",
    "LOGIN_FAILED"
]

# Loop through the events.
#
# Print only the login failures.
#
# Also count how many login failures occurred.


# YOUR CODE HERE



# ============================================================
# EXERCISE 10 — while Loop
# ============================================================

failed_attempts = 0

# Simulate login failures.
#
# Keep increasing failed_attempts until it reaches 3.
#
# Print each attempt number.
#
# Once 3 failures are reached, print:
# "ACCOUNT LOCKED"


# YOUR CODE HERE

