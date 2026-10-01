# Question 1
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


# result = []

# for numb in range(2000, 3201):
#     if numb % 5 != 0 and numb % 7 == 0:
#         result.append(str(numb))

# # print(result)
# g_result = ','.join(result)

# print(g_result)


# Question 2
# Question:
# Write a program which can compute the factorial of a given number. Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# numb_inp = int(input('enter a desired factorial number:\n'))

# result = 1

# for numb in range(1, numb_inp + 1):
#     result *= numb

# print(result)                                                      


# Question 3
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# usr_inp = int(input("Enter numb:\n"))

# some_dic = {}



# for numb in range(1 , usr_inp + 1):
#     key = numb
#     value = key ** 2
#     some_dic[key] = value

# print(some_dic)
###################################################################


# Question 4
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# 34,67,55,33,12,98
# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple



# # usr_inp = input('Enter number:')
# usr_inp = '34,67,55,33,12,98'

# answer_lst = usr_inp.split(',')
# answer = usr_inp.split(',')

# answer_tpl = tuple(answer)
# print(f"{answer_lst}\n{answer_tpl}")


# Question 5
# Question:
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

# class Car:

#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
    
#     def get_name(self):
#         print(self.name)

#     def get_model(self):
#         print(self.model)

#     def __str__(self):
#         return f"{self.name}, {self.model}"


#     def get_string(self):
#         usr_inp = input('Enter string:\n')
#         return usr_inp
    
#     def output_string(self, something_str):
#         print(something_str.upper())


# car1 = Car('Alfa Romeo', 'Giulia')
# # print(car1)

# def testing_methods():
#     some = car1.get_string()
#     car1.output_string(some)

# testing_methods()

##################

# class InputStringHandler:
#     def __init__(self):
#         self.s = ''

#     def get_string(self):
#         self.s = input('Enter string:\n')
    
#     def print_string(self):
#         print(self.s.upper())

# my_handler = InputStringHandler()

# my_handler.get_string()
# my_handler.print_string()


# Question 6
# Question:
# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it should be assumed to be a console input.

# import math

# def some_crazy_formula():

#     usr_inp = (input("Enter a number and if more than 1 entree seperate it with a comma:\n").strip())

#     c = 50
#     h = 30

#     t_lst = usr_inp.split(",")


#     d_lst = []
#     for entree in t_lst:

#         q = ((2*c*int(entree))/h)
#         root_result = math.sqrt(q)
#         rounden_result = round(root_result)
#         d_lst.append(str(rounden_result))
#     string_of_result = ",".join(d_lst)
#     return string_of_result

# print(some_crazy_formula())

###########################################################
# Question 7
# Question:
# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

# x = int(input('Please enter x:\n'))
# y = int(input('Please enter y:\n'))

# final_array = []
# for xnumb in range(0, x):
#     array = []
#     for ynumb in range(0, y):
#         array.append(xnumb * ynumb)
#     final_array.append(array)

# print(final_array)



# # Question 8
# # Question:
# # Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# # Suppose the following input is supplied to the program:

# # without,hello,bag,world
# # Then, the output should be:

# # bag,hello,without,world
# # Hints:
# # In case of input data being supplied to the question, it should be assumed to be a console input.

# usr_in = input("Enter words with coma seperated sequence:\n")

# usr_list = usr_in.split(',')

# alp_usr_lst = sorted(usr_list)

# result = ",".join(alp_usr_lst)

# print(result)



# # Question 9
# # Question:
# # Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# # Suppose the following input is supplied to the program:

# # Hello world
# # Practice makes perfect
# # Then, the output should be:

# # HELLO WORLD
# # PRACTICE MAKES PERFECT
# # Hints:
# # In case of input data being supplied to the question, it should be assumed to be a console input.

# lines = []

# while True:
#     line = input("")
#     if line == "stop":
#         break
#     lines.append(line)

# text = "\n".join(lines).upper()

# print(text)

# Question 10
# Question
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.


# usr_input = input('Enter a normal sentence:\n')

# tranform_usr1 = usr_input.split(' ')

# tranform_usr2 = sorted(set(tranform_usr1))

# result = " ".join(tranform_usr2)

# print(result)


# Question 11
# Question
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example:

# 0100,0011,1010,1001
# Then the output should be:

# 1010
# Notes: Assume the data is input by console.


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input

# usr_inp = input('Enter a sequence of 4 binary numbers separated by commas:\n')

# usr_lst = usr_inp.split(",")

# conv_str_lst = []

# for obj in usr_lst:
#     numb = int(obj, 2)
#     if numb % 5 == 0:
#         conv_str_lst.append(str(bin(numb))[2:])

# result = ",".join(conv_str_lst)

# print(result)

##############################################################################

# Question 12
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# t_lst = []

# for numb in range(1000, 3000 + 1):
#     if numb % 2 == 0:
#         t_lst.append(str(numb))


# result = ",".join(t_lst)

# print(result)



#################
# Question 13
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.





# try:
#     usr_inp = input("Please enter a sentence:\n")

#     digits = 0
#     letters = 0
#     for car in usr_inp:
#         if car.isdigit():
#             digits += 1
#         elif car.isalpha():
#             letters += 1
    
#     print(f"letters: {letters}, digits: {digits}.")
# except EOFError:
#     print("No input is given!")

########################################################


# Question 14
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

# def count_lower_upper():
#     try:
#         x = input("Enter a sentence without any numbers:\n")

#         upper = 0
#         lower = 0

#         for car in x:
#             if car.isupper():
#                 upper += 1
#             if car.islower():
#                 lower += 1
#             else:
#                 return "Please enter a sentence without numbers!"
        
#         return f"UPPER CASE {upper}\nLOWER CASE {lower}"
#     except EOFError:
#         print("No value entered!")

        

# print(count_lower_upper())


# ####################


# Question 15
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9

# Then, the output should be:

# 11106

# def special_form1():
#     try:
        
#         x = input("Please enter a number in order to compute it with special formula Type 1:\n")

#         if x.isdigit():
#             result = 0
#             for numb in range(1, 4+1):
#                 n = int(numb * x)

#                 result += n
#             return result
#         else:
#             return "Please Enter a number!"

#     except EOFError:
#         print("Please enter a number!")

# print(special_form1())

###########################################

# Question 16
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9
# Then, the output should be:

# 1,9,25,49,81

# def square_odd_numb():
#     try:
#         x_inp = input("Enter a sequence of comman-separated number:\n").strip()
#         splitted_lst = x_inp.split(",")
#         parse_lst = []
#         for numb in splitted_lst:
#             numb_int = int(numb)
#             if numb_int % 2 != 0:
#                 parse_lst.append(str(numb_int ** 2))
#         return ",".join(parse_lst)
#     except (EOFError, ValueError):
#         return "Enter a sequence of comman-separated number!"
         
# print(square_odd_numb())



# def square_odd_numb():
#     try:
#         x_inp = input("Enter a sequence of comman-separated number:\n")
#         splitted_lst = x_inp.split(",")
#         parse_lst = [int(numb) ** 2 for numb in splitted_lst if int(numb.strip()) % 2 != 0]
#         return ",".join([str(num) for num in parse_lst])
#     except (EOFError, ValueError):
#         return "Enter a sequence of comman-separated number!"
         
# print(square_odd_numb())



#############################################

# Question 17
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500
#################################################


# class BankAccount():

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance


#     def get_current_balance(self):
#         return f'Current balance in account: {self.balance}'
    
#     def deposit(self, x):
#         self.balance = self.balance + x

#     def withdraw(self, x):
#         if self.balance - x > 0:
#             self.balance = self.balance - x
#         else:
#             return "Balance insufficient!"

# account1 = BankAccount("acc1", 0)


# while True:
#     try:
#         x_usr = input("")
#         temp_lst = x_usr.split()
#         if temp_lst[0] == "?":
#             print(account1.get_current_balance())
#         if temp_lst[1].isdigit():
#             amount = int(temp_lst[1])
#         if temp_lst[0] == "D":
#             account1.deposit(amount)
#         elif temp_lst[0] == "W":
#             account1.withdraw(amount)
#     except IndexError:
#         continue



#########################################################

# Question 18
# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:

# ABd1234@1


# import re

# a = input("Enter password to validate:\n").split(",")

# pass_pattern =  re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$")

# for item in a:
#     if re.findall(pass_pattern, item):
#         print(item)

#####

# Question 19
# Question:
# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

# If the following tuples are given as input to the program:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:

# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]




# tlist = []

# while True:
#     user_input = input("Enter name,age,score (or press Enter to stop): \n")

#     if not user_input.strip():
#         print("Exiting program.")
#         break

#     try:
#         a = user_input.split(',')

#         stuple = (a[0].strip(),int(a[1]),int(a[2]))
#         tlist .append(stuple)

#         slst = sorted(tlist, key=lambda x: (x[0], x[1], x[2]))

#         print(slst)


#     except (IndexError, ValueError):
#         print('invalid format')


########################################

# Question 20
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14


# class GenDiv7():
#     def gen_div_7(self, n):
#         wlst = (numb for numb in range(0, n+1) if numb % 7 == 0)
#         return wlst

# gendiv7 = GenDiv7()
# something = gendiv7.gen_div_7(int(input('Please enter the number: \n')))
# for numb in something:
#     print(numb)




###########################
# Question 21
# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:

# 2
# Hints:

# In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.



# import math

# og_cords = [0,0]

# cords = [0,0]

# print("Welcome to this program that computes the auclidean distance your robot has taken.")

# while True:
#     usr = input("Enter the movements in the folowing format: 'movement steps', example: 'up 5' then press enter and continue to enter input and enter as much as you want. Press enter  without input after done.\n").upper().split()
#     if not usr:
#         break
#     inp_direction = usr[0]
#     inp_distance = int(usr[1])
#     if inp_direction == "UP":
#         cords[0] += inp_distance
#     elif inp_direction == "DOWN":
#         cords[0] -= inp_distance
#     elif inp_direction == "RIGHT":
#         cords[1] += inp_distance
#     elif inp_direction == "LEFT":
#         cords[1] -= inp_distance
#     else:
#         pass

# distance_taken = round(math.sqrt(((cords[0] - og_cords[0])**2) + ((cords[1] - og_cords[1])**2)))

# print(distance_taken)


#######################



# Question 22
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

# og_i = input('Enter a sentence:\n').split()


# def sort_alpanumerically(item):
#     if item.isdigit():
#         return (0, int(item))
#     elif item.isupper():
#         return (1, item)
#     else:
#         return (2, item)



# i_dic = {}

# for key in og_i:
#     if key not in i_dic:
#         i_dic[key] = 1
#     else:
#         i_dic[key] += 1


# sorted_dic = sorted(i_dic, key=sort_alpanumerically)
# print(sorted_dic)




##########################


# Question 23
# Question:
# Write a method which can calculate square value of number

# Hints:
# Using the ** operator which can be written as n**p where means n^p


# def squar_v(x):
#     return x ** 2
# print(squar_n(9))



############################


# Question 24
# Question:
# Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

# And add document for your own function

# Hints:
# The built-in document method is __doc__


# def info_function(function):
#     """ The info fucntion returns documentation of the inputted function """
#     return function.__doc__

# print(info_function(abs))
###################################

# Question 25
# Question:
# Define a class, which have a class parameter and have a same instance parameter.

# Hints:
# Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later


# class ToyotaCar():
#     DEFAULT_COLOR = "Green"

#     def __init__(self, name_model, color=None):
#         self.name_model = name_model
        
#         self.color = color if color is not None else ToyotaCar.DEFAULT_COLOR

#     def __str__(self):
#         return f"{self.name_model}, {self.color}"


# car1 = ToyotaCar("Yaris", "Yellow")
# car2 = ToyotaCar('Prius')

# print(car1)
# print(car2)


####################################

# Question 26
# Question:
# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.


# def sum(x, y):
#     return x + y

# print(sum(5, 7))

#################################

# Question 27
# Question:
# Define a function that can convert a integer into a string and print it in console.


# def str_conv(number):
#     return str(number)



##################################

# Question 28
# Question:
# Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.


# def add_str_numb(x, y):
#     return int(x) + int(y)

# print(add_str_numb("4", "3"))

###################################

# Question 29
# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.

# Hints:
# Use + sign to concatenate the strings.

# def add_str(x, y):
#     return x + y

# print(add_str("Hello ", "World!"))


# ######################################

# Question 30
# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

# Hints:
# Use len() function to get the length of a string.


# def get_max_str():
#     x = input("first line:\n")
#     y = input("second line:\n")

#     if len(x) > len(y):
#         return x
#     if len(x) < len(y):
#         return y
#     else:
#         return f"{x}\n{y}"

# print(get_max_str())


# ########################################

# Question 31
# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.


# def square_key_dic():
#     squarekey = {}
#     for numb in range(1, 21):
#         squarekey[numb] = numb ** 2
#     return squarekey

# print(square_key_dic())


# ########################################

# Question 32
# Question:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


# def only_key():
#     squarekey = {}
#     keyonly = []
#     for numb in range(1, 21):
#         squarekey[numb] = numb ** 2
#     for key, value in squarekey.items():
#         keyonly.append(key)
#     for item in keyonly:
#         print(item)


# print(only_key())

# ########################################

# Question 33
# Question:
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

# def squarevalue_lst():
#     squarevalue = []
#     for numb in range(1, 21):
#         squarevalue.append(numb**2)
#     return squarevalue

# print(squarevalue_lst())

# ########################################

# Question 34
# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list


# def squarevalue_lst():
#     squarevalue = []
#     for numb in range(1, 21):
#         squarevalue.append(numb**2)
#     return squarevalue

# print(squarevalue_lst()[0:6])

# ########################################

# Question 35
# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list


# def squarevalue_lst():
#     squarevalue = []
#     for numb in range(1, 21):
#         squarevalue.append(numb**2)
#     return squarevalue

# print(squarevalue_lst()[-5:])

# ########################################

# Question 36
# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

# def squarevalue_lst():
#     squarevalue = []
#     for numb in range(1, 21):
#         squarevalue.append(numb**2)
#     return squarevalue

# print(squarevalue_lst()[5:])

# ########################################

# Question 37
# Question:
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.

# def squarevalue_tupl():
#     squarevalue = []
#     for numb in range(1, 21):
#         squarevalue.append(numb**2)
#     return tuple(squarevalue)

# print(squarevalue_tupl())


# #################################################





# Question 38
# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.

# given = (1,2,3,4,5,6,7,8,9,10)

# print(given[0:5])
# print(given[5:11])

# #################################################


# Question 39
# Question:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# even_steven = []
# for numb in given:
#     if numb % 2 == 0:
#         even_steven.append(numb)

# parrot = tuple(even_steven)

# print(parrot)

# #################################################
# Question 40
# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# x = input("Enter yes in any manner or something else: \n")

# if x == "YES" or x == "Yes" or x == "yes":
#     print("Yes")
# else:
#     print("No")


# #################################################
# Question 41
# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Use map() to generate a list.Use lambda to define anonymous functions.

# random = [1,2,3,4,5,6,7,8,9,10]

# square_lst = list(map(lambda element: element ** 2, random))

# print(square_lst)

# #################################################
# Question 42
# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in 
# 

# random = [1,2,3,4,5,6,7,8,9,10]

# # Hints:
# # Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.

# even = filter(lambda numb: numb % 2 == 0, random)
# even = list(even)
# print(even)

# even_squared = list(map(lambda numb: numb ** 2, even))

# print(even_squared)




# #################################################
# Question 43
# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.Use lambda to define anonymous functions.

# numbers = range(1, 21)

# even_el = list(filter(lambda numb: numb % 2 == 0, numbers))

# print(even_el)

# #################################################

# Question 44
# Question:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.

# square_lst = list(map(lambda numb: numb ** 2, numbers))
# print(square_lst)

# ###################################
# Question 45
# Question:
# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.


# class American:

#     @staticmethod
#     def printNationality():
#         print('Nationality')


# American.printNationality()

# ###################################
# Question 46
# Question:
# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.*

# class American:
    
#     @staticmethod
#     def printNationality():
#         print('Nationality')


# class NewYorker(American):
#     pass

# ###################################
# Question 47
# Question
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

# import math

# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def circle_area(self):
#         return math.pi * self.radius ** 2





# ###################################
# Question 48
# Question
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def rect_area(self):
#         return self.length * self.width

# ###################################
# Question 49
# Question
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints
# To override a method in super class, we can define a method with the same name in the super class.

# class Shape:
#     area = 0

#     def get_area(self):
#         return self.area

# class Square(Shape):

#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         return self.length ** 2



# ###################################
# Question 50
# Question
# Please raise a RuntimeError exception.

# Hints
# UUse raise() to raise an exception.

# ###################################

# raise RuntimeError("problem")

###########################################

# Question 51
# Question
# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints
# Use try/except to catch exceptions.


# def div_zero(x):
#     try:
#         return x / 0
#     except(ZeroDivisionError):
#         return "Python doesnt know how to divide a number by zero!!!"


# print(div_zero(5))


##############################################

# Question 52
# Question
# Define a custom exception class which takes a string message as attribute.

# Hints
# To define a custom exception, we need to define a class inherited from Exception.

# class TestCustomException(Exception):

#     def __init__(self, message):
#         self.message = message
    
#     def __str__(self):
#         return f'{self.message}'

# error1 = TestCustomException("Invalid Operation, Python cannot handle this!")

# print(error1)

# or

# class MyException(Exception):
#     pass

# error2 = MyException("Wonderful!")

# # print(error2)

# def div_zero(x):
#     try:
#         return x / 0
#     except Exception:
#         raise MyException("very good!")

# print(div_zero(10))

# ##############################################

# Question 53
# Question
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com
# Then, the output of the program should be:

# john
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use \w to match letters.

#################################################



# try:
#     x = input("Enter company mail:\n")
#     result = x.split("@")
#     print(result[0])
# except Exception:
#     raise Exception

# or 

# import re

# text = input("Enter company mail:\n")

# pattern = r"(\w+)"

# match = re.search(pattern, text)

# print(match.group(1))

##############################################

# Question 54
# Question
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com
# Then, the output of the program should be:

# google
# In case of input data being supplied to the question, it should be assumed to be a console input.


# import re 

# text = input("Enter company mail:\n")

# pattern = r"@(\w+)\.com"

# match = re.search(pattern, text)

# print(match.group(1))



# ##############################################
# Question 55
# Question
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

# Example: If the following words is given as input to the program:

# 2 cats and 3 dogs.
# Then, the output of the program should be:

# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use re.findall() to find all substring using regex.

# import re

# # x = input("Enter input:\n")
# x = '2 cats and 3 dogs.'

# pattern = r"(\d+)"

# match = re.findall(pattern, x)

# print(match)

# ##############################################
# Question 56
# Question
# Print a unicode string "hello world".

# Hints
# Use u'strings' format to define unicode string.

# text = u"Hellow world!"

# print(text)

# ##############################################
# Question 57
# Question
# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# Hints
# Use unicode()/encode() function to convert.

# text = "hello world"

# text_ascii = text.encode("ascii")

# text_utf8 = text_ascii.decode('utf-8')

# print(type(text_utf8))

# ##############################################
# Question 58
# Question
# Write a special comment to indicate a Python source code file is in unicode.

# Hints
# Use unicode() function to convert.

# -*- special comment -*-



# ##############################################
# Question 59
# Question
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5
# Then, the output of the program should be:

# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use float() to convert an integer to a float.Even if not converted it wont cause a problem because python by default understands the data type of a value
# ##############################################


# n = int(input("Enter a numb:\n"))

# something = 0

# for numb1 in range(1, n+1):
#     result = float(numb1 / (numb1 + 1))
#     something += result

# print(round(something, 2))
# ##############################################

# Question 60
# Question
# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5
# Then, the output of the program should be:

# 500
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python.


# def somef(n):
#     if n == 0:
#         return 0
#     else:
#         result = somef(n - 1) + 100
#         return result



# print(somef(5))

##############################################

# Question 61
# Question
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.

# Example: If the following n is given as input to the program:

# 7
# Then, the output of the program should be:

# 13
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python.


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

# ##############################################

# Question 62
# Question
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.

# Example: If the following n is given as input to the program:

# 7
# Then, the output of the program should be:

# 0,1,1,2,3,5,8,13
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use string.join() to join a list of strings.


# x = 7


# def get_fib_lst(n):
#     somelst = ["0"]
#     a, b = 0, 1
#     for numb in range(n):
#         a, b = b, a + b
#         somelst.append(str(a))
#     return somelst

# something = get_fib_lst(x)

# result = ",".join(something)

# print(result)




# ##############################################

# Question 63
# Question
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

# Example: If the following n is given as input to the program:

# 10
# Then, the output of the program should be:

# 0,2,4,6,8,10
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use yield to produce the next value in generator.

# x = 10

# even_lst = [str(numb) for numb in range(0, x+1) if numb % 2 == 0]

# def gen(x):
#     for numb in range(0, x+1):
#         if numb % 2 == 0:
#             yield numb

# result = gen(10)
# something = []
# for numb in result:
#     something.append(str(numb))

# real_result = ",".join(something)

# print(real_result)
# ##############################################

# Question 64
# Question
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# Example: If the following n is given as input to the program:

# 100
# Then, the output of the program should be:

# 0,35,70
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use yield to produce the next value in generator.



# def gen(x):
#     for numb in range(0, x+1):
#         if numb % 5 == 0 and numb % 7 ==0:
#             yield numb

# result = gen(100)
# something = []
# for numb in result:
#     something.append(str(numb))

# real_result = ",".join(something)

# print(real_result)



# ##############################################

# Question 65
# Question
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# Hints
# Use "assert expression" to make assertion.

# lst = [2,4,6,8]

# for numb in lst:
#     assert numb % 2 == 0
#     print(numb)


# ##############################################

# Question 66
# Question
# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

# Example: If the following n is given as input to the program:

# 35 + 3
# Then, the output of the program should be:

# 38
# Hints
# Use eval() to evaluate an expression.

Here. 







# ##############################################

# Question 67
# Question
# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

# Hints
# Use if/elif to deal with conditions.

# ##############################################

# Question 68
# Question
# Please generate a random float where the value is between 10 and 100 using Python module.

# Hints
# Use random.random() to generate a random float in [0,1].

# ##############################################

# Question 69
# Question
# Please generate a random float where the value is between 5 and 95 using Python module.

# Hints
# Use random.random() to generate a random float in [0,1].


# ##############################################
 
# Question 70
# Question
# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# Hints
# Use random.choice() to a random element from a list.

# ##############################################

##############################################


# Question 71
# Question
# Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

# Hints
# Use random.choice() to a random element from a list.

# Question 72
# Question
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

# Hints
# Use random.sample() to generate a list of random values.

# Question 73
# Question
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

# Hints
# Use random.sample() to generate a list of random values.

# Question 74
# Question
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

# Hints
# Use random.sample() to generate a list of random values.

# Question 75
# Question
# Please write a program to randomly print a integer number between 7 and 15 inclusive.

# Hints
# Use random.randrange() to a random integer in a given range.

# Question 76
# Question
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

# Hints
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.

# Question 77
# Question
# Please write a program to print the running time of execution of "1+1" for 100 times.

# Hints
# Use timeit() function to measure the running time.

# Question 78
# Question
# Please write a program to shuffle and print the list [3,6,7,8].

# Hints
# Use shuffle() function to shuffle a list.

# Question 79
# Question
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# Hints
# Use list[index] notation to get a element from a list.

# Question 80
# Question
# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

# Hints
# Use list comprehension to delete a bunch of element from a list.

# Question 81
# Question
# By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.

# Question 82
# Question
# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

# Question 83
# Question
# By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

# Question 84
# Question
# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# Hints
# Use list comprehension to make an array.

# Question 85
# Question
# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple.

# Question 86
# Question
# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# Hints
# Use list's remove method to delete a value.

# Question 87
# Question
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

# Hints
# Use set() and "&=" to do set intersection operation.

# Question 88
# Question
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

# Hints
# Use set() to store a number of values without duplicate.

# Question 89
# Question
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# Hints
# Use Subclass(Parentclass) to define a child class.

# Question 90
# Question
# Please write a program which count and print the numbers of each character in a string input by console.

# Example: If the following string is given as input to the program:

# abcdefgabc
# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
# Hints
# Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.

# Question 91
# Question
# Please write a program which accepts a string from console and print it in reverse order.

# Example: If the following string is given as input to the program:*

# rise to vote sir
# Then, the output of the program should be:

# ris etov ot esir
# Hints
# Use list[::-1] to iterate a list in a reverse order.

# Question 92
# Question
# Please write a program which accepts a string from console and print the characters that have even indexes.

# Example: If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:

# Helloworld
# Hints
# Use list[::2] to iterate a list by step 2.

# Question 93
# Question
# Please write a program which prints all permutations of [1,2,3]

# Hints
# Use itertools.permutations() to get permutations of list.

# Question 94
# Question
# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# Hints
# Use for loop to iterate all possible solutions.

# Question 95
# Question
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# If the following string is given as input to the program:

# 5
# 2 3 6 6 5
# Then, the output of the program should be:

# 5
# Hints
# Make the scores unique and then find 2nd best number

# Question 96
# Question
# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

# If the following string is given as input to the program:

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
# Hints
# Use wrap function of textwrap module

# Question 97
# Question
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
# Hints
# First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.

# Question 98
# Question
# You are given a date. Your task is to find what the day is on that date.

# Input

# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

# 08 05 2015
# Output

# Output the correct day in capital letters.

# WEDNESDAY
# Hints
# Use weekday function of calender module

# Question 99
# Question
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input

# The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Output

# Output the symmetric difference integers in ascending order, one per line.

# 5
# 9
# 11
# 12
# Hints
# Use '^' to make symmetric difference operation.

# Question 100
# Question
# You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# If the following string is given as input to the program:

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Then, the output of the program should be:

# 3
# 2 1 1
# Hints
# Make a list to get the input order and a dictionary to count the word frequency

# Question 101
# Question
# You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

# If the following string is given as input to the program:

# aabbbccde
# Then, the output of the program should be:

# b 3
# a 2
# c 2
# d 1
# e 1
# Hints
# Count frequency with dictionary and sort by Value from dictionary Items