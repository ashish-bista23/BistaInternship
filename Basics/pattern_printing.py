n = 10

for i in range(1, n+1):
    for j in range(i, n+1):
        print("*", end='')
    print("\n")


for i in range(1, n+1):
    for j in range(1, i):
        print(" ", end='')
    for k in range(0, n-i+1):
        print("*", end='')
    print("\n")

