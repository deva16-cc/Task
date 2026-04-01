#Encapsulation
class user:
  def __init__(self):
    self.user_name = None
    self.pwd = None

  def set_user(self, user_name, pwd):
    self.user_name = user_name
    self.pwd = pwd

  def get_user(self):
    return self.user_name

  def register(self):
    print("Registering user:- ", self.user_name)

  def login(self):
    print("Logging in:- ", self.user_name)

#Test
user = user()
user.set_user("Deva", "4578")

user.register()
user.login()

#Inheritence
class user1:
  def  register(self):
    print("User Registered")

  def login(self):
    print("User Logged In")

class Student(user1):
  def student_greet(self):
    print("Hello Student")

class Faculty(user1):
  def student_greet(self):
    print("Hello Faculty")

class TempFaculty(Faculty):
  def student_greet(self):
    print("Hello TempFaculty")

#Objects
faculty = Faculty()
student = Student()
temp = TempFaculty()

#Parent Methods
student.register()
student.login()

#Child Methods
student.student_greet()
faculty.faculty_greet()
temp.tempFaculty_greet()
temp.faculty_greet()  
temp.register()       #We can only access child to parent

#Method Chaining
class user2:
  def register(self):
    print("Registering...")
    return self

  def login(self):
    print("Logined")
    return self

  def greet(self):
    print("Enjoy")
    return self

user = user()

user.login().greet().register()

#Method overriding

class User:

    def greet(self):
        print("Welcome User")


class Student(User):

    def greet(self):
        print("Welcome Student")


class Faculty(User):

    def greet(self):
        print("Welcome Faculty")


# Objects
student = Student()
faculty = Faculty()

student.greet()
faculty.greet()

# Combined Real-Time User System

class User:

    users_count = 0

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print("User logged in:", self.__name)
        return self

    def greet(self):
        print("Welcome User")
        return self

    def register(self):
        print("User registered:", self.__name)
        return self


class Student(User):

    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):

    def greet(self):
        print("Welcome Faculty")
        return self


# Objects
student = Student("Dev", "5578")
faculty = Faculty("Buson", "1458")

# Method Chaining
student.login().greet().register()
faculty.login().greet().register()

print("Total Users:", User.users_count)
