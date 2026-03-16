# number=0
# if number > 0:
  #   print("the number is positive")
# elif number < 0:
  #   print("the number is negative")
# else :
  #   print("the number is zero")
    

        
# if number % 2 == 0:
  #   print("the number is even")
# else:
  #   print(" the number is odd")
    
# if number>100:
 #    print("the number is greater than 100")
    

###########################


# text = input("Enter a string: ")

# for char in text:
   #  print(char)
    
######################################   
    
# text = input("Enter a string: ")

# count = 0
# for char in text:
   #  count = count + 1

# print(count)

######################################       
    
# text = input("Enter a string: ")

# count = 0
# for char in text:
    # if char.lower() in "aeiou":
    #     count = count + 1

# print(count)

#####################################

# text = input("Enter a string: ")

# for char in text:
  #   print(char.upper())
    
###########################################
    
# text = input("Enter a string: ")

# reverse = ""
# for char in text:
 #    reverse = char + reverse

# print(reverse)


#/////////////////////////////////////////////////////////////////////////////////

#1
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#2
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3
a, b, c = 10, 25, 15

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest:", largest)

#4
s = "programming"
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

#5
s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#6
a = 5
b = 10

a = a + b
b = a - b
a = a - b

print(a, b)

#7
arr = [1,2,3,4,5]
total = 0

for i in arr:
    total += i

print("Sum:", total)

#8
num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#9
for i in range(1,101):
    print(i)

#10
s = "python"
count = 0

for i in s:
    count += 1

print("Length:", count)

#11
arr = [10,20,4,45,99]

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)

#12
arr = [1,2,2,3,4,4]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)

#13
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial:", fact)

#14
n = 7
prime = True

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

print("Prime" if prime else "Not Prime")

#15
s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1

max_char = max(freq, key=freq.get)
print(max_char)

#16
s = "hello world"
words = s.split()

result = []
for w in words:
    result.append(w[::-1])

print(" ".join(result))

#17
a = [1,2,3,4]
b = [3,4,5,6]

intersection = []

for i in a:
    if i in b:
        intersection.append(i)

print(intersection)

#18
arr = [1,2,2,3,3,3]

freq = {}
for i in arr:
    freq[i] = freq.get(i,0) + 1

print(freq)

#19
arr = [5,3,8,1]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

#20
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
    
#21
n = 10
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#22 
arr = [1, 2, 4, 5]
n = 5
missing = n*(n+1)//2 - sum(arr)
print(missing)

#23
num = 1234
s = 0
for i in str(num):
    s += int(i)
print(s)

#24
num = 12345
print(len(num))

#25
n = 5
for i in range(1, n+1):
    print("*"*i)

#26
year = 2024
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

#27
arr = [1,0,2,0,3]
for i in arr:
    if i != 0:
        print(i, end=" ")
for i in arr:
    if i == 0:
        print(i, end=" ")

#28
arr = [5,2,8,1]
print(min(arr))

#29
num = 153
s = 0
for i in str(num):
    s += int(i)**3
if s == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#30
arr = [1,2,3,4,5]
k = 2
print(arr[k:] + arr[:k])

#31
arr = [1,2,3,2,4,1]
for i in arr:
    if arr.count(i) > 1:
        print(i)

#32
a = [1,3,5]
b = [2,4,6]
print(sorted(a + b))

#33
s = "python is very powerful"
words = s.split()
print(max(words, key=len))

#34
s = "hello world"
print(s.replace(" ",""))

#35
s = "hello"
vowels = "aeiou"
for i in s:
    if i in vowels:
        print("*", end="")
    else:
        print(i, end="")

#36
s = "HelloWorld"
u = 0
l = 0
for i in s:
    if i.isupper():
        u += 1
    if i.islower():
        l += 1
print("Upper:",u)
print("Lower:",l)

#37
a = "apple"
b = "grape"
for i in a:
    if i in b:
        print(i)

#38
arr = [1,2,3,4]
print(arr[::-1])

#39
arr = [1,2,3,4]
if arr == sorted(arr):
    print("Sorted")
else:
    print("Not Sorted")
