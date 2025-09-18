
"""We can do it by five methods first by linear search for each element from one to n second by hashing creating the n+1 size
of array initialized with zeroes. Third and fourth one is explained below"""

"""Just substarct the sum of all the elements of array with the sum of n natural numbers that is (n(n+1))//2."""

"""We can use XOR here as XOR returns if the numbers are same or if even in count of same number otherwise it gives the number
itself if doesn't follow the previous rules."""

# # for sorted array.
# def find_missing_number(arr):
#     count = 1
#     for i in arr:
#         if i^count != 0:
#             return count
#         count+=1

# arr = [1,2,4,5]
# print(find_missing_number(arr))


# for unsorted arr.
def find_missing_number(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all numbers in the array
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr  # Missing number

# Example
arr = [3, 7, 1, 2, 8, 4, 5]  # Missing 6
print(find_missing_number(arr))  # Output: 6



"""Just remember one thing that in XOR
        0^0=0
        1^1=0
        1^0=1
        0^1=1

        put this opeartion b/w two number's binary representation to get the result.
        
        """
