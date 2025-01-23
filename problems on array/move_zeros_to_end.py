"""Idea is of two pointers which will run left to right."""

def move_zero(arr):
    j=0
    i=0
    while i < len(arr):
        if arr[i]!=0:
            arr[j], arr[i] = arr[i], arr[j]
            j+=1
        i+=1



arr = [0,1,0,0,2,4,6,0,6,0,1,7]
move_zero(arr)
print(arr)

"""TC = O(n) and SC = O(1)"""