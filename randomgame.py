# # Exercise

# The goal is to write a game program, call it randomgame.py,
# ask a user to guess a number for example between 1 and 10. 
# do that using the sys.argv by using 2 index arguements. 
# python3 [filename.py] [range1] [range2], python3 [0] [1] [2]
# get that information and try to randomly generate a number from that range
# from there the user can keep guessing until the user gets it right. 
# and at the and say when the user got it right that the terminal prints: You are a genius!, and
# if the user keeps getting it wrong the terminal will keep asking the user until the user gets it right
# and also use validation in the program as well to make sure that the user enters something that has been provided by the terminal with as an option. 

import random

import sys

class RangeError(Exception):
    pass


try:
    user_first_numr = 1 #int(sys.argv [1])
    user_second_numr = 10 #int(sys.argv [2])
except (ValueError, IndexError):
            print("Please enter a valid number")
            sys.exit()


def get_random_number():
    return random.randrange(user_first_numr, user_second_numr  + 1)

def get_user_numb_inp():
    while True:
        try:
            x = None
            x = int(input("Please guess and enter a number, the number between the numbers that you have entered:\n"))
            if user_first_numr <= x <= user_second_numr:
                return x
            else:
                raise RangeError
        except ValueError:
                return("Please enter a valid number")
        except RangeError:
                return(f"{x} is outside of specified range!")
    
def validating(user_numb_inp, targetnumber):
        try:
            if user_numb_inp == targetnumber:
                return(f"You are a genius, the number was: {targetnumber}")
            else:
                return("please try again")
        except Exception as err:
            return err


def main():
    targetnumber = get_random_number()
    
    while True:
        user_numb_inp = get_user_numb_inp()
        if isinstance(user_numb_inp, str):
            print(user_numb_inp)
            continue

        result_message = validating(user_numb_inp, targetnumber)
        
        print(result_message)
        if user_numb_inp == targetnumber:
            break


if __name__=="__main__":
    main()

