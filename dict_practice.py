# # 🟢 Level 1 — Basics (Create simple dicts)

# # Exercise 1
# # Create a dictionary for a user with:
# # name: "Abdullah"
# # age: 21
# # country: "Netherlands"
# # //////////////////////


# thisdict = {
#     'name': "Abdullah",
#     'age': 21,
#     'country': "Netherlands"
# }



# # Exercise 2
# # Create a dictionary for a product:
# # 'name': "Laptop"
# # 'price': 1200
# # 'in_stock': True
# # /////////////////////////

# product_dict = {
#     'name': "laptop",
#     'price': 1200,
#     'in_stock': True
# }


# # Exercise 3
# # Create a dictionary for a movie:
# # title: "Inception"
# # year: 2010
# # rating: 8.8
# # /////////////////////////

# movie_dict = {
#     'title': "Incpetion",
#     'year': 2010,
#     'rating': 8.8
# }



# # 🟡 Level 2 — Access & Modify

# # Exercise 4
# # Given a dictionary with:
# # username: "cyber_learner"
# # level: "beginner"
# # Add a new key:
# # completed_lessons: 5
# # /////////////////////////

# cyber_course = {
#     "username": "cyber_learner",
#     "level": "beginner",
# }

# cyber_course["completed_lessons"] = 5

# print(cyber_course
# )

# # Exercise 5
# # Given a dictionary:
# # item: "mouse"
# # price: 25
# # Change the price to 30
# # /////////////////////////


# product = {
#     "item" : "mouse",
#     "price" : 25,
# }

# product.update({"price": 30})

# print(product)

# # Exercise 6
# # Given a dictionary:
# # name: "server1"
# # status: "offline"
# # Update the status to "online" and add:
# # ip: "192.168.1.10"
# # /////////////////////////

# server = {
#     "name": "server1",
#     "status": "offline",
# }

# server.update({"status": "online"})
# print(server)

# # 🟠 Level 3 — Nested Dictionaries

# # Exercise 7
# # Create a dictionary for a student:
# # name: "Ali"
# # age: 20
# # grades: (a dictionary with math: 80, english: 75, science: 90)
# # /////////////////////////

# student = {
#     "name": "ali",
#     "age": 20,
#     "grades": {
#         "math": 80,
#         "english": 75,
#         "science": 90
#     }
# }

# print(student)

# # Exercise 8
# # Create a dictionary for a user profile:
# # username: "abdullah123"
# # email: "test@email.com"
# # address: (dictionary with city: "Utrecht", zip: "1234AB")
# # /////////////////////////

# usr_profile = {
#     "username": "abdullah123",
#     "email": "test@email.com",
#     "address": {
#         "zip": "1234AB"
#     }
#     }
# print(usr_profile)

# # Exercise 9
# # Create a dictionary for a car:
# # brand: "Toyota"
# # model: "Corolla"
# # specs: (dictionary with horsepower: 130, fuel: "petrol")
# # /////////////////////////

# car = {
#     "brand": "Toyota",
#     "model": "Corolla",
#     "spec": {
#         "horsepower": 130,
#         "fuel": "petrol"
#     }
# }

# # 🔵 Level 4 — Lists inside Dicts

# # Exercise 10
# # Create a dictionary for a course:
# # name: "Python Basics"
# # students: ["Ali", "Omar", "Yusuf"]
# # /////////////////////////

# course = {
#     "name": "Python Basics",
#     "students": ["Ali", "Omar", "Yusuf"]
# }

# # Exercise 11
# # Create a dictionary for a server:
# # hostname: "server01"
# # open_ports: [22, 80, 443]
# # /////////////////////////d

# server = {
#     "hostname": "sever01",
#     "open_ports": [22, 80, 443]
# }


# # Exercise 12
# # Create a dictionary for a shopping cart:
# # user: "abdullah"
# # items: ["keyboard", "mouse", "monitor"]
# # /////////////////////////

# shopping_cart = {
#     "user": "abdullah",
#     "items": ["keyboard", "mouse", "monitor"]
# }


# 🔴 Level 5 — Intermediate (Realistic structures)

# Exercise 13
# Create a dictionary representing a SIEM alert:
# alert_id: "A1001"
# severity: "high"
# source_ip: "192.168.1.5"
# destination_ip: "10.0.0.2"
# timestamp: "2026-03-23 10:00"
# /////////////////////////

# SIEM_Alerts = {
#     "alert_id": "A1001",
#     "severity": "high",
#     "source_IP": "192.168.1.5",
#     "destination_ip": "10.0.0.2",
#     "timestamp": "2026-03-23 10:00"
# }
# print(SIEM_Alerts)

# Exercise 14
# Create a dictionary for a Linux system:
# hostname: "kali"
# users: (list of dictionaries with username + uid)
# services: (dictionary with ssh: "running", apache: "stopped")
# /////////////////////////

# ///
user_data = """ 
ali, 1001
omar, 1002
yusuf, 1003
zayd, 1004
ibrahim, 1005 
"""
rem_lines = user_data.strip().split("\n")
split_lines = [line.split(", ") for line in rem_lines]
usr_d_dict = dict(split_lines)
print(usr_d_dict)
# ////




linux_system = {
    "hostname": "kali",
    "users": usr_d_dict,
    "services": {
        "ssh": "running",
        "apache": "stopped"
    }

    }

print(linux_system)

# Exercise 15
# Create a dictionary for a log entry:
# event: "failed_login"
# user: "root"
# attempts: 3
# metadata: (dictionary with ip: "8.8.8.8", location: "unknown")
# /////////////////////////

# ⚫ Level 6 — Slightly Challenging (Think Structurally)

# Exercise 16
# Create a dictionary for a company:
# name: "CyberSec Ltd"
# employees: (list of dictionaries with name + role)
# departments: (dictionary where each department has a list of employee names)
# /////////////////////////

# Exercise 17
# Create a dictionary for a network:
# network_name: "office_net"
# devices: (list of dictionaries with ip, mac, and status)
# /////////////////////////

# Exercise 18
# Create a dictionary for a threat intelligence report:
# threat_name: "Brute Force Attack"
# indicators: (list of IPs)
# details: (dictionary with severity, description, mitigation_steps as a list)
# /////////////////////////