# -------------------List Programs----------------------

# Interchange first & last element of list

a = [23, 14, 57, 29, 10, 84, 69, 93]

b = a[0]
a[0] = a[-1]
a[-1] = b

print(a)


# swap 2 elements of list

i = int(input("Enter Index value to be swapped:"))
j = int(input("Enter Index value swapped with:"))

b = a[i]
a[i] = a[j]
a[j] = b

print(a)


# length of List

print(len(a))


# Element Exist in List

n = int(input("Enter element to be searched:"))

if n in a:
    print("{0} is present in the list.".format(n))
else:
    print("{0} is not present in the list.".format(n))


# Clear List

b = a
print(b)
b.clear()
print(b)


# Reverse List

a.reverse()
print(a)


# Sum of elements in List
s = 0
for i in a:
    s = s + i
print("Sum of List Elements is:", s)


# Multiply all elements in list
b = [12, 4, 5, 26]
s = 1
for i in b:
    s = s * i
print("Product of List Elements is:", s)


# Smallest Number in the List
low = min(b)
print(low)


# Largest Number in the List
large = max(b)
print(large)


# Second Largest in a List
b.sort()
print("Second Largest Element of a List is:", b[-2])


# Even Numbers in List
for i in a:
    if i%2 == 0:
        print(i, end=' ')


# Odd Numbers in List
for i in a:
    if i%2 == 1:
        print(i, end=' ')


# Even Numbers in Range
for i in a[0:5]:
    if i%2 == 0:
        print(i, end=' ')


# Odd Numbers in Range
for i in a[0:5]:
    if i%2 == 1:
        print(i, end=' ')


# Positive Numbers in a List

x = [29, -4, 38, 94, -2, -68, -26, 78]

for i in x:
    if i > 0:
        print(i, end=' ')


# Negative Numbers in a List

for i in x:
    if i < 0:
        print(i, end=' ')


# Positive Numbers in Range

for i in x[0:5]:
    if i > 0:
        print(i, end=' ')


# Negative Numbers in Range

for i in x[0:5]:
    if i < 0:
        print(i, end=' ')


# Remove multiple elements from a list

for i in x[0:4]:
    del x[i]

##  del x[0:4]


# Remove Empty List from a List

l = [20, [], 17, -36, [], [23, 57]]

for i in l:
    if not i:
        l.remove(i)

print(l)


# Cloning or copying a List

c = l.copy()
print(c)


# Occurrences of an element in List

p = [20, 89, 17, -36, 17, 23, 57, 17]

count = 0
for i in p:
    if i == 17:
        count += 1

print("Occurrences of 17 in a list are:", count)


# Remove Empty Tuples from a List

t = [(), ('ram', '15', '8'), (), ('Laxman', 'sita'), ('krishna', 'akbar', '45'), ('', ''), ()]

for i in t:
    if len(i) == 0:
        t.remove(i)

print(t)


# print duplicates from a list integers

p = [20, 89, 17, 36, 17, 20, 57, 57]

repeat = []
for i in range(0, len(p)):
    for j in range(i+1, len(p)):
        if p[i] == p[j] and p[i] not in repeat:
            repeat.append(p[i])

print(repeat)


# Cumulative Sum of List

p = [20, 9, 17, 36, 27]

cumulative_sum = []

for i in range(0, len(p)):
    if i == 0:
        cumulative_sum.append(p[i])
    else:
        cumulative_sum.append(cumulative_sum[i-1] + p[i])

print(cumulative_sum)


# Sum of Number Digits in List

p = [20, 9, 17, 36, 67]

sum_of_digits = []

for i in p:
    sum = 0
    while i > 0:
        rem = i % 10
        sum += rem
        i = i//10
    sum_of_digits.append(sum)

print(sum_of_digits)


# Break List into chunks of Size N

s = [20, 9, 17, 36, 67, 29, 48, 98, 33, 73, 59, 84]

for i in range(0, len(s), 4):
    x = i
    print(s[x:x+4])



