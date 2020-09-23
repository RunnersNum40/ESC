def mul(A, B): return [[sum([n*i for n, i in zip(A[x], [row[y] for row in B])]) for y in range(len(A))] for x in range(len(A))]

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
print(mul(A, B))