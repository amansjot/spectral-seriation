import math
import os, sys

sys.path.insert(1, os.path.join(sys.path[0], '../src'))
from approx_cutnorm import *

# --- functions for special types of matrices ---

# function to create a matrix of alternating 1s and -1s

def checkerboard_matrix(n):
    # initialize zero matrix of size n
    m = np.array([[0.0 for _ in range(n)] for _ in range(n)])

    # loop through rows and cols
    for i in range(n):
        for j in range(n):

            # if sum of cell indices is even, cell is 1
            if (i + j) % 2 == 0:
                m[i][j] = 1

            # otherwise, cell is -1
            else:
                m[i][j] = -1

    # return filled matrix
    return m

# function to randomly permute a checkboard of 1s and -1s

def perm_checkerboard_matrix(n):
    # initialize n x n array of zeroes
    m = np.array([[0.0 for _ in range(n)] for _ in range(n)])

    # shuffle indices to create a random permutation
    A = list(range(n))
    random.shuffle(A)

    # loop through rows and cols
    for i in range(n):
        for j in range(n):

            # map each cell to 1 or -1 based on the shuffled list
            m[i][j] = 2 * ((A[i] + A[j]) % 2) - 1

    # return filled matrix
    return m

# creating 50x50 matrix of zeroes to use for checkerboard matrices

size = 50
matrixB = zero_matrix(size)

# testing cutnorm of random permutation to show equality

cutn_round, cutn_sdp, info = compute_cutnorm(checkerboard_matrix(size), matrixB)
cutn_round = round(cutn_round, 8)
print("checkerboard cutnorm:", cutn_round)

cutn_round, cutn_sdp, info = compute_cutnorm(perm_checkerboard_matrix(size), matrixB)
cutn_round = round(cutn_round, 8)
print("permuted checkerboard cutnorm:", cutn_round, "\n")

# testing separate functions of all types (verified)

test_functions = []

function1 = lambda x, y : 1 - abs(y - x)
function2 = lambda x, y : (x - y) / 2
function3 = lambda x, y : 5
function4 = lambda x, y : (x + y) / 2
function5 = lambda x, y : math.cos(math.pi * (x - y))
function6 = lambda x, y : math.cos(2 * math.pi * (x - y))
function7 = lambda x, y : ((x * y) ** 2) - (3 * x * y) + 1

test_functions.append(function1)
test_functions.append(function2)
test_functions.append(function3)
test_functions.append(function4)
test_functions.append(function5)
test_functions.append(function6)
test_functions.append(function7)

for i in range(len(test_functions)):
    func = test_functions[i]
    print( "function" + str(i + 1) + ":", approx_cutnorm(func, 8) )
