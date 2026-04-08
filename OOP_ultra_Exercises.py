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
# - Implement at least one classmethod and one staticmethod
# - Apply encapsulation for sensitive data (like salaries or health stats)
# - Include inheritance (e.g., Mammal, Bird) and polymorphism (override methods)
# - Include both private and public variables
# Task: Design the classes and write code to simulate adding animals, hiring staff, and displaying info

class Zoo_Management_System():
    pass


class Animals(Zoo_Management_System):
    pass

class Staff(Zoo_Management_System):
    pass

class Mammal(Animals):
    pass

class Bird(Animals):
    pass







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