# def reverse_array(arr, s=0, e=0):
#     if e==0:
#         e = len(arr)-1
#     if s == e:
#         return
#     arr[s], arr[e] = arr[e], arr[s]
#     reverse_array(arr, s+1, e-1)


# arr = [1,2,3,4,5,6,7]
# reverse_array(arr)
# print(arr)


def reverse_array(arr, i=0):
    if i == len(arr)//2:
        return
    e = len(arr)-1-i
    arr[i], arr[e] = arr[e], arr[i]
    reverse_array(arr, i+1)

arr = [1,2,3,4,5,6,7]
reverse_array(arr)
print(arr)