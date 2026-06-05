"""1. Encapsulation – Banking Application"""
class Bank:
    def __init__(self):
        self.__balance=1000

    def deposit(self,a):
        self.__balance+=a

    def withdraw(self,a):
        self.__balance-=a

    def show(self):
        print(self.__balance)

b=Bank()
b.deposit(500)
b.withdraw(200)
b.show()



"""2. Encapsulation – Student Management"""
class Student:
    def __init__(self,r):
        self.__reg=r

    def get_reg(self):
        return self.__reg

s=Student(101)
print(s.get_reg())



"""3. Abstraction – Online Payment"""
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment")

u=UPI()
u.pay()



"""4. Abstraction – Car Example"""
from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class BMW(Car):
    def drive(self):
        print("Driving")

b=BMW()
b.drive()



"""5. Inheritance – Employee, Manager, Developer"""
class Employee:
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id

class Manager(Employee):
    def __init__(self,name,salary,id,team):
        super().__init__(name,salary,id)
        self.team=team

class Developer(Employee):
    def __init__(self,name,salary,id,lang):
        super().__init__(name,salary,id)
        self.lang=lang

m=Manager("Ravi",50000,1,10)
print(m.name,m.team)



"""6. Inheritance – Vehicle"""
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

c=Car("Toyota",120)
print(c.brand,c.speed)



"""7. Polymorphism – Notification System"""
class Email:
    def sendNotification(self):
        print("Email Sent")

class SMS:
    def sendNotification(self):
        print("SMS Sent")

class WhatsApp:
    def sendNotification(self):
        print("WhatsApp Sent")

for i in [Email(),SMS(),WhatsApp()]:
    i.sendNotification()
    
    
    
"""8. Polymorphism – Shape Area"""
class Circle:
    def calculateArea(self):
        print("Circle Area")

class Rectangle:
    def calculateArea(self):
        print("Rectangle Area")

class Triangle:
    def calculateArea(self):
        print("Triangle Area")

for i in [Circle(),Rectangle(),Triangle()]:
    i.calculateArea()
    
    
"""9. Mixed Scenario – Food Delivery App"""
class Customer:
    def __init__(self,name):
        self.__name=name

class PremiumCustomer(Customer):
    pass

class Payment:
    def pay(self):
        print("Payment Done")

class Bike:
    def charge(self):
        print("Bike Charge")

class Car:
    def charge(self):
        print("Car Charge")

Bike().charge()
Car().charge()


"""10. Hospital Management System"""
class Employee:
    def __init__(self,name):
        self.name=name

class Doctor(Employee):
    def salary(self):
        print("Doctor Salary")

class Nurse(Employee):
    def salary(self):
        print("Nurse Salary")

d=Doctor("Ravi")
n=Nurse("Priya")

d.salary()
n.salary()


