fruits = ["apple", "banana", "orange", "grape", "kiwi", "mango", "strawberry", "blueberry", "watermelon", "pineapple"]
  #        0         1         2         3         4         5         6         7         8          9        10
name= "mishal"
print(fruits)
print(fruits[6])
print(len(name))  # length of the string
print(f"length of the list,number: {len(fruits)}")
n=3
print(type(n))
print(type(name))
print(type(fruits))
f=list(fruits)
letters=list(name)
numbers=list(range(6))
print(numbers)


#         -5        -4       -3        -2       -1
fruits=["apple", "banana", "orange", "grape", "kiwi"]
print(fruits[-3])

#[index:end:step]
print(fruits[2:6])
print(fruits[1:4:2])


print("mango" in fruits)
print("kiwi" in fruits)


for fruit in fruits:
    pass
    print(fruit)
    
    
print(fruits)
# fruits=["apple", "banana", "orange", "grape", "kiwi"]
# fruits[0]=["mulberry",blueberry",watermelon","papaya",strawberry"]
#fruits[0:2]=["mulberry", "blueberry"]
#fruits[2:3]=["mulberry", "blueberry"]




#///////////////////////////////////////////////////////////////////////#

##################### LIST METHODS ##########################

# insert()
# fruits.insert(2,"mango")
# append()
# fruits.append("mango")
# extend()
# fruits.extend(["mango","pineapple"])
# fruits.extend("mango")

# pop()
# fruits.pop(2)
# fruits.pop()


# remove()
# fruits.remove("mango")

# clear()
# fruits.clear()
# del fruits

# count()
# print(fruits.count("mango"))


# index()
# print(fruits.index("mango"))
# fruits.sort(reverse=True)


#fa=fruits.copy()
fa=list(fruits)
fruits.reverse()
print(fruits)
print(fa)