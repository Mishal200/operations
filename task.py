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