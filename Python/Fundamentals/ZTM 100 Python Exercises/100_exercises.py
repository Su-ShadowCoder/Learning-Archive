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

random = [1,2,3,4,5,6,7,8,9,10]

# Hints:
# Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.

square_even_lst = [map()]































# #################################################
# Question 43
# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.Use lambda to define anonymous functions.

# #################################################

# Question 44
# Question:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.

# ###################################
# Question 45
# Question:
# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.

# ###################################
# Question 46
# Question:
# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.*

# ###################################
# Question 47
# Question
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

# ###################################
# Question 48
# Question
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

# ###################################
# Question 49
# Question
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints
# To override a method in super class, we can define a method with the same name in the super class.

# ###################################
# Question 50
# Question
# Please raise a RuntimeError exception.

# Hints
# UUse raise() to raise an exception.

# ###################################