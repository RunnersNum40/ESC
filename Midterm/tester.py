from midterm import *

x = [10.4, 1.6, 2, 0.2, 0, 0, 5.2, 0, 0, 0, 0, 0, 3.8, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 2.0, 0, 0, 0, 8.4, 2.2, 5.0]
y = moving_average(x)
print(y, len(x)-len(y))

M1 = [[1, 2, 3], [3, 4, 5]]
M2 = [[1, 2, 3], [3, 8, 5]]

print([*zip(*M1)])
print(share_n1(M1, M2))
print(match("czczczczczczczczczczczczczcza", "czaczczczczczczczczczczczczc"))