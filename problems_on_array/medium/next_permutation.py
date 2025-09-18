# https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
# https://youtu.be/JDOXKqF60RQ?si=pQQd2hAVoSb7tSeR


# Brute force approach.
"""Find all permutations and guess the next one."""
# Better approach. (only for c++ beacuse there we can use STL library for getting all the possible permutations.)






# optimal approach.
from typing import List
def next_permutation(input_arr: List[int]) -> List[int]:
    n = len(input_arr)
    bp_idx = -1
    
    # find the breakpoint(itrate reverse).
    """Breakpoint --> where element i < i+1."""
    for idx in range(n-2, -1, -1): # range(start, stop, step)
        if input_arr[idx] < input_arr[idx+1]:
            bp_idx=idx
            break
    
    # # if no breakpoint means that was the last permutaions so just reverse the array and return it as it would be the next permuation(first permutaion).
    # if bp_idx == -1:
    #     ans = reversed(input_arr)
    #     return ans
        
    # after finding break point find grater element than arr[break point] (itrate reverse) and swap with arr[break point].
    """We find only grater element to swap with the breakpoint element."""
    for idx in range(n-1, bp_idx, -1):
        if input_arr[idx] > input_arr[bp_idx]:
            input_arr[idx], input_arr[bp_idx] = input_arr[bp_idx], input_arr[idx]
            break
    
    # then reverse the entire right half of array after break point.
    input_arr[bp_idx+1:] = reversed(input_arr[bp_idx+1:])
    
    return input_arr

# input_arr = [6,0,8,1]
# input_arr = [2,3,0,0,1,4,5]
input_arr = [2,3,1]
ans=next_permutation(input_arr)
print(ans)


"""Summry of this algo."""
    # find the breakpoint(itrate reversely).
    # Breakpoint --> where element i < i+1.
    # if no breakpoint means that was the last permutaions so just reverse the array and return it as it would be the next permuation(first permutaion).
    # after finding break point find grater element than arr[break point] (itrate reverse) and swap with arr[break point].
    # then reverse the entire right half of array after break point.

