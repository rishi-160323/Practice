# https://takeuforward.org/data-structure/set-matrix-zero/

# Mark entire row and column with zero wherever you find zeroes.


from utils import print_matrix_table_decorator

def mark_row(matrix, row):
    for i in range(len(matrix[row])):
        if matrix[row][i] != 0:
            matrix[row][i] = -1

def mark_colum(matrix, column):
    for i in range(len(matrix)):
        if matrix[i][column] != 0:
            matrix[i][column] = -1


def replace_with_zeroes(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==-1:
                matrix[i][j] = 0
    return matrix
    

@print_matrix_table_decorator
def set_matrix_zeroes(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                mark_row(matrix, i)
                mark_colum(matrix, j)
    return replace_with_zeroes(matrix)



input = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# set_matrix_zeroes(input)

"""Here key points is, to mark the rows and columns having 0s we use -1 insted of 0 else it will mess all the to tarck the 0s."""

"""
Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.

Reason: Firstly, we are traversing the matrix to find the cells with the value 0. It takes O(N*M). Now, whenever we find any such 
cell we mark that row and column with -1. This process takes O(N+M). So, combining this the whole process, finding and marking, takes
O((N*M)*(N + M)).

Another O(N*M) is taken to mark all the cells with -1 as 0 finally.

Space Complexity: O(1) as we are not using any extra space."""








# Better Approach.

@print_matrix_table_decorator
def set_matrix_zeroes(matrix):

    # this is keep track where the zeroes are.
    horizontal_arr = [0]*len(matrix[0]) # to keep track of columns
    vertical_arr = [0]*len(matrix) # to keep track of rows

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # replacing with in side arrays.
            if matrix[i][j] == 0:
                horizontal_arr[j]=1
                vertical_arr[i]=1
    
    for i in range(len(vertical_arr)):
        for j in range(len(horizontal_arr)):
            # if vertical_arr[i] or horizontal_arr[j] == 1: # wrong way
            if vertical_arr[i] ==1 or horizontal_arr[j] == 1: # key
                matrix[i][j]=0
    return matrix
    


input = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# set_matrix_zeroes(input)


"""Here we keep track that which row and column has zeros using two side arrays
 one is 'horizontal_arr' and another is 'vertical_arr'."""


"""
Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: O(N) is for using the row array and O(M) is for using the col array.
"""








# optimal solution(saving space for arrays which we used to track 0s in better approach).

@print_matrix_table_decorator
def set_matrix_zeroes(matrix):

    """
    Set Matrix Zeroes (in-place solution with O(1) extra space).
    Idea:
      - Use first row & first column as "marker arrays"
      - Use an extra variable `c0` to track the zeroth column
    """


    c0 = 1 # this keeps track whether there is any 0 in matrix[i][0](Zeroth column of matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                if j != 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                else:
                    c0 = 0 # key and important
                    
    # except marker arrays we are re-writing other arrays.
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][0] ==0 or matrix[0][j] == 0:
                matrix[i][j]=0

    """Crucial strep to re-write the arrays which we have used to keep the track(first row and first column)."""

    # marking 0 in first row.
    if matrix[0][0] == 0:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    # marking 0 in first column.
    if c0 == 0:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    return matrix



input = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[0,1,1,1]]
set_matrix_zeroes(input)



"""
Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(1) as we are not using any extra space.
"""