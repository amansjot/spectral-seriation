# tests adjacency matrix for Robinson property (O(n^2))
# - works for undirected/directed (symmetric/asymmetric)
# - works for unweighted/weighted

def is_robinson(M: list[list[int]]) -> bool:
    # loop through rows
    for i in range(len(M)):

        # loop through cols
        for j in range(len(M[i])):

            # right of diagonal - False if down or left is >
            if i + 1 < j and (M[i][j] > M[i+1][j] or M[i][j] > M[i][j-1]):
                return False
                
            # left of diagonal - False if up or right is >
            elif i - 1 > j and (M[i][j] > M[i-1][j] or M[i][j] > M[i][j+1]):
                return False
    
    # True otherwise
    return True

if __name__ == '__main__':
    matrix1 = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    matrix2 = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    matrix3 = [[0, 0.2, 0.5], [0.4, 0, 0.3], [0.1, 0.3, 0]]
    matrix4 = [[0, 0.5, 0.2], [0.4, 0, 0.3], [0.1, 0.3, 0]]

    print( is_robinson(matrix1) )
    print( is_robinson(matrix2) )
    print( is_robinson(matrix3) )
    print( is_robinson(matrix4) )
