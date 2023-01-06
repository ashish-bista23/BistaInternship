# Words which are greater than length K

str = input("Enter a String:")
k = 3
l = list(str.split())

for i in l:
    if len(i) > k:
        print(i, end=' ')


# Removing i th Character from String

s = input("Enter a String:")
pos = int(input("Enter Index to be deleted:"))

for i in s:
    if s.index(i) == pos:
        continue
    else:
        print(i, end='')

# Split and join string

s = input("Enter a String:")

l = list(s.split())
print(l)
print("-".join(l))          # String Join with Delimiter


# String is Binary or not

s = input("Enter a String:")
if set(s) == {'1'} or set(s) == {'0'} or set(s) == {'0', '1'}:
    print("String is Binary.")
else:
    print("String is not Binary.")


# Uncommon Words from 2 Strings

str1 = "Apple Mango Banana"
str2 = "Mango Banana Watermelon"
n =[]

l = list(str1.split())
m = list(str2.split())

for i in l:
    if i not in m:
        n.append(i)

for j in m:
    if j not in l:
        n.append(j)

print("Uncommon Words in both Strings are:", n)


# Permutations of a given String

from itertools import permutations

str = 'ASH'
permList = permutations(str)

for i in list(permList):
    print(''.join(i))


# Check for URL in String

str = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
result = []
s = str.split()

for i in s:
    if i.startswith('https:') or i.startswith('http:') or i.startswith('www'):
        result.append(i)

print(result)


# String Slicing in Python to rotate a string

s = 'ashishghadi123'
d = 3

print("After Left Rotation:")
result = s[d:] + s[:d]
print(result)

print("After Right Rotation:")
result = s[len(s)-d:] + s[:len(s)-d]
print(result)


# Duplicate Characters in String

str = 'ashishghadi'
freq = []
s = set()

for i in str:
    if i in freq:
        s.add(i)
    else:
        freq.append(i)

for i in s:
    print(i, end=' ')


# Replace all occurrences of substring in a String

str = 'ashish'
s1 = 'sh'
s2 = 'pr'

s = str.replace(s1, s2)
print(s)

