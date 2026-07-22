# bbut isnt this just functional programming what you are trying to make me hammer

# Exercise:

# Greeting function
# Goodbye function
# Print a box of stars
# Print your name five times


# Greeting funciton:

def greet():
    print('Hello wonderful person!')


# Goodbye function

def valediction():
    print('Goodbye and may peace be upon you!')


# Print a box of stars

def box_of_stars():

    # width 
    a = int(input('Please enter the width for the specified box of stars you want to request:\n'))

    # height 
    b = int(input('Please enter the height for the specified box of stars you want to request:\n'))

    for element in range(1, b + 1):
        print("*" * a)
        


# Print your name five times

def name_announcement_x5(name="Stranger!"):
    # This time i gonna try it with a parameter
    result = (name +" ") * 5
    print(result)


# box_of_stars()

# name_anouncement_x5()


#######################################################
# Next Topic: Return Values (return) ⭐⭐⭐⭐⭐
#######################################################


# Exercises

# Don't skip these.

# 1. Add two numbers

# Make a function that returns the sum.


def add(x, y):
    return x + y

# result = add(10, 15)

# print(result)



# 2. Multiply two numbers

# Return the product.



def multiply(x, y):
    return x * y

# result = multiply(5, 4)

# print(result)



# 3. Find the largest number

# Example:

# largest = max_number(10, 20)

# print(largest)

# Output:

# 20



def largest_numb(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return f"{x} and {y} are equel"

# result = largest_numb(2, 8)

# print(result)




# 4. Is Even?

# Return True or False.

# Example:

# print(is_even(10))

# Output:

# True

def is_even(x):
    return x % 2 == 0

result = is_even(17)

print(result)


# 5. Grade Checker

# Input:

# 95

# Return:

# "A"

# Don't print inside the function.

# Return it.


def grade_check(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

# result = grade_check(78)

# print(result)




# 6. BMI Calculator

# Input:

# height // weight

# Return:

# BMI


def bmi_stat(weight, height):
    return weight / (height ** 2)

result = bmi_stat(140, 1.69)

print(result)


# 7. Rectangle Area

# Input:

# width
# height

# Return:

# area



def rect_area(width, height):
    return width * height

# result = rect_area(8, 8)

# print(result)




# 8. Temperature Converter

# Celsius → Fahrenheit

# Return the converted temperature.


def tempcc_to_f(c):
    return round(c * (9 / 5) + 32, 2)

# result = tempcc_to_f(26)

# print(result)

