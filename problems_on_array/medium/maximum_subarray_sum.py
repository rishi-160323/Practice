# Brute force approach.
"""Make all possible subarrays and compare that which sum is maximum."""

# Better Approach.




# Optimal solution.
"""Kadane's algorithm."""

import sys
def maximum_sum_subarray(arr):

    max = -sys.maxsize - 1
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

        if sum > max:
            max = sum
        
        if sum < 0:
            max = 0
            sum = 0

    return max

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maximum_sum_subarray(arr))




# Optimal solution.(Also returning array.)
"""Kadane's algorithm."""

import sys
def maximum_sum_subarray(arr):

    max = -sys.maxsize - 1
    sum = 0

    start = 0
    ansStart, ansEnd = -1, -1

    for i in range(len(arr)):

        if sum == 0:
            start = i

        sum += arr[i]

        if sum > max:
            max = sum

            ansStart = start
            ansEnd = i
        
        if sum < 0:
            sum = 0

    return ansStart, ansEnd

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_sum_subarray(arr))