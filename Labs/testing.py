from numpy import array

#q1
def print_matrix(M_lol):
    M = array(M_lol)
    #Now print it:
    print(M)

#problem 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)


#problem 3
def get_row_to_swap(M, start_i):
    smallest = []
    for i in range(start_i+1,len(M)):#looking after the one you are subbing in with
        lead = get_lead_ind(M[i])
        smallest.append(lead)

    #outside loop
    small = min(smallest)
    return smallest.index(small) + 1 + start_i


#problem 4
def add_rows_coefs(r1,c1,r2,c2):
    new_list = []
    for num in range(len(r1)):
        new_list.append(r1[num]*c1 + r2[num]*c2)
    return new_list

#problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    eraser = M[row_to_sub][best_lead_ind]

    for i in range(row_to_sub+1, len(M)):
        turn_to_zero = M[i][best_lead_ind]
        multiply = -1*(turn_to_zero / eraser)
        M[i] = add_rows_coefs(M[i],1,M[row_to_sub],multiply)

    return M


#problem 6
def forward_step(M):
    for i in range(len(M)-1):
        M[get_row_to_swap(M, i)], M[i] = M[i], M[get_row_to_swap(M,i)]
        eliminate(M, i, get_lead_ind(M[i]))
        print_matrix(M)
    return M 

# problem 7
M = [[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]]
print(get_row_to_swap(M, 0))
M = forward_step(M)