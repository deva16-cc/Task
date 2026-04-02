# Task 1 Super() function
#Parent class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
#Child class
class Student(Person):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
        
    def get_details(self):
        return f"StudentName: {self.name}, ID: {self.id}, Department: {self.dept}, Fees: {self.fees}"
    
class Faculty(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        
    def get_details(self):
        return f"FacultyName: {self.name}, ID: {self.id}, Salary: {self.salary}"
    
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, contract_period):
        super().__init__(name, id, salary)
        self.contract_period = contract_period
        
    def get_details(self):
        return f"TempFacultyName: {self.name}, ID: {self.id}, Salary: {self.salary}, Contract Period: {self.contract_period}"
    
s = Student("Divesh", 101, "Computer Science", 75000)
f = Faculty("Dr.C Jospeh", 201, 120000)
t = TempFaculty("Dr.Suresh", 301, 90000, "6 months")

s.get_details()
f.get_details()
t.get_details()

print(s.get_details())
print(f.get_details())
print(t.get_details())

# Task 2 Apply abstraction

from abc import ABC, abstractmethod

#abstract class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
    
#parent class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def get_details(self):
        return f"UserName: {self.name}, ID: {self.id}"
    
#child class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
        
    def get_details(self):
        return f"{super().get_details()}, Department: {self.dept}, Fees: {self.fees}"
    
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        
    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"
    
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, contract_period):
        super().__init__(name, id, salary)
        self.contract_period = contract_period
        
    def get_details(self):
        return f"{super().get_details()}, Contract Period: {self.contract_period}"
    
s = Student("Gokul", 101, "Computer Science", 95000)
f = Faculty("Dr.Ajithey", 201, 160000)
t = TempFaculty("Dr.Suriya", 301, 110000, "1 year")

print(s.get_details())
print(f.get_details())
print(t.get_details())

# Task 3 Sorting using key
#student
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
        
    def __str__(self):
        return f"StudentName: {self.name}- Fees: {self.fees}"
    
#faculty
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def __str__(self):
        return f"FacultyName: {self.name}- Salary: {self.salary}"
    
#list of students
students = [
    Student("Divesh", 101, "Computer Science", 75000),
    Student("Gokul", 102, "Information Technology", 85000),
    Student("Suresh", 103, "Electronics", 65000)
]
#sorting students by fees
students.sort(key=lambda x: x.fees)

print("Sorted Students (by Fees):")
for s in students:
    print(s)

#list of faculty
faculties = [
    Faculty("Dr.C Jospeh", 201, 120000),
    Faculty("Dr.Ajithey", 202, 160000),
    Faculty("Dr.Vijay", 203, 110000)
]
#sorting faculty by salary
faculties.sort(key=lambda x: x.salary)

print("Sorted Faculty (by Salary):")
for f in faculties:
    print(f)

#Task 4 Use map()
#students
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
        
#list of students
students = [
    Student("Ramesh", 101, "Computer Science", 85000),
    Student("Babu", 102, "Information Technology", 105000),
    Student("Anand", 103, "Electronics", 65000)
]

names = list(map(lambda x: x.name, students))
print("Student Names:", names)

#Task 5 Use filter()
#students
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
        
    def __str__(self):
        return f"StudentName: {self.name}- Fees: {self.fees}"
    
#faculty
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def __str__(self):
        return f"FacultyName: {self.name}- Salary: {self.salary}"
    
#Data
students = [
    Student("Ramesh", 101, "Computer Science", 85000),
    Student("Babu", 102, "Information Technology", 105000),
    Student("Anand", 103, "Electronics", 65000)
]

faculties = [
    Faculty("Dr.C Chandrasekar", 201, 90000),
    Faculty("Dr.Damodharan", 202, 160000),
    Faculty("Dr.Ramachardran", 203, 110000)
]

#filter students fees > 80000
high_fee = list(filter(lambda x: x.fees > 80000, students))

print("Students with Fees > 80000:")
for s in high_fee:
    print(s)
    
#filter faculty salary > 150000
high_salary = list(filter(lambda x: x.salary > 150000, faculties))

print("Faculty with Salary > 150000:")
for f in high_salary:
    print(f)
    
#Task 6 Use reduce()

from functools import reduce
#students
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

#faculty
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
#Data
students = [
    Student("Mani", 101, "Computer Science", 125000),
    Student("Arun", 102, "Information Technology", 205000),
    Student("kuamaran", 103, "Electronics", 185000)
]

faculties = [
    Faculty("Dr.C Chandrasekar", 201, 90000),
    Faculty("Dr.Damodharan", 202, 160000),
    Faculty("Dr.Ramachardran", 203, 110000)
]

#total fees of students
total_fees = reduce(lambda acc, x: acc + x.fees, students, 0)

#total salary of faculty
total_salary = reduce(lambda acc, x: acc + x.salary, faculties, 0)

print("Total Fees of Students:", total_fees)
print("Total Salary of Faculty:", total_salary)

#Task 7 Higher Order Functions

#students
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
        
    def __str__(self):
        return f"StudentName: {self.name}- Fees: {self.fees}"
    
def process_students(students, func):
    return list(map(func, students))

#Data
students = [
    Student("Mani", 101, "Computer Science", 125000),
    Student("Arun", 102, "Information Technology", 205000),
    Student("kuamaran", 103, "Electronics", 185000)
]

#Extract student names using higher order function
names = process_students(students, lambda s: s.name)
print("Student Names:", names)

#Increase student fees
updated_fees = process_students(students, lambda s: f"StudentName: {s.name}- Updated Fees: {s.fees + 10000}")
print("Updated Student Fees:", updated_fees)

#Format student details
details = process_students(students, lambda s: f"StudentName: {s.name}, Department: {s.dept}")
print("Student Details:", details)

#Task mini system

from abc import ABC, abstractmethod
from functools import reduce

#  Abstract Class
class  AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


#  Parent Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"


#  Student Class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"


#  Faculty Class
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"


#  Higher Order Function
def process_users(data, func):
    return list(map(func, data))


#  Data
students = [
    Student("Mahat", 101, "CSE", 50000),
    Student("Prem", 102, "IT", 60000),
    Student("Ganesh", 103, "ECE", 70000),
    Student("Sumanth", 104, "CSE", 80000),
    Student("Vinayak", 105, "IT", 90000)
]

faculty_list = [
    Faculty("Ravi", 201, 25000),
    Faculty("Suresh", 202, 35000),
    Faculty("Anand", 203, 45000)
]


#  1. Print All Details

print("---- All Student Details ----")
for s in students:
    print(s.get_details())

print("\n---- All Faculty Details ----")
for f in faculty_list:
    print(f.get_details())


# 2. Sorted Data
students_sorted = sorted(students, key=lambda s: s.fees)
faculty_sorted = sorted(faculty_list, key=lambda f: f.salary)

print("\n---- Students Sorted by Fees ----")
for s in students_sorted:
    print(s.get_details())

print("\n---- Faculty Sorted by Salary ----")
for f in faculty_sorted:
    print(f.get_details())


#  3. Filtered Data
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))

print("\n---- High Fee Students ----")
for s in high_fee_students:
    print(s.get_details())

print("\n---- High Salary Faculty ----")
for f in high_salary_faculty:
    print(f.get_details())


#  4. Total Aggregation (reduce)
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Salary Paid:", total_salary)


#  5. Using Higher Order Function (map)
student_names = process_users(students, lambda s: s.name)
faculty_names = process_users(faculty_list, lambda f: f.name)

print("\nStudent Names:", student_names)
print("Faculty Names:", faculty_names)

