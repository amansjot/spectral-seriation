# main file to plot the convergence of a graphon

import random
import re
import numpy as np
from matplotlib import pyplot as plt

from spectral_sort import *
from is_robinson import *
from approx_cutnorm import *
from graphon_matrix import *

# main function to plot cut norm difference convergence

def test_convergence(U, phi, trials):

    cutnorms = {}

    # use phi to map U to W
    U_phi = W = lambda x, y: U(phi(x), phi(y))

    # for each matrix size n... 
    for n in trials:

        # aample W to create weighted matrix G, then convert to unweighted
        w_matrix = graphon_to_weighted_adj_matrix(U_phi, n)
        uw_matrix = weighted_adj_matrix_to_unweighted(w_matrix)

        # find the Fielder vector
        uw_fiedler = fiedler_vector(uw_matrix)

        # run the spectral-sort algorithm, then choose one pq permutation
        pq_tree = spectral_sort_pq(uw_matrix, range(len(uw_matrix)))
        pq_perm = [int(num) for num in re.findall(r'\d+', pq_tree)]

        # account for errors in spectral_sort returned indexes (must fix)
        if sorted(pq_perm) != list(range(len(pq_perm))):
            print("error: bad pq permutation\n")

        else:
            # convert pq-permutation indices to matrix
            A = indexes_to_matrix(uw_matrix, pq_perm)
            B = function_to_matrix(U, n)

            # approximate the cutnorm of || Hn - U ||
            cutn_round, cutn_sdp, info = compute_cutnorm(A, B)
            # print(cutn_round, "\n")

            # if size n is repeated, average the values
            if n in cutnorms:
                cutnorms[n] += cutn_round
            else:
                cutnorms[n] = cutn_round

            print(n, ":", cutn_round)

    # plot cutnorm
    plt.plot(trials, cutnorms.values())

if __name__ == '__main__':

    # 8 example graphon functions

    U_functions = []

    U0 = lambda x, y: 1

    h1 = lambda x, y: max(min(x, 1 - x), min(y, 1 - y))
    U1 = lambda x, y: 1 - h1(x, y) if np.sign(x - 1/2) == np.sign(y - 1/2) else h1(x, y)

    U2 = lambda x, y : 1 - abs(x - y)

    h3 = lambda x, y: max(0, 0.5 - abs(x - 0.5) - abs(y - 0.5))
    U3 = lambda x, y: 1 - h3(x, y) if np.sign(x - 1/2) == np.sign(y - 1/2) else h3(x, y)

    U4 = lambda x, y: 0.5 - abs(x - 0.5) - abs(y - 0.5)

    U5 = lambda x, y: 1 - ((max(x, 1-x) + max(y, 1-y)) / 2)

    U6 = lambda x, y: 1 - ((max(y, 1-x) + max(x, 1-y)) / 2)

    U7 = lambda x, y: (1 - abs(x - 0.5)) * (1 - abs(y - 0.5))

    U_functions.append(U0)
    U_functions.append(U1)
    U_functions.append(U2)
    U_functions.append(U3)
    U_functions.append(U4)
    U_functions.append(U5)
    U_functions.append(U6)
    U_functions.append(U7)

    # --- use only this line to test all U_functions ---
    # for U in U_functions:

    # --- use only this line to test specific functions (by number) ---
    for U in [U1]:

        # for higher accuracy, set repeat to a higher value!
        # (this will multiply the runtime by the value of repeat)
        repeat = 1

        # set trials for matrix sizes
        trials = (list(range(5, 51+1))) * repeat

        # choose function to run with phi
        phi = lambda p: 1 - p
        test_convergence(U, phi, trials)

    # show plot
    plt.xlabel('Matrix Size')
    plt.ylabel('Cut Norm Difference')
    plt.show()
