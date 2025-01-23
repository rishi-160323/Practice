# https://takeuforward.org/data-structure/merge-sort-algorithm/

"""Divide and merge."""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right =  arr[mid:]

    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i]<right_arr[j]:
            arr[k]=left_arr[i]
            k+=1
            i+=1
        else:
            arr[k]=right_arr[j]
            k+=1
            j+=1

    while i < len(left_arr):
        arr[k]=left_arr[i]
        k+=1
        i+=1
    while j < len(right_arr):
        arr[k]=right_arr[j]
        k+=1
        j+=1
    return arr


arr = [13,46,24,52,20,9]
merge_sort(arr)
print(arr)

# In the merge sort we use temporary arrays. (quick sort doesn't use temporary array.)
# The Time complexity for this will be O(nlogn). (for more info please check out the link as TC is very important.)
# Space complexity will be O(n).


"""Following code is according to c++."""

# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid

#     # Create temporary arrays
#     L = [0] * n1
#     R = [0] * n2

#     # Copy data to temporary arrays
#     for i in range(n1):
#         L[i] = arr[left + i]
#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]

#     # Merge the temporary arrays back into the original array
#     i = j = 0
#     k = left
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     # Copy remaining elements of L[], if any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

#     # Copy remaining elements of R[], if any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1


# def merge_sort(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2

#         # Recursively sort first and second halves
#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid + 1, right)

#         # Merge the sorted halves
#         merge(arr, left, mid, right)


# # Example usage
# arr = [13, 46, 24, 52, 20, 9]
# merge_sort(arr, 0, len(arr) - 1)
# print(arr)