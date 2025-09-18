# comes as rotate image 90 degree.

from utils import print_matrix_table_decorator
from copy import deepcopy

# Brute force approach.
def create_new_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([-1 for j in range(len(matrix[i]))])
    return new_matrix

@print_matrix_table_decorator
def rotate_matrix_90_degree(matrix):

    new_matrix = create_new_matrix(matrix)

    # new_matrix = matrix # totally shalow copy
    # new_matrix = matrix[:] # new_matrix is a new list object, but its elements (the inner lists) are still the same references as in matrix.
    # new_matrix = deepcopy(matrix) # deep copy

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            m = j
            n = (len(matrix)-1)-i # try to observe the pattern while rotating using pen and paper.
            new_matrix[m][n] = matrix[i][j]
    return new_matrix



input = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# rotate_matrix_90_degree(input)

"""
Time Complexity: O(N*N) to linearly iterate and put it into some other matrix.

Space Complexity: O(N*N) to copy it into some other matrix."""



# optimal approach. (Doesn't use extra new matrix)
@print_matrix_table_decorator
def rotate_matrix_90_degree(matrix):

    # intension is to get the transpose of the matrix.
    # transpose means rows become columns and columns become rows.
    # then we will reverse each row to get the 90 degree clockwise tilted matrix.
    # but here we track a pattern while transposing and follow that pattern to make transpose.
    # the diagonal element that is ([0][0] to [n][n]) will remain same while transposing.(Insight)

    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversed(matrix[i]) # doen't modify in place instead returns another.
        matrix[i].reverse()
    return matrix
    

input = [[1,2,3],
         [4,5,6],
         [7,8,9]]

rotate_matrix_90_degree(input)



"""
Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.

Space Complexity: O(1)."""




























@print_matrix_table_decorator
def rotate_matrix_90_degree(matrix):
    n = len(matrix)

    # Step 1: Transpose (swap across diagonal)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix


input = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# rotate_matrix_90_degree(input)