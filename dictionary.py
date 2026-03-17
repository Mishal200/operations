students={
    "name":"vishnu",
    "age":23,
    "roll_no":3,
    "marks":[69,79,68,56],
    "name":"mishal",
    'is_adult':False
}

students['roll_no']=2
print(type(students))
print(students)
print(students['name'])
students.update(age=24)
print(students.get('roll_no'))


# student.pop('is_adult')
# sudent.popitem()
# student.clear()

list1=[]
for key in students.keys():
    list1.append(key)
print(list1)
print(students.values())
for value in students.values():
    print(value)
    
print(students.items())
items = students.items()
for key,value in students.items():
    print(key,' : ', value)
      
students['name']='manu'
print(students)
print(items)
for s in students:
    print(s)
    print(students[s])
print('is_adul' in students)


students['phone'] = 8956746331
students.update({'email':'manu@gamil.com'})
students.update(email='manu@gamil.com')
    
    
print(students)

dict1={}
keys = ('name','age','email')
y=0
dict1.fromkeys(keys,y)
print(dict1.fromkeys(keys,y))

students =[
    {'name':'manu','age':15},
    {'name':'mishal','age':23}
]

for student in students:
    for key in student:
        print(key,' : ',student[key])