#Bitwise Operator Tasks (1–8)

#1.
a = 10
b = 6
print(a&b)

#2.
x=12 ; y=5
print(x|y)

#3.
num = 8
print(~num)

#4.
a=15 ; b=9
print(a^b)

#5.
num=7
print(num<<2)

#6.
num=20
print(num>>1)

#7.
num1=int(input())
num2=int(input())
print(num1&num2)

#8.
num3=int(input())
num4=int(input())
print(num3^num4)

#String Tasks (9–14)

#9
word="hi"
print(word*4)

#10
word1="Python"
print(word1*3)

#11
a="Super"
b="man"
print(a+b)

#12
x="hello"
y=" "
z="world"
print(x+y+z)

#13
c=input("Enter your name:- ")
print(c*5)

#14
d=input("Enter First word:- ")
e=input("Enter Second word:- ")
print(d+" "+e)

#Input & Type Casting Tasks (15–20)

#15
name1=input("Enter Your Name:- ")
print(name1, type(name1))

#16
age=(input("Enter Your Age:- "))
age=int(age)
print(age, type(age))

#17
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
print(num1 + num2)

#18
num3=int(input("Enter num 1: "))
num4=int(input("Enter num 2: "))
print((num3 + num4)/2)

#19
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(3*a*2+b-2)

#20
num = input("Enter a number: ")
print("Before data type casting:", type(num))
num = int(num)
print("After data type casting:", type(num))

#Unit Digit Tasks (21–25)
#21
num=input("Enter Number: ")
print(num[len(num)-1])

#22
num1=int(input("Enter the value: "))
print(num1%10)

#23
num=123456
num //=10
print(num)

#24
num1=627856
num1 //=10
print(num1%10)

#25
n=78910
print("the last digit is:", n%10)

#If Statement Tasks (26–30)
# 26
if(10>=5):
    print("The condition is correct")

#27
num=int(input("Enter a number"))
if(num>50):
    print("Num is greater than 50")

#28
age=int(input())
if(age>=18):
    print("Age is greater than 18")

#29
num1=101
if(num1>100):
    print("Number is greater than 100")

#30
n=3
if(n>0):
    print("Number is greater than 0")

#If-Else Tasks (31–34)

#31
n=5
if(n%2==0):
    print("num is even")
else:
    print("num is odd")

#32
num=int(input("enter your marks"))
if(num>=35):
    print("You have passed the exam")
else:
    print("You have failed the exam")

#33
n=int(input("enter the number"))
if(n>0):
    print("Number is positive")
elif(n<0):
    print("The number is Negative")
else:
    print("The number is Zero")

#34
num=5
if(num<10):
    print("num is less than 10")
else:
    print("num is greater than 10")

#Nested If Tasks (35–37)

#35
name= input("Enter your name for job eligibility: ")
age=int(input("Enter your Age: "))
height=int(input("Enter your Height: "))
weight=int(input("Enter your Weight: "))

if (age>=18):
    if(height>=160):
        if(weight>=60):
            print(name, "Congrats you are Selected")
        else:
            print(name, "Sorry you are Rejected")    
    else: 
        print(name, "Sorry you are Rejected")
else:
    print(name, "Sorry you are Rejected")

#36.

name= input("Enter your name for admission: ")
age=int(input("Enter your age: "))
mark=int(input("Enter your marks: "))

if(age>=17 and mark>=60):
    print(name, "Congrats, admission successful")
else:
    print(name, "Sorry, admission not successful")

#37.

name= input("enter your name for sports selection: ")
age=int(input("enter your age: "))
height=int(input("enter your height: "))
weight=int(input("enter your weight: "))

if (age>=16):
    if(height>=50):
        if(weight>=60):
            print(name, "congrats you are selected")
        else:
            print(name, "your weight is not eligible")    
    else: 
        print(name, "Sorry your height is not eligible")
else:
    print(name, "Sorry your age is not eligible")

#38.

day=int(input("enter today's number: "))

match day:
    case 1:
        (print("sunday"))
    case 2:
        (print("monday"))
    case 3:
        (print("tuesday"))
    case 4:
        (print("wednesday"))
    case 5:
        (print("thursday"))
    case 6:
        (print("friday"))
    case 7:
        (print("saturday"))

#39.

color=int(input("enter color numbe: "))

match color:
    case 1:
        (print("The color is Red"))
    case 2:
        (print("The color is blue"))
    case 3:
        (print("The color is green"))

#40.

fruit=int(input("enter fruit number: "))

match fruit:
    case 1:
        (print("The fruit is apple"))
    case 2:
        (print("The fruit is mango"))
    case 3:
        (print("The fruit is orange"))
    case 4:
        (print("The fruit is banana"))
    