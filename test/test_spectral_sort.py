# test cases for src/spectral_sort.py

import os, sys

sys.path.insert(1, os.path.join(sys.path[0], '../src'))
from spectral_sort import *

# testing 6 matrices to show pq permutation (verified)

matrix1 = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
matrix2 = [[1, 1, 2], [1, 1, 1], [2, 1, 1]]
matrix3 = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
matrix4 = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]]
matrix5 = [[0, 1], [1, 0]]
matrix6 = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

print( spectral_sort_pq(matrix1, range(1, len(matrix1)+1)) )
print( spectral_sort_pq(matrix2, range(1, len(matrix2)+1)) )
print( spectral_sort_pq(matrix3, range(1, len(matrix3)+1)) )
print( spectral_sort_pq(matrix4, range(1, len(matrix4)+1)) )
print( spectral_sort_pq(matrix5, range(1, len(matrix5)+1)) )
print( spectral_sort_pq(matrix6, range(1, len(matrix6)+1)) )