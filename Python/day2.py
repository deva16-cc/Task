# Bitwise operator 

'''
AND  - &
OR   - |
NOT  - ~
XOR  - ^
leftShift - <<
RightShift - >>
'''

'''
XOR - ^


T   T    - F
T   F    - T
F   T    - T
F   F    - F
'''


a = 5

b = 7


print(a & b)
print(a | b)
print(~b)
print(a ^ b)


print(12 << 1) 
print(12 >> 1)



# String - "Adsf"

# string Replication 


a = "hello"

print(a * 5)

# string concatination  +

str1 = "iron"
str2 = "man"
str3 = " "

print(str1 +str3 + str2)


# user Input Console    (input())

# name = input("enter your name : - ")

# print("userName :- ",type(name))


# age = input("enter your age :- ")
# print("userAge :- ",type(age))


# TypeCasting 


# num2 = int(input("enter your mark Maths :- "))
# num3 = int(input("enter your mark Science :- "))

# print((num2+num2)/2)


# a = int(input("enter first value :- ")) #3
# b = int(input("second first value :- ")) #2

# print(3*a*2+b - 2) #error #18


#unit digit


# num = input() #10000 , 0 - 1, 1 - 0 , 2 - 0 , 3 - 0 ,4 - 0
# print(num[len(num)-1]) # num[len(num)-2]

# print(1234//10) --> 123


# num1 = int(input())

# num1 //= 10 #num1 = num1 // 10 = 1234 // 10 -- > 123

# print(num1 % 10) #123 % 10 --> 3


# flow control Statement

# 1. conditional statement

# 1. if statement

# if condition = true --> next line , false --> if inside not allow

# example 

if (5>=5) :
    print("now i think condition true")


# 2.if else statement

# if (5>5) :
#     print("condition true")
# else :
#     print("condition false")


# # 3. Elif Statement

# time = int(input("enter the time Now :- 24hrs"))

# if (time >= 1 and time <= 6) : 
#     print("good morning")
# elif (time >= 7 and time <=12) :
#     print("morning")
# elif (time >= 13 and time <= 17) : 
#     print("Good Afternoon")
# elif (time >= 18 and time <= 20) :
#     print("Good Evening")
# else :
#     print("Good night")


# #4. Nested If Statement 


# # uniform entrance selection application
# name = input("enter your name")
# age = int(input("enter your age"))
# height = int(input("enter you height using cm"))
# weight = int(input("enter your weight using kg"))

# if (age >= 18) :
#     if (height >= 160) : 
#         if (weight >= 60) :
#             print(name ," congradulation your selected 😊😊😊")
#         else : 
#             print(name, " your weight is not eligible")

#     else : 
#         print(name, "  your height is not eligible")
# else : 
#     print(name, " your age is not eligible")


# 5. match statement


# match variable :
#     case value : statement


# example 


day = int(input("enter the today number :- "))


match day :
    case 1 :
        print("sunday")
    case 2 :
        print("monday")
    case 3 :
        print("tuesday")
    case 4 :
        print("wednesday")
    case 5 :
        print("thursay")
    case 6 :
        print("friday")
    case 7 :
        print("saturday")
    







# 2. looping statement







