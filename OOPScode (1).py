"""Question 1: Single Inheritance (Person → Student)"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no

    def display_student(self):
        print(self.roll_no)

s=Student("Rathna",20,101)
s.display_person()
s.display_student()



"""Question 2: Vehicle → Car"""
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def show_brand(self):
        print(self.brand)

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def show_model(self):
        print(self.model)

c=Car("Toyota","Innova")
c.show_brand()
c.show_model()



"""Question 3: Animal → Dog → Puppy"""
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

p=Puppy()
p.eat()
p.bark()
p.weep()



"""Question 4: Person → Employee → Manager"""
class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)

m=Manager("Ravi",50000,"HR")
m.display()





"""Question 5: Multiple Inheritance (Father + Mother → Child)"""
class Father:
    def bike(self):
        print("Bike")

class Mother:
    def jewellery(self):
        print("Jewellery")

class Child(Father,Mother):
    pass

c=Child()
c.bike()
c.jewellery()


"""Question 6: Teacher + Researcher → Professor"""
class Teacher:
    def teach(self):
        print("Teaching")

class Researcher:
    def research(self):
        print("Researching")

class Professor(Teacher,Researcher):
    pass

p=Professor()
p.teach()
p.research()


"""Question 7: Hierarchical Inheritance (Shape)"""
class Shape:
    pass

class Circle(Shape):
    def draw(self):
        print("Circle")

class Rectangle(Shape):
    def draw(self):
        print("Rectangle")

class Triangle(Shape):
    def draw(self):
        print("Triangle")

Circle().draw()
Rectangle().draw()
Triangle().draw()


"""Question 8: Employee → Developer, Tester"""
class Employee:
    def work(self):
        print("Working")

class Developer(Employee):
    pass

class Tester(Employee):
    pass

d=Developer()
t=Tester()

d.work()
t.work()


"""Question 9: Hybrid Inheritance"""
class A:
    def methodA(self):
        print("A")

class B(A):
    def methodB(self):
        print("B")

class C(A):
    def methodC(self):
        print("C")

class D(B,C):
    def methodD(self):
        print("D")

d=D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()


"""Question 10: Employee → Manager, Developer → TeamLead"""
class Employee:
    def emp(self):
        print("Employee")

class Manager(Employee):
    def manager(self):
        print("Manager")

class Developer(Employee):
    def developer(self):
        print("Developer")

class TeamLead(Manager,Developer):
    def lead(self):
        print("TeamLead")

t=TeamLead()
t.emp()
t.manager()
t.developer()
t.lead()


"""Question 11: Constructor Inheritance (Person → Student)"""
class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll

    def display(self):
        print(self.name)
        print(self.roll)

s=Student("Rathna",101)
s.display()



"""Question 12: Vehicle → Car Constructor"""
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

class Car(Vehicle):
    def __init__(self,brand,model,price):
        super().__init__(brand)
        self.model=model
        self.price=price

    def display(self):
        print(self.brand)
        print(self.model)
        print(self.price)

c=Car("Toyota","Innova",2000000)
c.display()



"""Question 13: Banking System"""
class Account:
    def __init__(self,acc,bal):
        self.acc=acc
        self.bal=bal

class SavingsAccount(Account):
    def __init__(self,acc,bal,rate):
        super().__init__(acc,bal)
        self.rate=rate

    def display(self):
        print(self.acc)
        print(self.bal)
        print(self.rate)

s=SavingsAccount(12345,50000,5)
s.display()



"""Question 14: School Management"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def display(self):
        print(self.name)
        print(self.age)
        print(self.subject)

t=Teacher("Ravi",35,"Python")
t.display()


"""Question 15: Online Shopping"""
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Electronics(Product):
    def __init__(self,name,price,warranty):
        super().__init__(name,price)
        self.warranty=warranty

    def display(self):
        print(self.name)
        print(self.price)
        print(self.warranty)

e=Electronics("Laptop",50000,"2 Years")
e.display()