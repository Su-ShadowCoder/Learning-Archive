# ============================================
# SHORT EXAMPLES FOR INDIVIDUAL TOPICS
# ============================================

# # 1. Classes, Attributes, Methods, __init__
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def summary(self):
#         print(f"{self.title} by {self.author}")

# # 2. @classmethod and @staticmethod
# class Library:
#     books_count = 0

#     @classmethod
#     def increment_count(cls):
#         cls.books_count += 1

#     @staticmethod
#     def is_open(hour):
#         return 9 <= hour <= 17

# # 3. Encapsulation, Abstraction, Private/Public Variables
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # private

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# # 4. Inheritance and Polymorphism
# class Vehicle:
#     def move(self):
#         print("The vehicle is moving")

# class Car(Vehicle):
#     def move(self):
#         print("The car is driving smoothly")  # polymorphism

# ============================================
# EXERCISES COMBINING ALL TOPICS
# ============================================

# Exercise 1: Zoo Management System
# ----------------------------------
# Create a mini zoo system that tracks animals and staff.
# Requirements:
# - Create classes for Animals and Staff with attributes and methods
# - Use __init__ to initialize objects
#  - Implement at least one classmethod and one staticmethod
#  - Apply encapsulation for sensitive data (like salaries or health stats)
# - Include inheritance (e.g., Mammal, Bird) and polymorphism (override methods)
#  - Include both private and public variables
# Task: Design the classes and write code to simulate adding animals, hiring staff, and displaying info

# import textwrap

# class Zoo_Management_System():
#     def __init__(self, name, branch):
#         self.name = name
#         self.branch = branch


#     @staticmethod
#     def zoo_is_open(hour):
#         return 9 <= hour <= 17

#     def __str__(self):
#         return f"ZOO: {self.name}, Branch: {self.branch}."

# Zoo_Amsterdam = Zoo_Management_System("Artis", "Amsterdam")
# # print(Zoo_Amsterdam.zoo_is_open(20))

# class Staff(Zoo_Management_System):
#     def __init__(self, staff_name, staff_age, staff_gender, staff_roles, staff_salaries):
#         self.staff_name = staff_name
#         self.staff_age = staff_age
#         self.staff_gender = staff_gender
#         self.staff_roles = staff_roles
#         self._staff_salaries = staff_salaries

#     def __str__(self):
#         return textwrap.dedent(f"""
#         Staff name:     {self.staff_name}
#         Staff age:      {self.staff_age}
#         Staff gender:   {self.staff_gender}
#         Staff role:     {self.staff_roles}
#         Staff salary:   ${self._staff_salaries}
#         """)


# staff_1 = Staff("Natalie Heywood", 31, "female", "Head Care Taker", 4000)
# staff_2 = Staff("Andrew Pipehouse", 27, "male", "Care taker", 2000)
# staff_3 = Staff("Romanov Slovaski", 21, "male", "Assistant Care taker", 1500)
# staff_4 = Staff("Ariana Spielburg", 24, "female", "Cook", 2000)
# staff_5 = Staff("Sumisha Coleman", 29, "female", "Veterinarian", 5000)
# staff_6 = Staff("Gregory Mayweather", 35, "male", "Administrator", 4000)

# class Caretakers(Staff):
    
#     def feed_animal(self):
#         return "Feed animals according to type-specific diet."
#     def maintain_cleaning(self):
#         return "Maintain and clean enclosures."

# class Veterinarians(Staff):

#     def ex_health_check(self):
#         return "Conduct health checks."
#     def pres_treatment(self):
#         return "Prescribe treatment if needed."

# class Cooks(Staff):

#     def meal_prep(self):
#         return "Prepare meals for different animal types"
#     def food_s_h(self):
#         return "Ensure food safety and hygiene"

# class Administration(Staff):

#     def track_rec(self):
#         return "Track records of animals and staff"
#     def supp_inventory(self):
#         return "Manage supplies inventory"


# class Animals(Zoo_Management_System):
#     total_animals = 0

#     def __init__(self, animal, name, age, condition, _type):
#         self.animal = animal
#         self.name = name
#         self.age = age
#         self.condition = condition
#         self._type = _type
        
#         if type(self) is Animals:
#             Animals.increment_animals()
    
#     def __str__(self):
#         return textwrap.dedent(f"""
#         Animal:     {self.animal}
#         Name:       {self.name}
#         Age:        {self.age}
#         Condition:  {self.condition}
#         Type:       {self._type}
#         """)

#     @classmethod
#     def increment_animals(cls):
#             cls.total_animals += 1
        

#     @classmethod
#     def display_total_animal(cls):
#         return f"Total Animals: {cls.total_animals} in {Zoo_Amsterdam}"

    

    

#     def check_condition(self):
#         if self.condition == "Healthy":
#             return "Status: OK"
#         elif self.condition == "Recovering":
#             return "Need Regurlar Medical Check and Care"
#         else:
#             return "Please attend attend the animal to the veteranian!"

# leo = Animals("Lion", "Leo", 5, "Healthy", "Mammal")
# bella = Animals("Parrot", "Bella", 3, "Injured", "Bird")
# max_ = Animals("Elephant", "Max", 7, "Healthy", "Mammal")
# kiwi = Animals("Kiwi", "Kiwi", 2, "Sick", "Bird")
# sammy = Animals("Turtle", "Sammy", 1, "Healthy", "Reptile")
# daisy = Animals("Dog", "Daisy", 4, "Recovering", "Mammal")
# rocky = Animals("Snake", "Rocky", 6, "Healthy", "Reptile")
# polly = Animals("Cockatoo", "Polly", 8, "Injured", "Bird")
# tiger = Animals("Tiger", "Tiger", 5, "Healthy", "Mammal")
# nibbles = Animals("Guinea Pig", "Nibbles", 2, "Healthy", "Rodent")

# class Mammal(Animals):
#     def food_type(self):
#         return "Food: Meat and plants."
#     def health_check(self):
#         return "Weekly health check ups."

# leo = Mammal("Lion", "Leo", 5, "Healty", "Mammal")
# max_ = Mammal("Elephant", "Max", 7, "Healthy", "Mammal")
# daisy = Mammal("Dog", "Daisy", 4, "Recovering", "Mammal")
# tiger = Mammal("Tiger", "Tiger", 5, "Healthy", "Mammal")

# # print(leo.food_type(), leo.health_check())

# class Bird(Animals):
# # Need perches or flight space
#     def living_env(self):
#         return "Need Perches or flight space."
# # Daily feather inspections
#     def health_check(self):
#         return "Daily feather inpsections"

# bella = Bird("Parrot", "Bella", 3, "Injured", "Bird")
# kiwi = Bird("Kiwi", "Kiwi", 2, "Sick", "Bird")
# polly = Bird("Cockatoo", "Polly", 8, "Injured", "Bird")


# class Rodent(Animals):
#     def life_support(self):
#         return "Heat lamps and controlled humitiy"
# # Heat lamps and controlled humidity
#     def living_env(self):
#         return "Habitat mimics natural environment"
# # Habitat mimics natural environment

# nibbles = Rodent("Guinea Pig", "Nibbles", 2, "Healthy", "Rodent")


# class Reptile(Animals):
#     def food_type(self):
#         return "Fresh food."
#     def life_support(self):
#         return "bedding."
#     def living_env(self):
#         return "Space to dig and hide."
# # Fresh food and bedding
# # Space to dig and hide

# sammy = Reptile("Turtle", "Sammy", 1, "Healthy", "Reptile")
# rocky = Reptile("Snake", "Rocky", 6, "Healthy", "Reptile")

# print(Animals.display_total_animal())


# # Exercise 2: Online Learning Platform
# # ------------------------------------
# # Build a system for courses and users.
# # Requirements:

# # Phase 1. 
# # - Create a base User class and specialized Student and Instructor classes
# # - Use __init__ for attributes like name, role, and courses


# # Phase 2. 
# # - Implement classmethods for counting users and staticmethods for checking enrollment eligibility

# # Phase 3. 
# # - Use private variables for sensitive info (like passwords) and encapsulate access with methods

# # Phase 4
# # - Apply inheritance (Student, Instructor) and polymorphism (override methods to display info differently)

# # Phase 5
# # Task: Simulate enrolling students, assigning courses, and displaying course info


# class ZZZAcadamy:
#     def _init_(self, name, website, courses):
#         self.name = name
#         self.website = website


# class Users(ZZZAcadamy):
#     def _init_(self, name, age):
#         self.name = name
#         self.__password = password

#     def check_password(self, password):
#         return password == self.__password

# class Courses():
#     max_students = 20

#     def __init__(self, course_name, course_instructor, max_students):
#         self.course_name = course_name
#         self.course_instructor = course_instructor
#         self.max_students = max_students


# class Instructor(User):
#     def _init_(self, name, __password, role, _salary, courses):
#         super().__init__(name, __password)
#         self.role = role
#         self. __salary = salary
#         self.courses = courses

#     def get_salary(self):
#         return self.__salary
#     def get_role(self):
#         return self.role
#     def add_instructor_course(self):



# class Student(User):
#     minimum_student_age = 18
#     def _init_(self, name, __password, age, role, courses):
#         super().__init__(name, __password)
#         self._age = age
#         self.role = role
#         self.courses = courses



# def main():
#     pass

# if __name__ == "__main__":
#     main()



# Exercise 3: Banking Application
# --------------------------------
# Create a simplified banking system.
# Requirements:
# - Base Account class with private balance and public owner attribute
# - CheckingAccount and SavingsAccount inherit from Account
# - Use methods to deposit, withdraw, and display balance (polymorphism for different account types)
# - Implement classmethods for tracking total accounts and staticmethods for validating transactions
# - Encapsulate sensitive data and include both private and public variables
# Task: Simulate opening accounts, making transactions, and reporting total accounts





# 🧠 EXERCISE SERIES: OOP FROM ZERO TO COMPOSITION
# 1. Object + attributes only (no methods)
# Theme: Book library (simple storage)

# Create a class Book:

# title
# author
# pages

# Task:

# Create 3 book objects and print their attributes.

# Goal:

# Understand: objects are just structured data containers

# class Book():

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __str__(self):
#         return f"Book:{self.title}, Author:{self.author}, Pages:{self.pages}."

# def main():
#     book_1 = Book("Cooking with Gordon Ramsay", "Gordon Ramsay", 355)
#     book_2 = Book("Patientce", "Tom Hollar", 40)
#     book_3 = Book("EMT when far away", "Dr. Anderson", 450)
#     print(book_1)
#     print(book_2)
#     print(book_3)


# if __name__ == "__main__":
#     main()


# ///
# 2. Adding methods (behavior inside object)
# Theme: Car speed system

# Class Car:

# brand
# speed

# Add method:

# drive() → increases speed by 10

# Task:

# Call method multiple times and print speed.

# Goal:

# Understand: methods modify internal state


# class Car():

#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def __str__(self):
#         return f"Car brand:{self.brand}, Car Speed{self.speed}."

#     def drive(self):
#         self.speed += 10

# def main():
#     car1 = Car("Toyota", 50)
#     car2 = Car("Audi", 110)

#     print(car1)
#     car1.drive()
#     car1.drive()
#     print(car1)
#     print(car2)
    


# if __name__ == "__main__":
#     main()

# ///

# 3. Encapsulation (private attribute idea)
# Theme: Bank account

# Class BankAccount:

# owner
# balance (should NOT be directly modified)

# Add method:

# deposit(amount)
# get_balance()

# Rule:

# Do NOT access balance directly outside class.

# Goal:

# Understand: control access to data

# class BankAccount():

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
    
#     def __str__(self):
#         return f"{self.owner}, {self.__balance} Euro's"

#     def deposit(self, x):
#         self.__balance += x

#     def get_balance(self):
#         return self.__balance



# b_a_richard_blanks = BankAccount("Richard Blanks", 2100)

# print(b_a_richard_blanks)
# b_a_richard_blanks.deposit(1000)
# print(b_a_richard_blanks.get_balance())

# ///

# 4. Input + method interaction
# Theme: Login system

# Class User:

# username
# password (private)

# Method:

# check_password(input_password)
# Task:

# Ask user input and verify login.

# Goal:

# Understand: objects process external input


# class User():
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def get_usr_username(self):
#         return self.username

#     def check_password(self, x):
#         if  x == self.__password:
#             return True

# mikebik = User("admin", 1234)

# def mikebik_login():
#     usr_input_u = input("Please enter Username:\n")
#     if usr_input_u == mikebik.username:
#         usr_input_p = int(input("Please enter Password:\n"))
#         if mikebik.check_password(usr_input_p):
#             print(f"Access Granted")
#         else:
#             print(f"Access denied, please try again!")
#     else:
#         print(f"Username not registerd, please try again!")



# mikebik_login()
# ///

# ///

# 5. Class variables (shared data)
# Theme: Student counter

# Class Student:

# name
# class variable: total_students

# Every time a student is created → counter increases

# Goal:

# Understand: data shared across all objects

# class Student():
#     total_students = 0
    
#     def __init__(self, name, age, s_class):
#         self.name = name 
#         self.age = age 
#         self.s_class = s_class
#         Student.total_students += 1

#     @classmethod
#     def s_count(cls):
#         return cls.total_students

# s_kamal_bibi = Student("Kamal Bibi", 17, "1A")
# s_kamal_bibi = Student("Kamal Bibi", 17, "1A")
# s_kamal_bibi = Student("Kamal Bibi", 17, "1A")


# print(Student.s_count())

# 6. Class methods (@classmethod concept)
# Theme: Company system

# Class Employee:

# name
# salary

# Add:

# class method get_average_salary(all_employees)
# Goal:

# Understand: methods that work on the class level, not instance level

# class Employee():
#     all_employees = []
#     total_employee = 0
    


#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary
#         Employee.total_employee += 1
#         Employee.all_employees.append(self)


#     @classmethod
#     def total_salary(cls):
#         total = 0
#         for element in cls.all_employees:
#                 total += element._salary
#         return total

#     @classmethod
#     def avg_salary(cls):
#         avg_sal = cls.total_salary() / cls.total_employee
#         return avg_sal
    

# emp1 = Employee("Richard Edward", 3500)
# emp2 = Employee("Mike Ross", 3000)
# emp3 = Employee("Louis Piers", 4000)

# print(Employee.total_salary())
# print(Employee.avg_salary())


# 7. Static methods (no object needed)
# Theme: Math utilities

# Class MathTools

# Add:

# static method is_even(number)
# static method square(number)
# Rule:

# Do NOT use self

# Goal:

# Understand: function inside class that doesn’t depend on object



# class MathTools():
    
#     @staticmethod
#     def is_even(x):
#         return x % 2 == 0

#     @staticmethod
#     def square(y):
#         s = y ** 2
#         return s

# print(MathTools.is_even(44))
# print(MathTools.square(8))

# 8. Inheritance (basic reuse)
# Theme: Animals

# Base class: Animal

# name

# Child classes:

# Dog
# Cat

# Each has method:

# speak() (different output)
# Goal:

# Understand: shared structure + specialized behavior


# class Animal:
    
#     def __init__(self, name):
#         self.name = name


# class Bunny(Animal):
#     pass

#     def speak(self):
#         return "'squek'!, squek'!"

# class Cat(Animal):

#     def speak(self):
#         return "'Meeeoow'!"

# simba = Cat("Simba")
# sunny = Bunny("Sunny")

# print(simba.speak())
# print(sunny.speak())

# 9. Polymorphism (same method, different behavior)
# Theme: Shapes

# Base class: Shape

# method area()

# Subclasses:

# Square
# Circle

# Each implements area() differently.

# Task:

# Loop through shapes and call .area() on all.

# Goal:

# Understand: same interface, different behavior

# class shape:
#     pass

#     def area(self):
#         raise NotImplementedError

# class Square(shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height

# class Circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.pi = 3.14
    
#     def area(self):
#         return self.radius ** 2 * self.pi

# yellow = Circle(5)
# print(yellow.area())


# 10. Composition (objects inside objects)
# Theme: Online shop

# Classes:

# Product (name, price)
# Cart (contains products)

# Cart methods:

# add product
# calculate total
# Goal:

# Understand:

# objects can contain OTHER objects



# class Product:
#     all_products = []
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.all_products.append(self)
    
#     @classmethod
#     def get_all_products(cls):
#         for p in cls.all_products:
#             print(p.name)


# class Cart:
#     def __init__(self):
#         self.product_container = []

#     def get_product_container(self):
#         for element in self.product_container:
#             print(element.name)

#     def add_product(self, product):
#         self.product_container.append(product)

#     def total_price(self):
#         total_price = 0
#         for p in self.product_container:
#             total_price += p.price
#         return total_price

# milk = Product("Milk", 2)
# chocolate = Product("Chocolate", 1)
# cheese = Product("Cheese", 4)

# cart1 = Cart()

# cart1.add_product(milk)
# cart1.add_product(cheese)

# print(cart1.total_price())

# cart1.get_product_container()

# Product.get_all_products()

# print(add_product())
# //////////////////////////////////////////////
