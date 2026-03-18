# Section 1: Loop Basics (1–10)

#1
for i in range(1,51):
    print(i)
    

#2
for i in range(1,101):
    if i%2==0:
        print("Even Numbers:", i)
        
#3
for j in range(1,101):
    if j%2!=0:
        print("Odd Numbers:", j)
        
#4
n = 7
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")   
    
#5
total=0
for i in range(1,101):
    total+=i
print("Sum of first 100 natural numbers:", total)

#6
for i in range(50,0,-1):
    print(i)
    
#7
list1 = []
for i in range(1,100):
    if i%3 == 0:
        list1.append(i)
print(list1)
print("The Numbers divisible by 3 from 1-100 are : ",len(list1))

#8
for i in range(1,11):
    print(i**2)
    
#9
for i in range(1,11):
    print(i**3)
    
#10
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(i)
    
#Section 2: While Loop (11–15)

# 11 
i = 1
while i <= 20:
    print(i)
    i += 1

# 12
num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(fact)

# 13
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

# 14. Count digits
num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# 15. Until "stop"
while True:
    text = input("Enter something: ")
    if text.lower() == "stop":
        break
    
#Section 3: Nested Loop (16–20)

# 16. *
for i in range(1, 5):
    print("*" * i)

# 17. 1, 12, 123...
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Tables 1–5
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# 19. A B C pattern
for i in range(3):
    for j in ['A', 'B', 'C']:
        print(j, end=" ")
    print()

# 20. 1–9 grid
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
    
#Section 4: String Basics (21–25)

# 21. Count characters
s = input("Enter string: ")
count = 0
for ch in s:
    count += 1
print(count)

# 22. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

# 23. Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print(count)

# 24. Reverse string
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 25. Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
#Section 5: String Slicing (26–30)

s = input("Enter string: ")

# 26. First 5 characters
print(s[:5])

# 27. Last 3 characters
print(s[-3:])

# 28. Reverse
print(s[::-1])

# 29. Every 2nd character
print(s[::2])

# 30. Remove first & last
print(s[1:-1])

#Section 6: List Basics (31–35)

# 31. Sum of list
lst = [1, 2, 3, 4, 5]
print(sum(lst))

# 32. Max
print(max(lst))

# 33. Min
print(min(lst))

# 34. Count elements
count = 0
for i in lst:
    count += 1
print(count)

# 35. Check element
x = int(input("Enter number: "))
if x in lst:
    print("Exists")
else:
    print("Not Exists")
    
#Section 7: List Operations (36–40)

lst = []

# 36. Append 3 elements
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)

# 37. Insert
lst.insert(1, 15)
print(lst)

# 38. Remove
lst.remove(20)
print(lst)

# 39. Reverse without reverse()
rev = []
for i in lst:
    rev = [i] + rev
print(rev)

# 40. Sort without sort()
lst = [5, 2, 8, 1]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)
