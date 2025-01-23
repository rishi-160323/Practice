"""We can get it done by sorting also in descending order."""

import sys

def largest_ele(arr):
    max = -sys.maxsize
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
            idx = i
    return max, idx

arr = [1,9,4,8,5,3,8]
print(largest_ele(arr))