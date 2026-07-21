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
