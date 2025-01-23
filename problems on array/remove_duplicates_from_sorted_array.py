"""Only for SORTED array."""

def remove_duplicates(arr):
    prev = arr[0]
    for i in range(1,len(arr)):
        if arr[i]==prev:
            arr[i]=0
        else:
            prev=arr[i]
    return arr

arr = [1,7,9,9,12,13]
# arr = [1,1,2,2,2,3,3,4]
remove_duplicates(arr)
print(arr)


# # You can also do it by set.
# arr = [1,1,2,2,2,3,3,4]
# ans = set(arr)
# print(ans)



# # Keep the unique elements in the begining of the sorted array.
# def unique_first(arr):
#     i = 1
#     last_ele = arr[0]
#     for j in range(1,len(arr)):
#         if arr[j]!=last_ele:
#             last_ele = arr[j]
#             arr[i], arr[j]=arr[j], arr[i]
#             i+=1
#     # return arr
#     return arr[:i]


# arr = [1,1,2,2,2,3,3,4]
# print(unique_first(arr))
# print(arr)