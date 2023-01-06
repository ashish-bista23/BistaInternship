# Formatting
age = 20
name = "John"

print('{0} is {1} years old.'.format(name, age))

# '//' Operator <- Floor Division (returns quotient)
a = 22 // 7
print(a)  # output will be 3

# Divisibility Check
for i in range(1, 101):
    if(i % 7 == 0):
        print("{0} is divisible by 7.".format(i))

# break & continue keywords

list = [1,2,3,4,5,6]

for i in list:
    if i == 5:
        break
    if i == 3:
        continue
    print(i)    # Output will be 1 2 4

# For Loop increment by 2 or 3

for i in range(0, 11, 2):
    print(i)        # output would be 0 2 4 6 8 10

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for j in list[::3]:
    print(j)        # output would be 1 4 7 10

# docstrings

def add(a,b):
    '''
    This function returns addition of 2 numbers.
    :param a: num1
    :param b: num2
    :return: sum
    '''

    c = a+b
    return c


sum = add(9, 10)
print(sum)
print(add.__doc__)      # Returns Docstrings which mentioned in ''' quotes


# List Delete Element

list = [1, 2, 3, 4, 5, 6, 7]

del list[0]     # output would be 2 3 4 5 6 7


# Dictionary

dic1 = {
    'name': 'Ashish',
    'age': '24'
}

for name, age in dic1.items():
    print("{0}: {1}".format(name, age))     # output be name: Ashish age: 24

  # can have multiple Distionaries inside single List

#-----------------------------------------------------------------------------------------

# OOP Concepts







