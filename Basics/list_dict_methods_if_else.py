l=['Mani','bhuvi','vicky','nithya','ragha']


# lenght of list
# print(len(l))

# print(dir(l))

l.append('vishnu')
l.append('vishnu')
l.insert(2,"sandeep")

# count - returns the no of occurance of specifeid element
print(l.count('vishnu'))

# deafault last element removes
# if we do not specify index it removes last elemenet
print(l)
name=l.pop(1)
print(name)
print(l)

# it removes the first occurance of the item
print(l)
l.remove('vishnu')
print(l)

# creates and returns a copy 
l2=l.copy()
l3=l
# print(id(l2))
# print(id(l))
# print(id(l3))

# dictionary
person={
    'name':'Mani',
    'age':19,
    'course':'Python'
}

print(person.keys())

print(person.values())

print(person.items())

# for key,value in person.items():
#     print(key, " : ",value)


# person['phoneno']=9876543210

# person['name']='bhuvi'
# print(person)

# # deleting a single pair from dict
del person['age']

#################################################
#  conditional staements

age=12

l2=[1,2,3,4,5,6]
# if (age >15):
#     print(age ," yes !!") 
# elif age >10 and age <15:
#     print("im in btn 10 and 15")
# else :
#     print("no!!!")

if 5 not in l2:
    print("yes in there!!")
else:
    print("")


