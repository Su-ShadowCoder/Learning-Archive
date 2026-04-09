# ============================================
# SHORT EXAMPLES FOR INDIVIDUAL TOPICS
# ============================================

# 1. Classes, Attributes, Methods, __init__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def summary(self):
        print(f"{self.title} by {self.author}")

# 2. @classmethod and @staticmethod
class Library:
    books_count = 0

    @classmethod
    def increment_count(cls):
        cls.books_count += 1

    @staticmethod
    def is_open(hour):
        return 9 <= hour <= 17

# 3. Encapsulation, Abstraction, Private/Public Variables
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# 4. Inheritance and Polymorphism
class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving smoothly")  # polymorphism

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

import textwrap

class Zoo_Management_System():
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


    @staticmethod
    def zoo_is_open(hour):
        return 9 <= hour <= 17

    def __str__(self):
        return f"ZOO: {self.name}, Branch: {self.branch}."

Zoo_Amsterdam = Zoo_Management_System("Artis", "Amsterdam")
# print(Zoo_Amsterdam.zoo_is_open(20))

class Staff(Zoo_Management_System):
    def __init__(self, staff_name, staff_age, staff_gender, staff_roles, staff_salaries):
        self.staff_name = staff_name
        self.staff_age = staff_age
        self.staff_gender = staff_gender
        self.staff_roles = staff_roles
        self._staff_salaries = staff_salaries

    def __str__(self):
        return textwrap.dedent(f"""
        Staff name:     {self.staff_name}
        Staff age:      {self.staff_age}
        Staff gender:   {self.staff_gender}
        Staff role:     {self.staff_roles}
        Staff salary:   ${self._staff_salaries}
        """)


staff_1 = Staff("Natalie Heywood", 31, "female", "Head Care Taker", 4000)
staff_2 = Staff("Andrew Pipehouse", 27, "male", "Care taker", 2000)
staff_3 = Staff("Romanov Slovaski", 21, "male", "Assistant Care taker", 1500)
staff_4 = Staff("Ariana Spielburg", 24, "female", "Cook", 2000)
staff_5 = Staff("Sumisha Coleman", 29, "female", "Veterinarian", 5000)
staff_6 = Staff("Gregory Mayweather", 35, "male", "Administrator", 4000)

class Caretakers(Staff):
    
    def feed_animal(self):
        return "Feed animals according to type-specific diet."
    def maintain_cleaning(self):
        return "Maintain and clean enclosures."

class Veterinarians(Staff):

    def ex_health_check(self):
        return "Conduct health checks."
    def pres_treatment(self):
        return "Prescribe treatment if needed."

class Cooks(Staff):

    def meal_prep(self):
        return "Prepare meals for different animal types"
    def food_s_h(self):
        return "Ensure food safety and hygiene"

class Administration(Staff):

    def track_rec(self):
        return "Track records of animals and staff"
    def supp_inventory(self):
        return "Manage supplies inventory"


class Animals(Zoo_Management_System):
    total_animals = 0

    def __init__(self, animal, name, age, condition, _type):
        self.animal = animal
        self.name = name
        self.age = age
        self.condition = condition
        self._type = _type
        
        if type(self) is Animals:
            Animals.increment_animals()
    
    def __str__(self):
        return textwrap.dedent(f"""
        Animal:     {self.animal}
        Name:       {self.name}
        Age:        {self.age}
        Condition:  {self.condition}
        Type:       {self._type}
        """)

    @classmethod
    def increment_animals(cls):
            cls.total_animals += 1
        

    @classmethod
    def display_total_animal(cls):
        return f"Total Animals: {cls.total_animals} in {Zoo_Amsterdam}"

    

    

    def check_condition(self):
        if self.condition == "Healthy":
            return "Status: OK"
        elif self.condition == "Recovering":
            return "Need Regurlar Medical Check and Care"
        else:
            return "Please attend attend the animal to the veteranian!"

leo = Animals("Lion", "Leo", 5, "Healthy", "Mammal")
bella = Animals("Parrot", "Bella", 3, "Injured", "Bird")
max_ = Animals("Elephant", "Max", 7, "Healthy", "Mammal")
kiwi = Animals("Kiwi", "Kiwi", 2, "Sick", "Bird")
sammy = Animals("Turtle", "Sammy", 1, "Healthy", "Reptile")
daisy = Animals("Dog", "Daisy", 4, "Recovering", "Mammal")
rocky = Animals("Snake", "Rocky", 6, "Healthy", "Reptile")
polly = Animals("Cockatoo", "Polly", 8, "Injured", "Bird")
tiger = Animals("Tiger", "Tiger", 5, "Healthy", "Mammal")
nibbles = Animals("Guinea Pig", "Nibbles", 2, "Healthy", "Rodent")

class Mammal(Animals):
    def food_type(self):
        return "Food: Meat and plants."
    def health_check(self):
        return "Weekly health check ups."

leo = Mammal("Lion", "Leo", 5, "Healty", "Mammal")
max_ = Mammal("Elephant", "Max", 7, "Healthy", "Mammal")
daisy = Mammal("Dog", "Daisy", 4, "Recovering", "Mammal")
tiger = Mammal("Tiger", "Tiger", 5, "Healthy", "Mammal")

# print(leo.food_type(), leo.health_check())

class Bird(Animals):
# Need perches or flight space
    def living_env(self):
        return "Need Perches or flight space."
# Daily feather inspections
    def health_check(self):
        return "Daily feather inpsections"

bella = Bird("Parrot", "Bella", 3, "Injured", "Bird")
kiwi = Bird("Kiwi", "Kiwi", 2, "Sick", "Bird")
polly = Bird("Cockatoo", "Polly", 8, "Injured", "Bird")


class Rodent(Animals):
    def life_support(self):
        return "Heat lamps and controlled humitiy"
# Heat lamps and controlled humidity
    def living_env(self):
        return "Habitat mimics natural environment"
# Habitat mimics natural environment

nibbles = Rodent("Guinea Pig", "Nibbles", 2, "Healthy", "Rodent")


class Reptile(Animals):
    def food_type(self):
        return "Fresh food."
    def life_support(self):
        return "bedding."
    def living_env(self):
        return "Space to dig and hide."
# Fresh food and bedding
# Space to dig and hide

sammy = Reptile("Turtle", "Sammy", 1, "Healthy", "Reptile")
rocky = Reptile("Snake", "Rocky", 6, "Healthy", "Reptile")

print(Animals.display_total_animal())


# Exercise 2: Online Learning Platform
# ------------------------------------
# Build a system for courses and users.
# Requirements:
# - Create a base User class and specialized Student and Instructor classes
# - Use __init__ for attributes like name, role, and courses
# - Implement classmethods for counting users and staticmethods for checking enrollment eligibility
# - Use private variables for sensitive info (like passwords) and encapsulate access with methods
# - Apply inheritance (Student, Instructor) and polymorphism (override methods to display info differently)
# Task: Simulate enrolling students, assigning courses, and displaying course info

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