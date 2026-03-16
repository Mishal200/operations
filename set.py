my_set1={'apple',2,3,'grapes',1,'grapes',1,1,1,1}
print(my_set1)
print(len(my_set1))
my_set2=set()
print(type(my_set2))
my_set1.add(63)
my_set1.update(['mango','orange','banana','grapes','apple'])
print(my_set1)

my_set3=set([454,6,79,98,98,76,79])
print(my_set3)

# my_set1.clear()
# my_set1.pop()
# my_set1.pop()

my_set1.remove('apple')
my_set1.discard('grapess')

#del my_set1
print(my_set1)


# //////////////////////////////////////////////////////////////////////


set1={'apple','orange','banana'}
set2={'google','samsung','apple'}

print(set1.union(set2))
print(set1 | set2)

set1.update(set2)
print(set1,'update')

print(set1.intersection(set2))
print(set1 | set2)

set1.intersection_update(set2)
print(set1,'intersection_update')

print(set1.difference(set2))
print(set2.difference(set1))
print(set1-set2)

set1.difference_update(set2)
print(set1,'difference_update')
print(set1.symmetric_difference(set2))
print(set1^set2)
set1.symmetric_difference_update(set2)
print(set1)


#//////////////////////////////////////////////////////////////
                   #subset&superset
                   
                   
a={1,2,3,4,5}
b={3,4,5}
c={6,7,8}

print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))

print(a.isdisjoint(b))
print(a.isdisjoint(c))