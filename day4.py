#Mini Project 1: Employee Management System

employees = []

def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    salary = float(input("Salary: "))
    employees.append({"name": name, "age": age, "role": role, "salary": salary})

def display():
    for emply in employees:
        print(emply)

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = float(input("New salary: "))

def delete_employee():
    name = input("Enter name to delete: ")
    for emply in employees:
        if emply["name"] == name:
            employees.remove(emply)

add_employee()
add_employee()
add_employee()
display()

#Mini Project 2: Student Report Card

def report():
    name = input("Enter student name: ")
    m1 = int(input("Mark1: "))
    m2 = int(input("Mark2: "))
    m3 = int(input("Mark3: "))
    
    total = m1 + m2 + m3
    avg = total / 3
    
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    else:
        grade = "C"
    
    print(f"\n{name} ReportCard")
    print(f"Total:{total}/300, Average: {avg:.1f}, Grade: {grade}")

report()

#Mini Project 3: Shopping Cart System

cart = []

def add_item():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart.append({"name": name, "price": price, "qty": qty})

def show_cart():
    total = 0
    for item in cart:
        cost = item["price"] * item["qty"]
        total += cost
        print(item["name"], cost)
    print("Total:", total)

def remove_item():
    name = input("Remove product: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)

while True:
    print("\n1.Add 2.Show 3.Remove 4.Exit")
    ch = input("Choice: ")
    
    if ch == "1":
        add_item()
    elif ch == "2":
        show_cart()
    elif ch == "3":
        remove_item()
    else:
        break


#Mini Project 4: Login & User Validation

users = {"admin": "1234", "user": "pass", "guest": "Name", "john": "doe"}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

#Mini Project 5: Unique Visitor Counter
visitors = set()

for i in range(5):
    name = input("Visitor name: ")
    visitors.add(name)

print("Unique Visitors:", len(visitors))
print(visitors)

#Mini Project 6: String Formatter Tool

name = input("Enter name: ")
product = input("Enter product: ")

print(f"{name} bought {product}")

text = name + product
print("------{text:<20}------".format(text=text))
print("------{text:>20}------".format(text=text))
print("------{text:^20}------".format(text=text))

#Mini Project 7: Bank Account System

account = {"name": "Deva", "balance": 1000}

def deposit():
    amt = float(input("Enter Deposit amount: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Enter Withdraw amount: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient balance")

def check():
    print("Balance:", account["balance"])

deposit()
withdraw()
check()


#Mini Project 8: Voting System

votes = {"A": 0, "B": 0, "C": 0}

for i in range(5):
    v = input("Vote (A/B/C): ")
    if v in votes:
        votes[v] += 1
    else:
        print("Invalid vote")

winner = max(votes, key=votes.get)
print("Winner:", winner)

#Mini Project 9: Course Enrollment System
students = {}

def add_student():
    name = input("Student: ")
    courses = input("Courses (comma): ").split(",")
    students[name] = courses

def display():
    print(students)

add_student()
display()

#Mini Project 10: Number Utility Tool
num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

print("With commas:", f"{num:,}")
print("Scientific:", f"{num:e}")

