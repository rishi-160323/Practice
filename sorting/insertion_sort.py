"""Take an element and insert it in its correct order and make the portion(mostly left) of array as sorted."""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        j = i-1
        while arr[j] > ele and j >= 0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=ele # This j+1 can be so dangerous, be careful, while writing algorithm small + - can make you code totally wrong. (you will get repeative elements).


arr = [13,46,24,52,20,9]
insertion_sort(arr)
print(arr)

"""TC = O(n^2) for worst and avg case
TC = O(n) for the best case when the arrays is sorted."""

# I think this is the best option for sorting then selection sort and bubble sort as inner loop will not be running if array is already sorted.