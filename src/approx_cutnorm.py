# code to approximate the cutnorm of a function by converting it to a matrix

import math
import random
import numpy as np
from scipy import integrate
from cutnorm import compute_cutnorm

def function_to_matrix(f: callable, n: int):
    # initialize zero matrix of size n
    m = np.array([[0.0 for _ in range(n)] for _ in range(n)])

    # random permutation
    A = list(range(n))
    random.shuffle(A)

    # loop through rows and cols
    for i in range(n):
        for j in range(n):

            # take the double definite integral for dx and dy 
            integration = integrate.dblquad(f, (A[i]/n), (A[i]+1)/n, (A[j]/n), (A[j]+1)/n)[0]
            
            # set cell to the average value
            if abs(integration) > 1.0e-18:
                m[i][j] = integration * n * n
    
    # return filled matrix
    return m

def zero_matrix(n: int):
    # create and return n x n matrix of zeroes
    m = [[0.0 for _ in range(n)] for _ in range(n)]
    return m

def approx_cutnorm(f: callable, round_to: int):
    # initialize max variables
    max_cutnorm = 0
    ideal_size = 0

    # test from s=5 to s=25 to find most accurate approximation
    # (since some multiples have shown higher accuracy)
    for s in range(5, 26):

        # convert f to a s x s matrix
        A = function_to_matrix(f, s)
        
        # create s x s matrix of zeroes
        B = zero_matrix(s)

        # call function to approximate cut norm value
        cutn_round, cutn_sdp, info = compute_cutnorm(A, B)

        # set max value and size
        if cutn_round > max_cutnorm:
            max_cutnorm = cutn_round
            ideal_size = s
    
    # round cutnorm to 8 decimal places
    max_cutnorm = round(max_cutnorm, round_to)
    return max_cutnorm, ideal_size

if __name__ == '__main__':
    function = lambda x, y : math.cos(2 * math.pi * (x - y))
    cutnorm, size = approx_cutnorm(function, 8)
    print("The cutnorm of the function is ~" + str(cutnorm) + ", calculated at a matrix size of", size)