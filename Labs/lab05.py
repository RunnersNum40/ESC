#Problem 1
def list1_start_with_list2(list1, list2):
    return len(list1) >= len(list2) and all(x==y for x, y in zip(list1, list2))

#Problem 2
def match_pattern(list1, list2):
    pattern_length = len(list2)
    for i in range(len(list1)-pattern_length+1):
        if list1[i:i+pattern_length] == list2:
            return True
    return False

#Problem 3
def repeats(list0):
    for n, item in enumerate(list0[:-1]):
        if item == list0[n+1]:
            return True
    return False

#Problem 4
    #Problem 4a
def print_matrix_dim(M):
    print("{}x{}".format(len(M), len(M[0])))

    #Problem 4b
def mult_M_v(M, v):
    return [sum(row[n]*v[n] for n in range(len(row))) for row in M]

    #Problem 4c
def mul(A, B):
    height = len(A)
    new = [[None for c in range(height)] for r in range(height)]
    for x in range(height):
        for y in range(height):
            new[x][y] = sum([n*i for n, i in zip(A[x], [row[y] for row in B])])
    return new

if __name__ == '__main__':
    x = list(range(10))
    y = list(range(5))
    z = list(range(5, 10))
    print(x, y, z)
    print(list1_start_with_list2(x, y))
    print(match_pattern(y, x))
    print(match_pattern(x, z))
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    v = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    print(mul(M, v))