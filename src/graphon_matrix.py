# --- all functions relating to graphon and matrix conversions ---

import random
import numpy as np

# convert a graphon into a weighted adjacency matrix

def graphon_to_weighted_adj_matrix(w: callable, n: int) -> list[list[int]]:
    
    # generate n random numbers [0, 1] and sort
    x = [random.uniform(0, 1) for _ in range(n)]
    x.sort()

    # create n x n matrix applying graphon for all pairs of x      
    m = [[w(x[i], x[j]) for i in range(n)] for j in range(n)]

    # return weighted matrix
    return m

# convert a weighted adjacency matrix into an unweighted matrix of 0s and 1s

def weighted_adj_matrix_to_unweighted(A: list[list[int]]) -> list[list[int]]:

    # create matrix of 0s
    m = [[0 for _ in range(len(A))] for _ in range(len(A))]

    # loop through weighted matrix
    for i in range(len(A)):
        for j in range(len(A)):
            if i < j:

                # generate random number
                r = random.uniform(0, 1)

                # prob in unweighted matrix: 1 if >, 0 if <= 
                m[i][j] = 1 if A[i][j] > r and i != j else 0
                m[j][i] = m[i][j]

    # return unweighted matrix
    return m

# function to permute matrix according to given index order

def indexes_to_matrix(A, U):
    n = range(len(A))
    m = np.array([[0 for _ in n] for _ in n])

    for i in n:
        for j in n:
            m[i][j] = A[U[i]][U[j]]

    return np.array(m)

if __name__ == '__main__':
    print("Permuting matrix of 1-9 according to indices [2, 1, 0]:")
    print(indexes_to_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [2, 1, 0]))