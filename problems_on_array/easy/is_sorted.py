"""When the array might be in ascending order."""

def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr = [1,7,9,9,12,13]
print(is_sorted(arr))