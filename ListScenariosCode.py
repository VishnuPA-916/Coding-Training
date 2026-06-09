1. LIST Scenarios


Scenario 1: Student Marks

marks=[78,90,65,88,95]
print(max(marks))
print(sum(marks)/len(marks))
marks.sort()
print(marks)

Scenario 2: Shopping Cart

cart=["Laptop","Mouse","Keyboard","Mouse"]
print(len(cart))
cart.remove("Keyboard")
print("Laptop" in cart)
print(cart)

Scenario 3: Attendance List

students=["Ram","Sam","John","Arun"]
students.append("Kumar")
students.remove("Sam")
print(students)


2. TUPLE Scenarios


Scenario 1: GPS Coordinates

location=(13.0827,80.2707)
print("Latitude:",location[0])
print("Longitude:",location[1])

Scenario 2: RGB Color

color=(255,0,0)
print("Red:",color[0])
print("Green:",color[1])
print("Blue:",color[2])

Scenario 3: Student Record

student=(101,"Pradeep")
print("ID:",student[0])
print("Name:",student[1])


3. DICTIONARY Scenarios


Scenario 1: Student Information

student={
"name":"Pradeep",
"age":21,
"department":"CSE"
}
print(student["name"])
student["age"]=22
student["cgpa"]=8.5
print(student)

Scenario 2: Product Inventory

inventory={
"Laptop":10,
"Mouse":25,
"Keyboard":15
}
print(inventory["Laptop"])
inventory["Monitor"]=5
del inventory["Keyboard"]
print(inventory)

Scenario 3: Employee Salary

salary={
"Ram":50000,
"Sam":45000,
"John":60000
}
print(max(salary.values()))
salary["Ram"]+=5000
print(salary)


4. SET Scenarios


Scenario 1: Unique Visitors

visitors={"Ram","Sam","John","Ram","Sam"}
print(len(visitors))

Scenario 2: Subjects Chosen

student1={"Python","Java","SQL"}
student2={"Python","C++","SQL"}
print(student1&student2)
print(student1-student2)

Scenario 3: Email Registration

emails={"a@gmail.com","b@gmail.com"}
new="c@gmail.com"
if new in emails:
    print("Duplicate Email")
else:
    emails.add(new)
    print(emails)