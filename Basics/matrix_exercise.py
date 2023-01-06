#####------------------ Matrix Programs --------------######

m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[19, 18, 17],
      [16, 15, 14],
      [13, 12, 11]]

m = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

n = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Matrix Addition

for i in range(0, len(m1)):
      for j in range(len(m1[0])):
            m[i][j] = m1[i][j] + m2[i][j]

print(m)


# Matrix Multiplication

for i in range(0, len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            n[i][j] += m1[i][k] * m2[k][j]

print(n)

# Matrix Product

a = [[2, 5, 7], [3, 6], [8], [4, 9]]
prod = 1

for i in a:
    for j in range(len(i)):
        prod *= i[j]

print(prod)





