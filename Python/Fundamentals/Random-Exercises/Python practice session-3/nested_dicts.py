# # 🟢 Exercise 1

# # Information

# # Employee 1

# # Name: Sarah
# # Age: 29
# # Department: IT

# # Employee 2

# # Name: Ahmed
# # Age: 35
# # Department: HR

# # Tasks

# # Create a nested dictionary.
# # Print Ahmed's department.

# employees = {
#     'Employee 1': {
#     'Name': 'Sarah',
#     'Age': 29,
#     'Department': 'IT'
# },
# 'Employee 2': {
#     'Name': 'Ahmed',
#     'Age': 35,
#     'Department': 'HR'
# }
# }

# # print(employees['Employee 2']['Department'])


# # 🟢 Exercise 2

# # Update Sarah's age to 30.

# # Print the updated nested dictionary.

# employees['Employee 1']['Age'] = 30

# # print(employees)


# # 🟢 Exercise 3

# # Add:

# # salary = 4200

# # to Ahmed.

# employees['Employee 2'].update({"Salary": 4200})
# # print(employees)

# # 🟢 Exercise 4

# # Add a third employee.

# # Information:

# # Name: Maria
# # Age: 41
# # Department: Finance

# # Then print Maria's information.

# employees['Employee 3'] = {'Name': 'Maria', 'Age': 41, 'Department': 'Finance'}


# # print(employees['Employee 3']


# # 🟢 Exercise 5

# # Delete department from Sarah.


# # del employees['Employee 1']['Department']

# # print(employees['Employee 1'].keys())



# # ⭐ Cybersecurity Challenge
# # Information
# # Event 1
# # Username: shadow
# # IP: 192.168.1.44
# # Status: Failed Login
# # Timestamp: 08:41
# # Event 2
# # Username: admin
# # IP: 10.0.0.5
# # Status: Success
# # Timestamp: 09:12
# # Event 3
# # Username: guest
# # IP: 172.16.5.10
# # Status: Failed Login
# # Timestamp: 09:45
# # Tasks
# # Create a nested dictionary.
# # Print the IP address of Event 2.
# # Change Event 3's status to "Locked".
# # Add a field:
# # severity = High
# # to Event 1.
# # 5. Delete the timestamp from Event 2.
# # 6. Print the entire nested dictionary.

# events = {
#     'event 1': {'Username': 'shadow', 'IP': '192.168.1.44', 'Status': 'Failed Login', 'Timestamp': '08:41'},
    
#     'event 2': {'Username': 'Admin', 'IP': '10.0.0.5', 'Status': 'Success', 'Timestamp': '09:12'},
    
#     'event 3': {'Username': 'guest', 'IP': '172.16.5.10', 'Status': 'Failed Login', 'Timestamp': '09:45'}
# }

# # print(events)

# # print(events['event 2']['IP'])

# # events['event 3']['Status'] = 'Locked'

# # print(events['event 3']['Status'])

# # events['event 1'].update({'Severity': 'High'})

# # del events['event 2']['Timestamp'] # or update the the item by inserting a none or just black space for the value of the timestamp.

# # print(events)


# # i had to do a lot of document reviewing so i google a lot if i am being honest. also just ot make it easier for myself once i had one dict set i copied it and changed the values XD. 



# Mini SOC Analyst Exercise

# You receive these login events:

events = [
    {
        "username": "shadow",
        "status": "Failed",
        "ip": "192.168.1.20"
    },
    {
        "username": "admin",
        "status": "Success",
        "ip": "10.0.0.5"
    },
    {
        "username": "shadow",
        "status": "Failed",
        "ip": "192.168.1.20"
    }
]

# Your tasks would be:

# Create a function that counts failed logins.
# Loop through the events.
# Check the status.
# Return the number of failed attempts.

failed_counts = 0

for inner_dict in events:
    # print(inner_dict)
    print(inner_dict['status'])



    if inner_dict['status'] == 'Failed':
        failed_counts += 1

print(failed_counts)
