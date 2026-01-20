# print("Hellow world!")


# ////////////////////////////////////////////////////////////////
# Lesson: What Is OOP? 
# Object oriented programming is creating your own data type objects and working with it. custom data types. 

# Object-oriented programming means you create your own data types and write your program by working with those data types. Those data types also define what can be done with the data. 

# Why is this usefull? example, Amazone -> delivery drones needed to transport packages. because complicated. to make code more manageable, use OOP. easier to maintain, extend and write. example, to code a custom data type: object; which is the propellors which allows the drone to fly, another example is signalling to signal and give status. another dev works on camera and works on the vision of the drone. this breaks up the funtionality in different pieces, that model the real world into seperate objects. so that different people can work on different parts and then they can combine them afterwards. 

# OOP is a method of dividing and conquiring in programming where you can seperate a whole goal/functionality into smaller objects and work to complete the objective in organized manner trough the use of creating different custom data types and then combining them. 
# ////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////
# Lesson: What is OOP? Part 2

# class BigObject:
#     pass

# obj1 = BigObject()

# print(type(obj1))

# every new word in a new datatypse has to have a capital letter. 
# A class is a blueprint of the object. from that blueprint you are able to create different objects over and over using this blueprint as the building block. 

# Class -> Instantiate -> Instances 

# Class         = New DataType
# Instantiate   = Create the New Datatype
# Instance      = Object based on the New Datatype

# Instantiating a new class, allows for programmers to refer back to that one code block without keep repeating and going over new code in order work with a new data type like a function, because instiatntiating a new class would be asigning python the code to memory where you can always then reuse it. 
# ////////////////////////////////////////////////////////////////





# ////////////////////////////////////////////////////////////////
# Lesson:

# new classes usualy are in singular not plural because it is a blueprint. And from this blueprint which is the class, we can create more objects, so that is why classes are usually defined as singular. like here the example here below:

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print('run')
#         return 'done'

# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
# player2.attack = 50


# print(player1)
# print(player2)


# so self is like append to list, but for instantiating a new class. and whenever you use the self method in creating a new class or adding a new parameter to the class you use self. so that the class has a new 'attribute'.
# which makes the the class dynamic, based on the attributes on what we assign it to be.  

# player one and player 2 are at different location in memory. This way we are able to keep things safe. 
# ////////////////////////////////////////////////////////////////

# Define the class
# class Car:
#     def __init__(self, make, model, year):
#         # Initialize attributes
#         self.make = make
#         self.model = model
#         self.year = year

#     # Define a method
#     def display_info(self):
#         print(f"Car: {self.year} {self.make} {self.model}")


# # Create an object of the class
# my_car = Car("BrandName", "ModelName", 2023)

# # Call the method
# my_car.display_info()


# /////////////////////////////////////////////////////////////////////////


# Exercise:
# Create a class called Book that has:

# Attributes: title, author, pages.

# A method summary() that prints a short description of the book.

# Then, create an object of the class and call the method.

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def summary(self):
#         print(f"Title: {self.title}\n"
#         f"Author: {self.author}\n"
#         f"Pages: {self.pages}")


# putin_bio = Book("Putins Biography", "Putin", 310)

# putin_bio.summary()



# ////////////////////////////////////////////////////////////////
# Lesson: Attributes and Methods

# by typing help then object like here under you can get the full code template so you dont have to search into the code what the hack a object is. This explains the whole object code which is very very nice. 

# help(Book)

# class PlayerCharacter:
#     # Class Object Attribute , not dynamic
#     membership = True
#     def __init__(self, name, age):
#         if (self.membership):
            
#             self.name = name #attributes, are dynamic
#             self.age = age

#     def shout(self):
#         print(f'my name is {self.name}')

# player1 = PlayerCharacter('cindy', 44)
# player2 = PlayerCharacter('Tom', 21)


# print(player2.membership)
# print(player1.membership)

# print(player2.shout())
# ////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////
# Lesson:



# ////////////////////////////////////////////////////////////////