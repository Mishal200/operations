import re

# re.findall()
# re.search()
# re.split()
# re.sub()


text = "I Love Cats"
text1 = "cat is a domestic animal"
# print(f"python\bdjango")
# print(r"python\bdjango")
print(re.search(r'^cat',text))
print(re.search(r'^cat',text1).group())


phone = "8086671008"
result = re.search('^[\d]{10}$',phone)
print(result.group())


print(result.start())
print(result.end())
print(result.span())

print(re.match('cat',text))
print(re.match('cat',text1))


str1 = 'mishal is 23 and adhiee is 21 of ages'  #['mishal is ',' and adhiee is ',' of ages']

print(re.findall(r'\d+',str1))
print(re.search(r'\d+',str1))
print(re.split(r'\d+',str1))
print(re.sub(r'\d+','age',str1))




#/////////////////////////////////////////////////



# num = "9876543210e"

# print(re.search(r"[6-9]{1}\d{9}$", num))