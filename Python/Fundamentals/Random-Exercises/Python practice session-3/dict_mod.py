# 🟡 Topic 1 — Add New Keys ⭐⭐⭐⭐⭐
# Exercise 1

# Create this dictionary:

# user = {
#     "username": "shadow",
#     "role": "student"
# }

# Add:

# email
# country

# Print the whole dictionary.



user = {
    "username": 'shadow',
    'role': 'student'
}

user['email'] = 'cyberguardian@gmail.com'

user['country'] = 'Netherlands'

# print(user)

# Exercise 2

# Create:

# game = {
#     "name": "Knight"
# }

# Add:

# level
# health
# mana

# Print the dictionary.


game = {
    'name': 'knight'
}

game['level'] = 43

game['health'] = 89

game['mana'] = 150

# print(game)




# Exercise 3

# Create:

# employee = {
#     "name": "Sarah",
#     "department": "IT"
# }

# Add:

# salary
# years_worked

# Print everything.


employee = {
    'name': 'Sarah',
    'department': 'IT'
}

employee['salary'] = 3400
employee['years_worked'] = 5

# print(employee)

# 🟡 Topic 2 — Update Existing Values ⭐⭐⭐⭐⭐
# Exercise 4
# inventory = {
#     "apples": 15,
#     "bananas": 8
# }

# Update:

# apples → 20
# bananas → 5

# Print the dictionary.



inventory = {
    "apples": 15,
    "bananas": 8
}


inventory['apples'] = 20
inventory['bananas']= 5

# print(inventory)

# Exercise 5
# player = {
#     "name": "Warrior",
#     "level": 1,
#     "hp": 100
# }

# Update:

# level → 2
# hp → 120

# Print everything.


player = {
    "name": "Warrior",
    "level": 1,
    "hp": 100
}

player['level'] = 2
player['hp'] = 120

# print(player)



# Exercise 6
# movie = {
#     "title": "The Matrix",
#     "rating": 8.5
# }

# Update the rating to 9.2.


movie = {
    "title": "The Matrix",
    "rating": 8.5
}

movie['rating'] = 9.2


# print(movie)





# 🟡 Topic 3 — Delete Keys ⭐⭐⭐⭐☆
# Exercise 7
# person = {
#     "name": "Ali",
#     "age": 24,
#     "city": "Amsterdam"
# }

# Delete:

# age

# Print the dictionary.



person = {
    "name": "Ali",
    "age": 24,
    "city": "Amsterdam"
}


del person['age']
# print(person)



# Exercise 8
account = {
    "username": "shadow",
    "password": "abc123",
    "email": "shadow@email.com"
}

# Delete the password.

# Print the dictionary.


del account['password']
# print(account)





# Exercise 9
shopping = {
    "milk": 2,
    "bread": 1,
    "eggs": 12
}

# Delete "bread".

shopping.pop('bread')
# print(shopping)




# 🟡 Topic 4 — .get() ⭐⭐⭐⭐⭐

# This is one of the most useful dictionary methods.

# Exercise 10
student = {
    "name": "Mike",
    "course": "Python"
}

# Use .get() to print:

# name
# course





# print(student.get('name'))
# print(student.get('course'))




# Exercise 11

# Try to get:

# "age"

# using .get().

# What happens?





# print(student.get('age'))

# i get NONE. because there is no value. and the correct one is to use is indeed the get method.




# Exercise 12

# Now use:

# .get("age", "Unknown")

# What gets printed?




# print(student.get('age', 'Uknown'))

# i get unknown




# ⭐ Mini Project

# Create a dictionary representing a login event.

# It should have at least:

# username
# ip_address
# country
# failed_attempts
# account_locked

# Now:

# Add a timestamp.
# Update failed_attempts.
# Delete the country.
# Use .get() to retrieve:
# username
# timestamp
# device (which doesn't exist)



log_event = {
    'username': 'shadow123',
    'ip_address': '192.168.24.1',
    'country': 'Unitedkingdom',
    'failed_attempts': 3,
    'account_locked': False
}

print(log_event)

log_event['time'] = '16:43:15'

log_event['failed_attempts'] = 4

del log_event['country']


print(log_event.get('username'))
print(log_event.get('time'))
print(log_event.get('device'))

print(log_event)



# 🎯 Challenge (No Hints)

# Create a dictionary for a bank account.

# Include at least:

# account number
# owner
# balance
# active

# Then:

# Add an account type.
# Update the balance.
# Delete one key.
# Use .get() on both an existing key and a missing key.

bank_account = {
    'account number': 123443324,
    'owner': 'James Smith',
    'balance': 1500,
    'active': True
}

print(bank_account)

bank_account['account type'] = 'Saving account'

print(bank_account)

bank_account['balance'] = 3000

print(bank_account)

del bank_account['active']


print(bank_account.get('active'))
print(bank_account.get('balance'))

