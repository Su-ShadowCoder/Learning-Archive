# 🔥 Exercise 1 — Player System
# 📌 Requirements

# Build a system for players.

# Data:
# Each player has:
# name
# score
# Class behavior:
# There must be a shared list that stores ALL players
# Methods:
# Add each new player to that shared list automatically
# A method that returns the total number of players
# A method that returns the average score of all players
# ⚠️ What I will check
# Did you use self vs cls correctly?
# Where does the list live?
# Are you mixing instance data with class data?
# ////


# class Player:
#     all_players = []
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         Player.all_players.append(self)
    
#     @classmethod
#     def get_all_players(cls):
#         for p in cls.all_players:
#             print(p.name, p.score)

#     @classmethod
#     def total_players(cls):
#         total_p = len(cls.all_players)
#         return total_p

#     @classmethod
#     def total_score(cls):
#         total_s = 0
#         for p in cls.all_players:
#             total_s += p.score
#         return total_s

#     @classmethod
#     def avg_playa_score(cls):
#         avg_playerScore = 0
#         avg_playerScore = cls.total_score() / cls.total_players()
#         print(avg_playerScore)


 
# player_1 = Player("adrew123", 120)
# player_2 = Player("boba_4", 99)
# player_3 = Player("soprano555", 110)

# Player.get_all_players()
# print(Player.total_players())
# print(Player.total_score())
# Player.avg_playa_score()

# ////
# 🔥 Exercise 2 — Order System (Composition)
# 📌 Requirements

# Build a simple order system.

# Classes:
# Item
# has name, price
# Order
# contains a list of items
# Methods:
# Add item to order
# Get total price of order
# Get names of all items in order (list or print)
# ⚠️ What I will check
# Does the list belong to the class or the instance?
# Are you passing objects correctly?
# Are you iterating over objects properly?
# ////

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

    

# class Order:
#     def __init__(self):
#         self.item_lst = []

#     def add_item(self, product):
#         self.item_lst.append(product)

#     def total_price_order(self):
#         total_p = 0
#         for price in self.item_lst:
#             total_p += price.price
#         return f"Total price: {total_p} Euro's"

#     def get_all_itemlist_name(self):
#         all_items = []
#         for item in self.item_lst:
#             all_items.append(item.name)
#         return all_items

# jam = Item("Jam 450g", 1.50)
# rice = Item("Rice 1kg", 2)
# chickenpie = Item("Chickenpie 400g", 1.30)


# Order_basket1 = Order()

# Order_basket1.add_item(jam)
# Order_basket1.add_item(rice)
# Order_basket1.add_item(chickenpie)

# print(Order_basket1.get_all_itemlist_name())
# print(Order_basket1.total_price_order())

# ////
# 🔥 Exercise 3 — Company Salary System
# 📌 Requirements

# Build a company system.

# Data:
# Each employee has:
# name
# salary
# Class behavior:
# Store ALL employees in one shared list
# Methods:
# Get total salary payout (all employees combined)
# Get highest salary
# Get employee count
# ⚠️ What I will check
# Are you using cls correctly for aggregation?
# Are you accessing instance data through objects?
# Are you confusing local variables with class variables?
# ////


# class Employee:
#     employee_list = []
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.employee_list.append(self)

#     @classmethod
#     def get_all_emp(cls):
#         emp = []
#         for element in cls.employee_list:
#             emp.append(element.name)
#         return emp

#     @classmethod
#     def get_total_emp_count(cls):
#         return len(cls.employee_list)
    
#     @classmethod
#     def total_all_emp_Pay_out(cls):
#         total_sal = 0
#         for sal in cls.employee_list:
#             total_sal += sal.salary
#         return total_sal
    
#     @classmethod
#     def get_highest_salary(cls):
#         highest_sal = 0
#         for sal in cls.employee_list:
#             if sal.salary > highest_sal:
#                     highest_sal = sal.salary
#         return highest_sal
    



# emp2 = Employee("Mike Ross", 3500)
# emp3 = Employee("Jessica Pierson", 8000)
# emp4 = Employee("Harvey Specter", 6000)
# emp1 = Employee("Richard Alone", 2000)

# print(Employee.get_all_emp())

# print(Employee.get_total_emp_count())

# print(Employee.total_all_emp_Pay_out())

# print(Employee.get_highest_salary())

# ///////



# ///////

# class Book:
#     all_books = []
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
#         Book.all_books.append(self)


# class Library:
#     def __init__(self):
#         self.lib = []

#     def add_book(self, book):
#         self.lib.append(book)
    
#     def show_all_titles(self):
#         all_titles = []
#         for book in self.lib:
#             all_titles.append(book.name)
#         return all_titles

#     def total_pages_lib(self):
#         total_pages = 0
#         for book in self.lib:
#             total_pages += book.pages
    
#     def get_library(self):
#         library = []
#         for book in self.lib:
#             library.append(f"{book.name}, {book.author}, {book.pages} pages")
#         return library

# # apparantly instead of a tuple you can also use a f string to append multiple things in one container. 


# bk1 = Book("The Silent Horizon", "Elias Verne", 342)
# bk2 = Book("Ashes of Tomorrow","Mira Solen", 287)
# bk3 = Book("The Iron Garden", "Tobias Hale", 415)
# bk4 = Book("Fractured Light", "Noura El-Karim", 198)
# bk5 = Book("Echoes Beneath", "Daniel Cross", 256)

# library_praryfire = Library()

# library_praryfire.add_book(bk1)
# library_praryfire.add_book(bk2)
# library_praryfire.add_book(bk3)

# print(library_praryfire.get_library())

# ///////

# ///////

# class BankAccount:
#     all_bank_accounts = []
#     def __init__(self, owner_name, __balance):
#         self.owner_name = owner_name
#         self.__balance = __balance
#         BankAccount.all_bank_accounts.append(self)

#     @classmethod
#     def total_all_acc_money(cls):
#         total_money = 0
#         for account in cls.all_bank_accounts:
#             total_money += account.__balance # dont make a specific logic for if account goes into minus because the __balance attribute is safeguarded in not being able to access the balance beyond negative trough the withdraw method.
#         return f"Total all Account Balance: {total_money} Euro." 

#     @classmethod
#     def highest_balance_account(cls):
#         first_acc = cls.all_bank_accounts[0]
#         highest_acc_balance = first_acc.__balance
#         for account in cls.all_bank_accounts:
#             if account.__balance > highest_acc_balance:
#                 highest_acc_balance = account.__balance
#                 name = account.owner_name
#         return name, highest_acc_balance

#     @classmethod
#     def get_all_accounts(cls):
#         all_acounts = []
#         for account in cls.all_bank_accounts:
#             all_acounts.append(f"Name: {account.owner_name} - Balance: {account.__balance} Euro.")
#         return all_acounts

#     def deposit_money(self, money):
#         self.__balance += money
#         print(f"Bank Account:{self.owner_name} - Bank Balance: {self.__balance} Euro")

#     def withdraw_money(self, money):   #(no negative balance allowed)
#         if self.__balance > 0:
#             if self.__balance - money < 0:
#                 print(f"Unable withdraw, Insufficient funds!")
#             else:
#                 self.__balance -= money    
#                 print(f"Bank Account:{self.owner_name} - Bank Balance: {self.__balance} Euro")
#         else:
#             print(f"Unable withdraw, Insufficient funds!")
    
# ba1 = BankAccount("Adam Carter", 1250.75)
# ba2 = BankAccount("Sara Khan", 3400.00)
# ba3 = BankAccount("Lucas Meyer", 890.50)
# ba4 = BankAccount("Nina Vos", 5600.20)
# ba5 = BankAccount("Omar El-Sayed", 150.00)

# print(BankAccount.get_all_accounts())
# print(BankAccount.highest_balance_account())
# print(BankAccount.total_all_acc_money())

# ba1.deposit_money(2000)
# ba2.withdraw_money(5000)
# ba3.withdraw_money(200)

# ///////

# ///////



# class Student:
#     all_student_lst = []
#     def __init__(self, name):
#         self.name = name
#         Student.all_student_lst.append(self)


#     @classmethod
#     def get_all_student(cls):
#         all_student = []
#         for student in cls.all_student_lst:
#             all_student.append(student.name)
#         return all_student


# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name
#         self.course_student_list = []


#     def enroll_students(self, student):
#         self.course_student_list.append(student)
    
#     def get_course_student_lst(self):
#         course_student_lst = []
#         for student in self.course_student_list:
#             course_student_lst.append(student.name)
#         return course_student_lst
    
#     def total_student_number(self):
#         total_numb = 0
#         for student in self.course_student_list:
#             total_numb += 1
#         return total_numb # could have done a = len(self.course_student_list), return a. 



# def main():

#     st1 = Student("Ayaan Malik")
#     st2 = Student("Sofia Vermeer")
#     st3 = Student("Lucas van Dijk")

#     c1 = Course("Python Basics")
#     c2 = Course("Data Structures")

#     print(Student.get_all_student())

#     c1.enroll_students(st1)
#     c2.enroll_students(st3)
#     c1.enroll_students(st2)

#     print(c1.get_course_student_lst())
#     print(c2.get_course_student_lst())
#     print(c1.total_student_number())
#     print(c2.total_student_number())

# if __name__ == "__main__":
#     main()

# /////////////////



# /////////////////



# class Product:
#     product_lst = []
#     def __init__(self, sku, name, category):
        
#         self.sku  = sku
#         self.name = name
#         self.category = category
#         Product.product_lst.append(self)

#     def __str__(self):
#         return f"[SKU]:{self.sku}, {self.name}"
    
#     def __repr__(self):
#         return f"Product(sku={self.sku}, name={self.name}, category={self.category})"



# class Inventory:
#     def __init__(self):
#         self.lst = []

#     def add_product(self, p):
#         self.lst.append(p)

#     def get_first_p_lst(self):
#         print(self.lst[0])
    
#     def get_all_p_lst(self):
#         print(self.lst)

# def main():

#     abc1 = Product("bc-1", "short pants", "Men")
#     abc2 = Product("cc-2", "shirt", "Men")
#     abc3 = Product("dc_v", "blouse", "Woman")

#     print(abc1.__str__())
#     print(abc2.__repr__())

#     inv1 = Inventory()
#     inv1.add_product(abc1)
#     inv1.add_product(abc2)
#     inv1.add_product(abc3)

#     inv1.get_first_p_lst()
#     inv1.get_all_p_lst()

# if __name__ == "__main__":
#     main()

# /////////////////

    



# /////////////////


# /////////////////

class Post:

    def __init__(self, username, content, timestamp):
        self.username = username
        self.content = content
        self.timestamp = timestamp
    

class Feed:
    def __init__(self):
        self.posts_lst = []

    def add_post(self, post):
        self.posts_lst.append(post)

    def __str__(self):
        ok_feed = []
        ok_feed.append(f"--- TIMELINE ---")
        for p in self.posts_lst:
            formatted_feed = f"{p.username}: \"{p.content}\" [{p.timestamp}]"
            ok_feed.append(formatted_feed)
        ok_feed.append("----------------")
        return "\n".join(ok_feed)
        
   

def main():
    
    p1 = Post("@Ayaan", "Learning Python today!", "10:00 AM")
    p2 = Post("@Sofia", "Object oriented code is cool.", "10:05 AM")
    p3 = Post("@Rico", "Done some analyses!", "10:10 AM")

    my_feed = Feed()

    my_feed.add_post(p1)
    my_feed.add_post(p2)
    my_feed.add_post(p3)

    print(my_feed)


if __name__=="__main__":
    main()
