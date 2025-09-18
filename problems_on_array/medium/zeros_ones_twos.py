# Brute force approach
"""Count all the element and the refile them according to the count in order."""


# Better Approach.
"""Sort the array with any of the sorting algorithm"""



# Optimal Solution
"""Here we are assuming that the array b/w mid and high will be always unsorted."""
def dutch_national_flag(arr):
    low = mid = 0
    high = len(arr)-1

    while mid <= high:
        if arr[mid]==0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1


# arr = [2, 0, 2, 1, 1, 0, 2, 1, 0, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 0]
# # arr = [0, 1, 2, 0, 1, 2]
# arr = [2, 0, 2, 1, 1, 0]
# arr = [2, 2, 2, 2, 2, 2, 2]
arr = [1, 2, 0]
dutch_national_flag(arr)
print(arr)