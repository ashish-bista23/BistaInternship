# --------------------------String Programs--------------------------

# Palindrome or not

str = input("Enter String:")

if str == str[::-1]:
    print("{0} is Palindrome.".format(str))
else:
    print("{0} is not a Palindrome.".format(str))


# Symmetrical or not

str = input("Enter String:")

if len(str) % 2 == 0:
    if str[:(len(str)//2)] == str[len(str)//2:]:
        print("{0} is Symmetrical String.".format(str))
    else:
        print("{0} is not a Symmetrical String.".format(str))
else:
    print("{0} is not a Symmetrical String.".format(str))


# Reverse String

s = input("Enter String:")

print(s[::-1])


# Reverse Words in given String

s = input("Enter String:")

r = s.split()
r = r[::-1]

for i in r:
    print(i, end=' ')


# Remove nth character from String

s = input("Enter String:")
index = int(input("Enter Index to be removed:"))

if index < len(s):
    s = s[:index] + s[index+1:]
    print(s)
else:
    print("Enter Valid Index!!")


# Substring present in String

s = input("Enter String:")
sub = input("Enter Substring:")

if s.find(sub) >= 0:
    print("Substring is present.")
else:
    print("Substring is not present.")


# Words Frequency in String

str = input("Enter String:")

for key in str.split():
    res = {key: str.count(key)}
    print(res)


# Snake Case to Pascal Case

snake_case = input("Enter String:")

pascal_case = snake_case.replace("_", " ").title().replace(" ", "")
print(pascal_case)


# Length of a String

str = input("Enter String:")
print(len(str))


# Print Even Length Words from String

s = input("Enter String:")
word = s.split()

for i in word:
    if len(i) % 2 == 0:
        print(i)


# Number of matching Characters in a pair of strings

str1 = set(input("Enter String1:"))
str2 = set(input("Enter String2:"))

common_characters = str1 & str2

print("No. of Matching Characters in both Strings are:", len(common_characters), " & they are:", common_characters)


# Remove all duplicates from given String

str = input("Enter a String:")
######### Without Order #########
s = set(str)
print("Without Order:")
for i in s:
    print(i, end='')

######### With Order #########

p = ""
for i in str:
    if i in p:
        continue
    else:
        p += i

print("\nWith Order:", p)


# Least frequent Character in String

str = input("Enter String:")

freq = {}

for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

least_frequent = min(freq, key=freq.get)
print("Least Frequent Character in given String is:", least_frequent)

minimum_freq = min(zip(freq.values(), freq.keys()))
print("Least Frequent Character in given String is:", minimum_freq[1])


# Maximum Frequent Character in String

str = input("Enter String:")
freq = {}

for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
############ Using max() & key  ###############
max_frequent = max(freq, key=freq.get)
print("Max Frequent Character in given String is:", max_frequent)

############ Using max() & zip() ##############
maximum_freq = max(zip(freq.values(), freq.keys()))
print("Max Frequent Character in given String is:", maximum_freq[1])


# check if string contains any special character

s = input("Enter a String:")


def check_special_character(str):
    for i in str:
        if i.isalpha() or i.isdigit() or i == ' ':
            continue
        else:
            return 0
    return 1


if check_special_character(s):
    print("String does not contain Special Character.")
else:
    print("String contains Special Character.")


