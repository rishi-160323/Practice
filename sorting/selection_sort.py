"""select the minimum and swap them, and this should keep going on utill the array is sorted where one pointer will always be moving
towards the unsorted portion of array."""

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = arr[i]
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j]<min:
                min=arr[j]
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]



arr = [13,46,24,52,20,9]
selection_sort(arr)
print(arr)


"""If outer loop runs for n times and for every iteration inner loop goes like n-1, n-2, n-3....2, 1 and when we will sum up all
so the time comlexity will be almost n(n+1)/2 which is equivalent to O(n^2), which is best, avg and wosrt Time complexity for this code."""

# https://takeuforward.org/sorting/selection-sort-algorithm/