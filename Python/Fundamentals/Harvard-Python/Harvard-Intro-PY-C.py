
# # #Ask user for their name
# name = input('Whats\'s your name?\n').strip().title()

# # #Say hello to user

# # F-string concatenation
# print(f'Hello, {name}')



# /////////////////////
# Remove whitespace from str ; method. 
# name = name.strip()

# Captilize user's name
# name = name.title()

# Spit user's name into first name last name
# first, last = name.split(" ")

# concatination
# print("hello, ", end='')
# print(name)
# /////////////////////

# Pseudo code, is basically an step-plan where you first write down every step what you are going to do to divide the problems into small blocks and know what you must do and convert it into python language code where then begin the actually code based on the step by step comments you made.
# ////////////////////////


# int are whole numbers without decimal points, and python allows us to perform mathematical operations in code. The % operator is called the modulo operator, which returns the remainder after a division. 
# /////////////////////////////////////////////
# NOTES
# /////////////////////////////////////////////
# Harvard Python C Notes

# In an IDE or terminal, you can press the Tab key after typing a few letters to let the terminal auto-complete the file or folder name you want to access or execute.
# //
# You can also use the up and down arrow keys to access the command you previously entered in the terminal or IDE.
# //
# When you want to use an integer variable with the input() function, you can nest functions. This means placing one function call inside another function call so that the return value of the inner function becomes the argument of the outer function.

# This is similar to mathematics: you solve expressions from the inside outward, first calculating what is inside the parentheses, and then using that result in the outer expression.

# So first the innermost parentheses are evaluated, and then you work outwards  in turn using that result.
# //
# Readability is more important that letting code nest into each other, for example to code everything in one line. 
# //
# A string is a sequence of text.

# An integer is an integer like -1, 0 and 1.

# A float is a number with a decimal point. 
# //
# Its properly called a floating point value. you can think of the floating point as a decimal that might have some numbers with the digits to the left or the right. mathematical its a real number.

# If you want to support floating point values in your code.

# instead of:
# x = int(input("What's x?"))

# you do:
# x = float(input("What's x?"))

# and you would get an output with a floating point values, which in return you can do floating point arithmetic with that. so essentially you can work or code with numbers that has decimal values.
# //
# If you want to support the user typing in floating point values with decimal points but you want an integer value that has been rounded, for instance for the nearest integer.
# //
# Round function:

# function(argument[, optional argument]):

# round(number[, ndigits])

# if you don't specify a number of digits you just specify the number to round it rounds to the nearest integer. 

# but in the instance that you do want to specify the number of decimals you specify that by writing a the numbers of decimals in the optional argument place which is suposed to be at ndigits if you look at the round function.
# //
# x ...
# y ...

# z = round(x + y) -> you would get here the rounded result of x plus y.

# This helps with the readability and is easier for the coder that wants to work one at the time especially  if you want to commenting on each of these chunks of code.
# //
# Some countries use , or . for every 3 deciamals points or for every 000. by looking at the python document you can search and do this:

# print(f"{z:,}")
# by doing this you will get
# 1,000 which is 1000.
# //
# floats cannot represent number infinitely precisely. because a computer has only a finite amount of memory. so at some point the computer will then round the number.
# //

# Division:
# /

# code:
# z = round(x / y, 2)

# terminal:
# x =2
# y =3

# output:
# 0.67
# //

# code:
# print(f"{z:.2f}")
# output:
# 0.67

# so here is again that you can look up in the python documentation to do that with less code in one line where you can just add a optional argument in the print function code line to have a floating point value with 2 decimal points. Solving the same problem in multiple ways.
# //
# If you want to make your own function you use the python keyword def for define. this keyword allows you to code a customized function that you want. for example if you want to have a Hello function which does not exist, but the function of this yet to be function is to say hello username asking first the name of the user, by which you can keep using this function whenever you want without writing the same code of block again and again. you can make a hello function by using the python keyword def, which stands for define. with def you can make custom function, specialized function you have made. so you only have to code the function one time and you can call it by simply using the customized function name.

# name = input("What's your name?")
# print(f"Hello, {name})
# //
# Now it is this above code that i want to have a function as and i dont want to repeat in coding this. so i make a custom function called; hello() function.

# def hello(to="World"):
#     print(f"Hello, {to}")


# name = input("What's your name? ")

# hello()
# //
# If you use a custom function it must already exist by the time you are calling it. in other words you must code in order to access the function by first coding the custom function. Logically, top to bottom.
# //
# def main():

# This connotes to the reader that this the main part of the program.
# //
# The method bellow allows me to organize my file and define functions in any order I want. By placing main() at the point where I want the program to start, I can control the flow of execution and avoid issues with Python not recognizing functions before they are called. This approach ensures that each function is clearly defined and that the program runs in a predictable, structured way.

# Explanation / correction of facts:

# In Python, functions must be defined before they are called, otherwise you’ll get a NameError.

# Placing main() at the “top” of the file doesn’t matter by itself; what matters is that the function definitions for anything main() calls must appear before main() is executed.

# Your original code works because hello() is defined before main() is called at the bottom.

# def main():
# 	name = input("What's your name? ")
# 	hello(name)
	
# def hello(to="World"):
#     print(f"Hello, {to}")

# main()
# //
# Scope is about where a variable or function can be accessed. Variables defined inside a function are local to that function and cannot be accessed from outside, while variables defined outside functions are global and can be accessed inside functions unless a local variable with the same name exists. 
# //
# return
# To use a local variable outside the function, the function must return it. The key idea is that local variables exist only within their function, and return allows their values to be used elsewhere, while print only displays them.
# //
# /////////////////////////////////////////////
# calculator

# x = int(input(f"What's x?\n"))
# y = int(input(f"What's y?\n"))

# z = x + y

# print(f"z = {z}")

# ////////////////////////////////

# def hello(to="World"):
#     print(f"Hello, {to}")


# name = input("What's your name? ")

# hello()

# ///////////////////////

# def main():
#     x = int(input("what's x? "))
#     print(f"x squared is", square(x))


# def square(n):
#     return n ** 2

# main()
# ///////////////////////////

# End of first lesson!!!

# ///////////////////////////////////////////////////////



# /////////////////////////////
# Lesson 2: Conditionals:
# /////////////////////////////

# compare
# x = int(input("What's x?\n"))
# y = int(input("What's y?\n"))


# //
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# # elif x == y:
# #     print("x is equal to y")
# # This would not be necassary as the only other option availble would be the logic hereunder. so you would not need to ask the question for it. and can directly give the condition of else. 
# else:
#     print("x is equal to y")

# //

# if x != y:
# # if x < y or x >y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# //

# grade

# score = int(input("Score: \n"))

# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score <= 90:
#     print("Grade: B")
# elif score >= 70 and score <= 80:
#     print("Grade: C")
# elif score >= 60 and score <= 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


# make it more efficient
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score <= 90:
#     print("Grade: B")
# elif 70 <= score <= 80:
#     print("Grade: C")
# elif 60 <= score <= 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


# make it even more efficient
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# //

# parity


# def main():
#     x = int(input("What's x?\n"))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False





