"""Push the maximum to the last by adjacent swap."""

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [13,46,24,52,20,9]
bubble_sort(arr)
print(arr)

"""If outer loop runs for n times and for every iteration inner loop goes like n-1, n-2, n-3....2, 1 and when we will sum up all
so the time comlexity will be almost n(n+1)/2 which is equivalent to O(n^2), which is avg and wosrt Time complexity for this code."""



"""Optimized code."""
# # If all the elements were sorted already.(best case with optimized code.)
# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         did_swap = 0
#         for j in range(len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 did_swap = 1
#         if did_swap == 0: # if no swap happend means the array is already sorted so need to run all the loop.
#             print("Great it was alraedy sorted") # Just to capture the result.
#             break


# # arr = [13,46,24,52,20,9]
# arr = [9, 13, 20, 24, 46, 52]
# bubble_sort(arr)
# # print(arr)

"""The time complexity of this optimized code when the case is best, will be O(n)"""