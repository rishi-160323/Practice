# def frequency(arr):
#     counter = {}
#     for i in arr:
#         if i not in counter.keys():
#             counter[i]=1
#         else:
#             counter[i]+=1
#     return counter

# arr = [1,2,1,3,2,5]
# print(frequency(arr))



def frequency(arr1, arr2):
    result = {}
    for i in arr1:
        result[i]=0

    for i in arr2:
        result[i]+=1

    return result

arr1 = [1,2,3,4,5,6,7,8,9,10,11,12] #Numbers to find.
arr2 = [1,2,1,3,2,5]
print(frequency(arr1, arr2))