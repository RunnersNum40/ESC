def count_evens(L):
    return  [n%2 for n in L].count(0)

def list_to_str(lis):
    return "["+", ".join(map(str, x))+"]"

def lists_are_the_same(list1, list2):
    return len(list1) == len(list2) and all(x==y for x, y in zip(list1, list2))

def simplify_fraction(n, m):
    fac1, fac2 = n, m
    while fac2:
        fac1, fac2 = fac2, fac1%fac2
    print("{}/{}".format(n/fac1, m/fac1))

from math import pi, floor
def pi_iterations(n):
    n = 10**n
    goal = floor(pi*n)/n
    iterations = 0
    total=0.0
    while floor(4*total*n)/n != goal:
        total += ((-1)**iterations)/(2*iterations+1)
        iterations += 1

    print(4*total)
    return iterations

for n in range(10):
    print(n, pi_iterations(n))