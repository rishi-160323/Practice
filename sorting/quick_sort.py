"""1. Pick a pivot(first/last/medium/random element) and place it in correct its correct place in sorted array.
2. place elements smaller than pivot in the left and larger in the right."""


# Less optimized

def partition(arr, low, high):
    pivot = arr[low]  # Choose the first element as the pivot
    i = low + 1       # Index for elements greater than pivot
    j = high          # Index for elements smaller than pivot

    while True:
        # Find an element greater than or equal to the pivot from the left
        while i <= j and arr[i] <= pivot:
            i += 1

        # Find an element smaller than or equal to the pivot from the right
        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:  # If i and j have not crossed, swap them
            arr[i], arr[j] = arr[j], arr[i]
        else:  # If i and j have crossed, exit the loop
            break

    # Place the pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j  # Return the partition index


def quick_sort(arr, low, high):
    if low < high:
        # Find the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage
arr = [13, 46, 24, 52, 20, 9]
quick_sort(arr, 0, len(arr) - 1)
print(arr)



# # Optimized code.
# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low+1
#     for j in range(low+1, high+1):
#         if arr[j]<pivot:
#             arr[j], arr[i] = arr[i], arr[j]  #Crucial step
#             i+=1
#     arr[low], arr[i-1] = arr[i-1], arr[low]  #Crucial step
#     return i-1
    
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)

#         quick_sort(arr, low, pi-1)
#         quick_sort(arr, pi+1, high)

# # Example usage
# arr = [13, 46, 24, 52, 20, 9]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)