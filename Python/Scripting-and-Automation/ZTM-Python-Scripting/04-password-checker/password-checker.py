
# the request module allows your code to access the internet withtout using a interface. 

# when storing a password you never want to save your password in plain text. instead it beter to hash it, by encrypting it with a certain algoritme encpryption. you can then store it on your device or such is how password are stored in databases.

# You dont want the raw password to go over the line so it best to first hash it and then do then make the receiver decrypt the password.

# Kanonymity allows for the hash to be even more secure and is a modern method big companies use. They use it to track you but still not know who you are. They way kanonymity works is that you only give the first 5 caracter of the hash password. 

# What the api is going to do. its going to compare in the database that is appointed to with the first 5 letters of the hash caracter. then the api will answer back with only the info about the first 5 letters. then the rest will be done in the same of some manner. in this way the api would not now the full hash password and would be relative secure. 

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res

def get_password_lleaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
    

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_5char)
    return get_password_lleaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times... you should probably change your password!")
        else:
            print(f"{password} was NOT found. Carry on!")
    return 'done!'


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# to improve is that some terminal shell programs allows you to use upper arrow key to recover what was previously entered. when using this script it would not be secure to enter a password in this way to check. so in order to safeguard that the password wont get saved in such manner, i need to make it as such that the password get check from a txt file and in such manner that the script reads the txt file and checks the password with this method. 

