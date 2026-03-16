#1
numbers = [12, 45, 7, 23, 89, 34, 56, 1, 90, 18]
largest = max(numbers)
smallest = min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

#2
numbers = [10, 15, 22, 33, 40, 55, 60]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Number of even numbers:", count)

#8
numbers = [10, 20, 30, 20, 40, 20, 50]
element = 20
count = 0
for num in numbers:
    if num == element:
        count += 1
print("Element appears", count, "times")

#10
numbers = [5, 10, 15, 20]
total = 0
for num in numbers:
    total += num
print("Sum of elements:", total)

#11
numbers = (10, 20, 30, 40, 50)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length of tuple:", len(numbers))

#12
numbers = (10, 20, 30)
num_list = list(numbers)
num_list.append(40)
numbers = tuple(num_list)
print("Updated tuple:", numbers)

#13
numbers = (10, 20, 30, 20, 40, 20)
element = 20
count = numbers.count(element)
print("Element appears", count, "times")

#14
numbers = (15, 42, 8, 33, 67)
maximum = max(numbers)
minimum = min(numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)

#19
numbers = [1, 2, 3, 4, 5]
first = numbers.pop(0)
numbers.append(first)
print(numbers)