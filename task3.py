numbers = [10, 5, 20, 8, 15, 30, 3, 12, 25, 7]

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)


#/////////////////////////////////////////////////////////

numbers = [1,2,3,4,5,6,7,8,9,10]

count = 0

for n in numbers:
    if n % 2 == 0:
        count += 1

print("Even numbers:", count)

#//////////////////////////////////////////////

numbers = [1,2,3,4,5]

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)

#////////////////////////////////////////////


numbers = [1,2,2,3,4,4,5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)


#//////////////////////////////////////////////////


numbers = [1,2,3,4,5,6,7,8]

odd_list = []

for n in numbers:
    if n % 2 != 0:
        odd_list.append(n)

print(odd_list)


#////////////////////////////////////////////////////////


numbers = [10, 20, 5, 40, 30]

largest = max(numbers)
numbers.remove(largest)

second_largest = max(numbers)

print("Second Largest:", second_largest)

#///////////////////////////////////////////////////////////


numbers = [10,20,30,40,50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

#////////////////////////////////////////////////////////////


numbers = [1,2,3,2,4,2,5]

element = 2
count = 0

for n in numbers:
    if n == element:
        count += 1

print("Count:", count)

#////////////////////////////////////////////////////////


list1 = [1,2,3,4]
list2 = [3,4,5,6]

merged = list1 + list2
result = []

for n in merged:
    if n not in result:
        result.append(n)

print(result)


#////////////////////////////////////////////////////////

numbers = [1,2,3,4,5]

total = 0

for n in numbers:
    total += n

print("Sum:", total)


#////////////////////////////////////////////////////////


t = (10,20,30,40,50)

print("First:", t[0])
print("Last:", t[-1])
print("Length:", len(t))


#////////////////////////////////////////////////////////

t = (1,2,3)

l = list(t)
l.append(4)

t = tuple(l)

print(t)


#////////////////////////////////////////////////////////


t = (1,2,3,2,4,2)

count = 0

for n in t:
    if n == 2:
        count += 1

print("Count:", count)


#////////////////////////////////////////////////////////


t = (10,5,20,3,15)

print("Max:", max(t))
print("Min:", min(t))


#////////////////////////////////////////////////////////

numbers = [1,2,2,3,4,4,5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

result = tuple(unique)

print(result)


#////////////////////////////////////////////////////////


data = [(1,5), (3,7), (8,2)]

for t in data:
    print(t[0] + t[1])
    
    
#////////////////////////////////////////////////////////



data = [(1,2), (4,5), (3,7)]

max_sum = 0
result = ()

for t in data:
    s = t[0] + t[1]
    if s > max_sum:
        max_sum = s
        result = t

print(result)


#////////////////////////////////////////////////////////

t = (1,2,3,4,5,6,7)

even = []
odd = []

for n in t:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)


#/////////////////////////////////////////////////////


