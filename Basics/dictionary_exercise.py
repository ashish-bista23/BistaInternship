# -------------------Dictionary Programs------------------------

# Extract Unique Values from Dictionary Values

d = {'gfg': [5, 6, 7, 8],
     'is': [10, 11, 7, 5],
     'best': [6, 12, 10, 8],
     'for': [1, 2, 5]}
l = []

for i in d.values():
    for j in i:
        l.append(j)
print(list(set(l)))


# Sum of All Items in Dictionary

d = {'a': 34, 'b': 57, 'c': 33, 'd': 28}
tot = 0
for i in d.values():
    tot += i

print("Sum of All Items in Dictionary:", sum(d.values()))   # single line output
print("Sum of All Items in Dictionary:", tot)


# Remove Key from Dictionary

d = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

del d['Haritha']
print(d)


# Sort List of Dictionaries by Values using Lambda Function

l = [{"name": "Ashish", "age": 24},
       {"name": "Zeeshan", "age": 22},
       {"name": "Akshay", "age": 22}]

print(sorted(l, key=lambda i: i['age']))
print(sorted(l, key=lambda j: (j['age'], j['name'])))
print(sorted(l, key=lambda k: k['age'], reverse=1))


# Merging 2 Dictionaries

d1 = {'a': 34, 'b': 57, 'c': 33, 'd': 28}
d2 = d = {'Anuradha': 21, 'Harsh': 21, 'Arushi': 22, 'Mani': 21}

d1.update(d2)
print(d1)


# Convert Key-Values List to Dictionary

d = {'month': [1, 2, 3, 4, 5],
     'name': ['Jan', 'Feb', 'March', 'April', 'May']}

l = list(d.values())
x = l[0]
y = l[1]
d = {}

for i in range(0, len(x)):
    d[x[i]] = y[i]

print(d)




