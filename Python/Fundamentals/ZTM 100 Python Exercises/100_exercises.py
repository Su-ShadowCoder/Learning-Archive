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

