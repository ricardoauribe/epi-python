# Arrays

## Core Functions

```
a = [1,2,3,4,5]

```
### Append

```
a.append(6)
```

### Remove

```
a.remove(2)
```

### Insert (location, item)

```
a.insert(1,28)
```

### 2D Array

```
b=[[1,2],[3,4,5],[6,7]]
```

### Is in

```
print(3 in a)
print(9 in a)
```

### Min

```
print(min(a))
print(max(a))
```

### Copies

Shallow, items are just referenced not really independent

```
new_b = copy.copy(b)
b[0][0] = 33
```

Deepcopy are fully independent

```
new_b2 = copy.deepcopy(b)
b[0][0] = 44
print(new_b2)
print(b)
```

### Reverse

```
a.reverse() 
```

### Sort

```
a.sort()
```

### Slicing 

TODO: Add all operations in page 41

```
d = a[2:]
```
print(d)

### List comprehension

```
c=[x**2 for x in range(6)]
print(c)
```

## Resolved Problems
