# Step 1: Understand Classes and Objects (Absolute Beginner)
# * Goal: Know what a class and an object is.
# * Practice:
#    * Make a `Car` or `Dog` class with attributes like `color`, `name`.
#    * Create 2–3 objects and print their attributes.
# * Key concepts: `class`, `object`, `self`.
# //

# //
# class Lamborgini:
#         def __init__(self,model_name, year, color):
#             self.model_name = model_name
#             self.year = year
#             self.color = color
#             self.engine_running = False
        
#         def engine_on(self):
#             self.engine_running = True
#             return f"{self.model_name}'s engine is now ON"

#         def __str__(self):
#             status = "running" if self.engine_running else "off"
#             return f"{self.model_name}, {self.year}, {self.color} - engine {status}"



    
# def main():
#     car_1 = Lamborgini("Avendtador", 2020, "Yellow")
#     car_2 = Lamborgini("Hurancan", 2025, "MatteBlack")
#     car_3 = Lamborgini("Urus", 2018, "White")

#     print(car_1)
#     car_1.engine_on()
#     print(car_1)
#     print(car_1.engine_on())


# if __name__ == "__main__":
#     main()
# //


# //
# Step 2: Learn Attributes and Methods
# * Goal: Make objects store information and do things.
# * Practice:
#    * Add a method to your `Car` class like `drive()` or `honk()`.
#    * Add a method that uses attributes (`describe()` prints color and brand).
# * Key concepts: `self.attribute`, `self.method()`

# Step 3: Practice Creating Multiple Objects
# * Goal: See how each object is independent.
# * Practice:
#    * Create multiple `Dog` objects with different names.
#    * Make them perform actions (`bark()`, `sit()`).

# Step 4: Learn Inheritance (Beginner+)
# * Goal: Avoid repeating code and make hierarchical structures.
# * Practice:
#    * Make a `Device` parent class and `Laptop` / `Printer` child classes.
#    * Use inherited methods and add child-specific methods.
# * Key concept: `ChildClass(ParentClass)`

# Step 5: Understand Method Overriding (Beginner+)
# * Goal: Let child classes change how inherited methods behave.
# * Practice:
#    * Override `turn_on()` in `Laptop` to also print "Booting OS…"
# * Key concept: Child method can replace parent method

# Step 6: Encapsulation Basics (Beginner+ / Early Intermediate)
# * Goal: Protect attributes from being changed directly.
# * Practice:
#    * Make `self.__secret_code` (private)
#    * Use methods to access or update it safely
# * Key concept: `private vs public attributes`, `getter & setter methods`

# Step 7: Polymorphism (Intermediate)
# * Goal: Use the same method name for different behaviors.
# * Practice:
#    * `Device` class has `action()`
#    * `Laptop` and `Printer` each do something different when `action()` is called

# Step 8: Advanced Concepts (Later)
# * Abstract classes / interfaces
# * Class methods & static methods
# * Multiple inheritance
# * Design patterns

# 💡 Tip:
# * Don't rush. Focus one step at a time and practice.
# * Each step builds on the previous one.