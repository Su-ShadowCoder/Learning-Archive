# analytical questions:

# q1 i dont know because , you didnt use user.key(), maybe error or the place where the key is
# q2 all the values in the the user dict. 
# q3 you get all the items in the user dict


# Exercise 1

# Create:

# book = {
#     "title": "Dune",
#     "author": "Frank Herbert",
#     "pages": 412
# }

# # Use a loop to print only the keys.


# for key in book.keys():
#     print(key)


# Exercise 2

# Using the same dictionary,

# print only the values.


# for value in book.values():
#     print(value)

# Exercise 3

# Using the same dictionary,

# print both key and value.

# Example output:

# title : Dune
# author : Frank Herbert
# pages : 412

# for key, value in book.items():
#     print(key, value)

# Exercise 4

# Create:

server = {
    "hostname": "DC01",
    "ip": "10.0.0.5",
    "status": "Online",
    "users": 18
}

# Print:

# hostname = DC01
# ip = 10.0.0.5
# status = Online
# users = 18

# using one loop.

# for key, value in server.items():
#     print(f"{key} = {value}")



# Exercise 5

# Create a dictionary describing your favorite game.

# Include at least:

# title
# genre
# platform
# year
# rating

# Use one loop to print everything.

# cyberpunk2077 = {
#     'title': "Cyberpunk2077",
#     'genre': 'Sci-Fi',
#     'platform': 'PC',
#     'year': 2020,
#     'rating': 'Steam: 9/10'
# }

# for key, value in cyberpunk2077.items():
#     print(key, value)

# ⭐ Cybersecurity Exercise

# Create:

event = {
    "username": "shadow",
    "ip_address": "192.168.1.44",
    "event_type": "Failed Login",
    "severity": "High",
    "timestamp": "09:42"
}


# for key, value in event.items():
#     print(f"{key} -> {value}")

# Loop through the dictionary and print:

# username -> shadow
# ip_address -> 192.168.1.44
# event_type -> Failed Login
# severity -> High
# timestamp -> 09:42


# ⭐ Mini Project

# Create an inventory.

inventory = {
    "Keyboard": 8,
    "Mouse": 12,
    "Monitor": 5,
    "Laptop": 3,
    "USB": 25
}

# Using one loop, print:

# Keyboard : 8
# Mouse : 12
# Monitor : 5
# Laptop : 3
# USB : 25


# for key, value in inventory.items():
#     print(f"{key} : {value}")


# 🎯 Challenge (No Hints)

# Create a dictionary with 10 keys about your PC.

# Then:

# Print only the keys.
# Print only the values.
# Print both.
# Count how many iterations the loop performs.

# (Hint: Think about what determines the number of iterations.)

random_pc = {
    'CPU Clock Speed': '5.1 GHz',
    'RAM Capacity': '32 GB',
    'GPU VRAM': '16 GB GDDR6X',
    'Storage Interface': 'PDle 4.0 NVMe',
    'Power Supply Unit(PSU)': '850W 80+ Gold',
    'Motherboard Form Factor': 'ATX',
    'Cooling Type': '360mm AIO Liquid Cooler',
    'Case Fan Size': '120mm',
    'Display Refresh Rate': '240 Hz',
    'Thermal Design Power (TDP)': '125W'
}

for key in random_pc.keys():
    print(key)

for value in random_pc.values():
    print(value)

count = 1
for key, value in random_pc.items():
    print(count, key, value)
    count += 1

