#Problem 1
def list1_start_with_list2(list1, list2):
    return len(list1) >= len(list2) and all(x==y for x, y in zip(list1, list2))

#Problem 2
def match_pattern(list1, list2):
    pattern_length = len(list2)
    for i in range(len(list1)-pattern_length):
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
    return [[*map(lambda n:n*v, row)] for row in M]