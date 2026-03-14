print("hello world", end=" ")
print("welcome python")
print("laptop","mouse","keyboard",sep="\'")


# escape sequence

# \n (new line)
# \t (tab character it create space)


# jgjgvghfghfhg - single line comment

'''
print("hello")
print("welcome")
print("hi")

multiline command
'''

# data Types

'''
simple dataType

1. integer  - 100

2. string   - "whatever"

3. float    - 50.2

4. boolean  - True , False

'''

'''
complex DataType

1. list

2. Dictionary

3. Tuple

4. set

'''

# variables 

name = "navi"
age = 15

print(name,age , sep=",")

# assignment 

# single assignment

n = 5

print("sigle assignment :- ", n)

# multi assignment

name1,age1,launguage = "navi",15,True

print("multi assignment :- ", name1, age1,launguage)



# Indexing

name2 = "john"

print(name2[0])

# immutability

# name2[0] = "R"

# print(name2)



# operators


'''
1 . arithmetic operator
2 . assignment operator
3 . comparision operator
4 . logical operator
5 . bitwise operator
6 . membership operator
'''

# 1. arithmetic operator 

# addition      +

print(1 + 3)

# subraction    -

print(2 - 1)

# multiplication *

print(3*3)

# division   /

print(5 / 5)

# modulus    % (it return remainder if right side value is large it return answer as left value)

print(20%10)

# Exponencial **

print(4**2) # 4^2 = 4*4 = 16


# floar division // (it return quotient value)

print(18 // 2)

'''
Bodmas 

b - bracket
o - order
d - division
m - multiplication
a - addition
s - subraction
'''



print(2**3**(2%10)) #        2**3**2 = 2^9

print(2**9)



# Assignment operator

num1 = 10
additionVal = 100

num1 /=  additionVal

print(num1)


# comparision & Relational operator

'''
lessThen     <       (5<5)     False

greaterThen  >       (5>5)     False

lessThenEq   <=      (5<=5)    True

GreaterThenEq >=     (10>=2)   True

LoosyTypeEq   ==     (10=="10") False

LoosyNotEq    !=     (10 != "10") True



'''
print(10>10)
print(10>.5)
print(10=="10")

print("10")
print(10)


a = "siva"
b = "Siva"

print("s :-", ord("s"))
print("S :-", ord("S"))

print(a==b)



a = 5
b = 7

print(a,b)

# temp = a

# a = b 

# b = temp

# print(a,b)

a,b = b,a

print(a,b)



# membership operator [in] , [not in]

group = [1,2,3,4,5]

print(50 not in group)


# logical operator

'''
AND   -- > and
OR    -- > or
NOT   -- > not

'''


# AND 

# True and True and True = True 
# True and False and True = False


# OR

# True or False or False = True
# False or False or False = False

# NOT

# not(True) = False
# not(False) = True 


print(5>5 and 5==5 and 1>=.1000) # False
print(5==5 or 5>=3 and 2==2) # True
print(not(6>=2) and 8>3) #False


# Bitwise operator 

'''
AND  - &
OR   - |
NOT  - !
XOR  - ^
'''

a = 4

b = 5 

print(a ^ b)

#-----------------------------------------------------------------

#Task 1 - Print Foramtting

print("Hello World", end=" ")
print("Welcome Python")
print("Laptop", "Mouse", "Keyboard", sep="|")

#Task 2 - Variables

name = "ravi"
age =22
city ="Chennai"

print(name, age, city, sep="-")

#Task 3 - Multiple Assignment

name = "Meena"
age = 20
student = True

print(name, age, student)

#Task 4 - Indexing

word = "Python"
print(word[0], word[2], word[5])

#Task 5 – Arithmetic Operators

print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 3)
print(2 ** 4)
print(20 // 3)

#Task 6 – BODMAS Expression

print(3 + 2 * 5 ** 2)
# BODMAS is Rule to execute brackets, division, multiplication, addition, subtraction

#Task 7 – Assignment Operator

num = 50
num += 25
print(num)
num = 100
num /= 10
print(num)

#Task 8 – Comparison Operators

print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

#Task 9 – String Comparison

a = "apple"
b = "Apple"
print(a == b) 
# The result is false because python is case-sensitive and also the ASCII Value of a=97 and A=65 are not same
print("a :-", ord("a"))
print("A :-", ord("A"))

#Task 10 – Logical Operators

print(10 > 5 and 5 == 5) 
print(5 > 10 or 10 == 10) 
print(not(5 > 2)) 

#Task 11 – Membership Operator

numbers = [10,20,30,40,50]
print(20 in numbers, 60 in numbers, 30 not in numbers)

#Task 12 – Swap Variables

a = 10
b = 20
a, b = b, a
print(a, b)

#Task 13 – Bitwise XOR

a = 6 #binary value = 110
b = 3 #binary value = 011
print(a ^ b)