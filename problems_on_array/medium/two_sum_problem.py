# Brute force approach.
def sum_of_two(arr, k):
    n = len(arr)
    i = 0
    
    while i < n:
        j = i+1
        while j < n:
            if arr[i] + arr[j] == k:
                return i, j
            j+=1
        i+=1
    return -1, -1


arr = [2,6,5,8,11]
k = 14
# print(sum_of_two(arr, k))




# Better Approach.
"""just storing the remainder in the hashMap and finding if the same element is present in the array or not to complete the sum."""
def sum_of_two(arr, k):
    n = len(arr)
    i = 0
    hashMap = {}

    while i < n:
        if arr[i] in hashMap:
            return hashMap[arr[i]], i

        rem = k-arr[i]
        if rem not in hashMap:
            hashMap[rem]=i
        i+=1
    return -1, -1




arr = [2,6,5,8,11]
k = 14
# print(sum_of_two(arr, k))



# Optimal Solution
"""The only problem with this solution is that it can't return the original inidices of the array as the array will be modified
and we can go in way where we can store all the elements in other data structure with their indices but again that will increase
the complexity of the code and the solution will not be in optimal way. So here we will just return thst whether pairs exist or not."""
def sum_of_two(arr, k):
    left = 0
    right = len(arr)-1

    arr.sort()

    while left<right:
        if arr[left]+arr[right]<k:
            left+=1
        elif arr[left]+arr[right]>k:
            right-=1
        else:
            return True
    return False


arr = [2,6,5,8,11]
k = 14
print(sum_of_two(arr, k))