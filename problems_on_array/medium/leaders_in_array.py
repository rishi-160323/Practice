# https://takeuforward.org/data-structure/leaders-in-an-array/

"""Everything in the right should be smaller."""
"""An element is a leader if it is greater than or equal to all the elements to its right (i.e., strictly the maximum 
from its position till the end)."""

# Broute force approach.
def get_leaders(arr):
    leaders_arr = []
    for i in range(len(arr)):
        leader = True
        for j in (range(i+1, len(arr))):
            if arr[i]<arr[j]:
                leader = False
                break
        if leader:
            leaders_arr.append(arr[i])
    return leaders_arr

print(get_leaders([16, 17, 4, 3, 5, 2]))


# optimal solution.
"""Here we will traverse reversely and will keep the max element and then we will compare with the ith element whether it is
grater or smaller."""

import sys

def get_leaders(arr):
    idx = len(arr) -1
    last_max = -sys.maxsize-1
    leaders = []
    while idx >= 0:
        if arr[idx]>last_max:
            last_max = arr[idx]
            leaders.append(arr[idx])
        idx -= 1
    return leaders[::-1]


print(get_leaders([16, 17, 4, 3, 5, 2]))
