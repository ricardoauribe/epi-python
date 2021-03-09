import copy

# Arrays basics

a = [1,2,3,4,5]

print(len(a))
#Add
a.append(6)
print(a)

#Remove
a.remove(2)
print(a)

#Insert (location, item)
a.insert(1,28)
print(a)

#2D Array
b=[[1,2],[3,4,5],[6,7]]
print(b)

#is in
print(3 in a)
print(9 in a)

#min
print(min(a))
print(max(a))

#Copies
#Shallow, items are just referenced not really independent
new_b = copy.copy(b)
b[0][0] = 33
print(new_b)
#Deepcopy are fully independent
new_b2 = copy.deepcopy(b)
b[0][0] = 44
print(new_b2)
print(b)

#Reverse
a.reverse() 
print(a)

#Sort
a.sort()
print(a)

#Slicing - TODO: Add all operations in page 41
d = a[2:]
print(d)

#List comprehension example
c=[x**2 for x in range(6)]
print(c)