# Simple Interest
import math


def simple_interest_calculator(amount, rate, time):
    simple_interest = amount*rate*time/100
    return simple_interest


p = int(input("Enter Amount:"))
r = int(input("Enter Rate per year:"))
t = int(input("Enter Time Period in Years:"))

interest = simple_interest_calculator(p, r, t)
print("Simple Interest for Rs.{0} for {1}% per year rate for {2} years is: Rs.".format(p, r, t), interest)

# Factorial of a Number


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


n = int(input("Enter a Number:"))

f = factorial(n)
print("Factorial of {0} is {1}.".format(n, f))


# Number is Prime or Not

def prime_check(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 0


n = int(input("Enter a Number:"))

ret = prime_check(n)
if ret == 0:
    print("{0} is not a Prime Number.".format(n))
else:
    print("{0} is a Prime Number.".format(n))

