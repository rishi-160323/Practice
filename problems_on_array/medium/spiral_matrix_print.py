# It has only solution in present(optimal).
def sprial_matrix_print(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    result = []

    while top <= bottom and left <= right: # this is the important don't forget.
        # row(forward)
        i = left
        while i <= right:
            result.append(matrix[top][i])
            i+=1
        top += 1
        
        # column(forward)
        j = top
        while j <= bottom:
            result.append(matrix[j][right])
            j+=1
        right -= 1
        
        if top <= bottom: # if matrix is not square and only single row.
            # row(backword)
            k = right
            while k >= left:
                result.append(matrix[bottom][k])
                k-=1
            bottom -= 1
        
        if left <= right:  # if matrix is not square and only column row.
            # column(backword)
            l = bottom
            while l >= top:
                result.append(matrix[l][left])
                l -= 1
            left += 1
    return result
        




input = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

# input = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# input = [
#     [1,2,3],
#     [5,6,7],
#     [9,10,11],
#     [13,14,15]
# ]
print(sprial_matrix_print(input))


"""
1. We use for pointer here to track the elements.
2. Two check while traversing backwords(important when matrix is not square.).
"""