# -------------------Tuple Programs----------------------

# Size of Tuple

a = (1, 23, 45, 69, 37, 81, 97, 17)

print("Size of Tuple is:", len(a))

# Max and Min in Tuple

print("Maximum:", max(a))
print("Minimum:", min(a))

# Make List of Tuples from List Element with their Cubes

l = [3, 6, 4, 8, 2, 7, 9]
t = []

for i in l:
    t.append(tuple((i, i**3)))
print(t)


# Adding Tuple to List and Vice Versa

p = [1, 2, 3, 4, 5]
q = (7, 6, 8)

r = p + list(q)
print(r)

r = tuple(list(q) + p)
print(r)


# join tuples if similar first element

l = [(5, 6, 12, 16), (5, 7, 18), (6, 8, 11, 20), (6, 10, 9), (7, 13, 21, 23)]
first_element = []
final_list = []

for i in l:
    if i[0] not in first_element:
        first_element.append(i[0])

for i in first_element:
    p = []
    p.append(i)
    for j in l:
        if i == j[0]:
            for k in range(1, len(j)):
                p.append(j[k])
    final_list.append(p)

print("Final List:", final_list)


# All Pair Combinations of 2 Tuples

t1 = (1, 2, 3)
t2 = (5, 6)

result = [(i, j) for i in t1 for j in t2] + [(i, j) for i in t2 for j in t1]

print(result)


# Remove Tuples of Length K

l = [(1, 2), (3, 4, 5), (6,), (7, 8), (9,), (10, 11, 12), (13, 14, 15, 16)]
k = 3

for i in l:
    if len(i) == k:
        l.remove(i)

print(l)


# Sort List of tuples by Second Item of each Tuple

d = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]

d.sort(key=lambda i: i[1])
print(d)


# Flatten tuple of list to tuple

t = ([5], [6, 7, 1], [3, 2], [8, 9, 11, 4])
result = []

for i in t:
    for j in range(0, len(i)):
        result.append(i[j])

print(tuple(result))


# Convert Nested tuple to Custom Key Dictionary

t = ((1, 'abc'), (2, 'def'))
keys = ['key', 'value']
result = []

for i in t:
    for j in range(0, len(i)):
        result.append({keys[j]: i[j]})
print(result)

