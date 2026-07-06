import requests

# the request module allows your code to access the internet withtout using a interface. 

# when storing a password you never want to save your password in plain text. instead it beter to hash it, by encrypting it with a certain algoritme encpryption. you can then store it on your device or such is how password are stored in databases.

# You dont want the raw password to go over the line so it best to first hash it and then do then make the receiver decrypt the password.

# Kanonymity allows for the hash to be even more secure and is a modern method big companies use. They use it to track you but still not know who you are. They way kanonymity works is that you only give the first 5 caracter of the hash password. 

# What the api is going to do. its going to compare in the database that is appointed to with the first 5 letters of the hash caracter. then the api will answer back with only the info about the first 5 letters. then the rest will be done in the same of some manner. in this way the api would not now the full hash password and would be relative secure. 

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)

print(res)