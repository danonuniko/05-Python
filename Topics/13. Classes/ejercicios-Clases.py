"""
1. Create a class called “Rectangle” with two instance attributes called “width” and “height”. 
Create a method called “area” that returns the area of the rectangle.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rectangle = Rectangle(10, 5)
print(rectangle.area())


"""
2. Create a class called “Circle” with an instance attribute called “radius”. 
Create a method called “area” that returns the area of the circle.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * 3.14

circle = Circle(5)
print(circle.area())


"""
3. Creates a class called “BankAccount” that has an attribute called “balance” and two methods called “deposit” and “withdraw”. 
The “deposit” method takes an argument called “amount” and adds it to the balance. 
The “withdraw” method takes an argument called “amount” and subtracts it from the balance if there are sufficient funds. 
If there are not sufficient funds, it prints a message saying so.
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You cannot withdraw an amount higher than your actual balance")
            
    def __str__(self):
        return f"Your actual balance is {self.balance} €"

cuenta_bancaria = BankAccount(10000)
print(cuenta_bancaria)
cuenta_bancaria.deposit(2500)
print(cuenta_bancaria)
cuenta_bancaria.withdraw(7500)
print(cuenta_bancaria)
cuenta_bancaria.withdraw(7500)
print(cuenta_bancaria)