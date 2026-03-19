def is_even(num):
    return num%2 == 0
print(is_even (10))
print(is_even(13))
# print(is_even())
def user_details(age, name="Guest"): # Default parameter
    print(f"Hello, {name}! Age: {age}")
x="Akhil"
user_details(8, x) # Positional arguments
user_details(10)

user_details(name="Anandhu", age=9) # Keyword arguments 
def numbers(*args): # Arbitrary arguments
    print(args)

numbers (1)

def details(**kwargs): # Arbitrary keyword arguments
    print (kwargs)

# print(kwargs)
details (name="Anandhu", age=9)

result = lambda x,y:x+y
print (result (5,3))
# map ()
# filter()
# reduce()