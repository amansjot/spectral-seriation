# Python implementation of the spectral-sort algorithm mathematically notated
# in the Atkins-Boman-Hendrickson paper on Spectral Seriation (1998)

import numpy as np

def dfs(A: list[list[int]], vertex: int, visited: list[bool], indices: list[int]):
    # set vertex to visited
    visited[vertex] = True
    indices.append(vertex)
    
    # recurse on all unvisited neighbors
    for neighbor in range(len(A)):
        if A[vertex][neighbor] == 1 and not visited[neighbor]:
            dfs(A, neighbor, visited, indices)

def irreducible_blocks(A: list[list[int]], U: list[int]) -> tuple:
    # create lists to check if visited and for blocks and sets  
    visited = [False] * len(A)
    blocks = []
    index_sets = []

    # if vertex is not visited
    for vertex in range(len(A)):
        if not visited[vertex]:

            # run dfs to find irreducible blocks
            indices = []
            dfs(A, vertex, visited, indices)

            # find the blocks based on index
            block = np.array(A)[np.ix_(indices, indices)]
            blocks.append(block)

            # add the indices
            indices = [U[index] for index in indices]            
            index_sets.append(indices) 

    # returns irreducible blocks and sets
    return blocks, index_sets

def fiedler_vector(A: list[list[int]]):
    # find the Lapplacian matrix
    D = np.diag(np.sum(A, axis=1))
    L = D - A

    # return the second smallest eigenvalue (Fiedler vector) 
    eigenvalues, eigenvectors = np.linalg.eig(L)
    sorted_indices = np.argsort(eigenvalues)
    return eigenvectors[:, sorted_indices[1]]

def spectral_sort_pq(A: list[list[int]], U: list[int]) -> str:
    # length of A
    n = len(A)

    # subtract the minimum value element-wise
    A -= np.min(A)

    # find irreducible blocks and sets
    blocks, index_sets = irreducible_blocks(A, U)
    
    # if there are multiple irreducible blocks
    if len(blocks) > 1:

        # recurse on each block
        T = []
        for j in range(len(blocks)):
            T.append( spectral_sort_pq(blocks[j], index_sets[j]) )
        
        # surround each node or element in a P-node
        return "(" + ", ".join(map(str, T)) + ")"
        
    # if there is only one irreducible block
    else:

        # if the block is only one element long, return the element
        if n == 1:
            return U[0]

        # if the block is 2 elements long, return both in a P-node
        elif n == 2:
            return "(" + ", ".join(map(str, U)) + ")"

        # if the block is >2 elements long...
        else:
            
            # find and sort the Fielder vector of A
            x = fiedler_vector(A)
            x_sorted = np.sort(x)
            unique_vals = np.unique(x_sorted)

            # split the matrix based on Fiedler vector values
            T = []
            for j in range(len(unique_vals)):
                Vj = np.where(x == unique_vals[j])[0]
                Aj = np.array(A)[Vj, :][:, Vj]
                Uj = np.array(U)[Vj]

                # recurse on each value for specific blocks and sets
                T.append( spectral_sort_pq(Aj, Uj) )

            # surround each element in a Q-node
            return "[" + ", ".join(map(str, T)) + "]"
