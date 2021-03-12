# Strings general operations

s = "this is a string"
t = "another one"
r = "one"

# Access based 0 a location
print(s[3]) 

# Length
print(len(s))

# Concatenating
print(s+t)

# Silicing [includes index, exculdes index] base 0 indexing
print(s[2:4])

# Find
print(r in t)
print(s in t)

# Strip - Remove leading and trailing spaces
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# Or specific characters
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

# Starts with

print(s.startswith("this"))

# Ends with
print(s.endswith("ostring"))
print(s.endswith("string"))

# Split
a = 'a,b,c,d'
a_array = a.split(',')
print(a_array)

# Reproduce
print(3 * '01')

# Join - takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = ",".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# To Lower
f = "HEY"
print(f.lower())

# Substitute
e = 'Name: {name}, Rank: {rank}'.format(name='Ricardo', rank='Apprentice')
print(e)