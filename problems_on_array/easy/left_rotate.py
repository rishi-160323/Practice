def left_rotate(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[i]=temp


arr = [1,2,3,4,5,6,7]
left_rotate(arr)
print(arr)


"""TC = O(n), SC = O(1) (as an extra space) but actual SC would be O(n) as we are using 'arr' of size 'n'."""