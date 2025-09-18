# https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/

# Brute force approach.
class longest_consequtive_sequence:

    def __init__(self, arr):
        # self.arr = set(arr) # removes extra check for improving time complexity.
        self.arr = arr

    def linear_search(self, num, arr):
        if len(arr) == 0:
            return False
        if num in arr:
            return True
        else:
            return False

    def main(self):
        ans = 1
        for i in range(len(self.arr)):
            next_num = self.arr[i]+1
            seq_len = 1
            while self.linear_search(next_num, self.arr):
                seq_len += 1
                next_num += 1
            ans = max(ans, seq_len)

        return ans
            


# input = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
input=[5,6,2,7,8,3,4,1,1,1,0]
solution = longest_consequtive_sequence(input)
print(solution.main())



# better solution.

"""Sorting is the key."""

def longest_consequtive_sequence_func(arr):
    arr = sorted(arr)
    count = 1
    last_ele = arr[0]
    ans = 0
    for i in range(len(arr)):
        if arr[i] == last_ele+1:
            count += 1
            last_ele = arr[i]
        elif arr[i] != last_ele:
            count = 1
            last_ele = arr[i]
        ans =  max(ans, count)
    return ans


# input = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
input=[5,6,2,7,8,3,4,1,1,1,0]
print(longest_consequtive_sequence_func(input))


# Optimal solution

"""Here the difference is that we are not sorting the given array.(Not messing with the input)"""

def longest_consequtive_sequence_func(arr):
    set_arr = set(arr)
    ans = 0
    count = 0
    for i in set_arr:
        # looking if the element is starting of the sequence.
        if i-1 not in set_arr: # <----Key✅
            count = 1
            ele = i
        while ele+1 in set_arr:
            count +=1
            ele +=1
        ans = max(ans, count)
    return ans


input = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
# input=[5,6,2,7,8,3,4,1,1,1,0]
print(longest_consequtive_sequence_func(input))    


# points to be remembered
"""
1. We need to find the element first element of the sequence if it is there then only we will proceed further
otherwise keep finding the first element of the sequence."""