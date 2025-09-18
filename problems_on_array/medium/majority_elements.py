"""Number of majority element should be >n/2."""


# Brute force Approach
"""Go to individual elements of the array and search for its total number of occurance."""




# Better Approach.
# TC=O(n), TC=O(n)
"""Use mapping."""
def majority(arr):
    count = {}
    for i in range(len(arr)):
        if arr[i] not in count:
            count[arr[i]]=1
        else:
            count[arr[i]]+=1
    
    for i in count:
        if count[i] > (len(arr)/2):
            return i
    return None

arr = [1, 1, 2, 1, 3, 5, 1]
print(majority(arr))





# Optimal Solution
""" Moore's Voting Algorithm"""

"""Remember one thing that Moore's voting algo is just to find the majority finding cases most of tha places it gets failed
so apply it everywhere and read about the limitations of this algo.(Hint: As you can see here only three unique elemenst in the array.)"""

def majorityElement(arr):
    # Size of the given array
    n = len(arr)
    cnt = 0  # Count
    el = None  # Element

    # Applying the algorithm
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    # Checking if the stored element is the majority element
    cnt1 = 0
    for i in range(n):
        if arr[i] == el:
            cnt1 += 1

    if cnt1 > (n / 2):
        return el
    return -1


arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)



# https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/
