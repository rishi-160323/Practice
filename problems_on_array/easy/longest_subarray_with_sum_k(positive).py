"""contigeous part of an array, one element/entire array can also be considered as subarray.
Sunsequence is different it is non contigeous."""


"""make all posible subarrays."""
# Brute force approach.
def longest_subarray_with_sum_k(arr, k):

    n = len(arr)
    sum = 0
    length = 0
    start = 0
    end = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            if sum == k and j-i+1 > length:
                start, end = i, j
                length = j-i+1
                break
    return start, end



# arr = [1,2,3,1,1,1,1,4,2,3]
# k = 3
arr = [1, 2, 3, 7, 5, 1, 4, 3, 2, 6, 1, 1, 1]
k = 12
# print(longest_subarray_with_sum_k(arr,k))



# Better approach.
# https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/

"""Here we will keep the track of sum till every ith index and then according to the requirement from those sums we will substract the current sum
if we will be getting the desired sum after substracting the current subarray with the previous subarray and length will be also greater
then we will return the values.(Read blog)"""


"""Subtracting with the subarrays as needed."""
# this code is optimisd(best solution) if the array has positive, zeroes and negatives.
# Only better if array has positives only.
def longest_subarray_with_sum_k(arr, k):
    n = len(arr)
    sum = 0
    maxLen = 0
    start = end = -1
    preSumMap = {}

    for i in range(n):

        sum+=arr[i]
        if sum == k:
            start = 0
            end = i
            maxLen = i+1
        
        rem = sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            if length > maxLen:
                start = preSumMap[rem] + 1
                end = i
                maxLen = length

        # This condition before updating preSumMap is for edge case when zeros will be also there in the array as it can give you the wrong length of subarray.
        if sum not in preSumMap:
            preSumMap[sum]=i

    return start, end
        

# arr = [1,2,3,1,1,1,1,4,2,3]
# k = 3
arr = [1, 2, 3, 7, 5, 1, 4, 3, 2, 6, 1, 1, 1]
k = 12
# print(longest_subarray_with_sum_k(arr,k))


"""Two pointers approach."""
# Optimal solution if the array is having all the positive intgers. TC = O(2n) @ worst case and O(n) @ best case.

def longest_subarray_with_sum_k(arr, k):

    n = len(arr)
    sum=0
    right = left = 0
    length=0
    start = end = -1

    while right < n:
        sum+=arr[right]

        while sum > k and left<=right:
            sum-=arr[left]
            left+=1

        if sum == k and right-left+1 > length:
            start = left
            end = right
            length = end-start+1
                
        right+=1

    return start, end



arr = [1, 2, 3, 7, 5, 1, 4, 3, 2, 6, 1, 1, 1]
k = 12
print(longest_subarray_with_sum_k(arr,k))