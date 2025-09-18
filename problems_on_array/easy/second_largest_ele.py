"""Here we can't find it by sorting if there is duplicate elements in the array."""

import sys

def second_large(arr):
    first_large = -sys.maxsize
    second_large = -sys.maxsize
    for i in range(len(arr)):
        if arr[i]>second_large:
            second_large=arr[i]
            if arr[i]>first_large:
                second_large=first_large
                first_large=arr[i]
    return second_large

arr = [1,9,4,8,5,3,8]
print(second_large(arr))




# def second_small(arr):
#     first_small = sys.maxsize
#     second_small = sys.maxsize
#     for i in range(len(arr)):
#         if arr[i]<second_small:
#             second_small=arr[i]
#             if arr[i]<first_small:
#                 second_small=first_small
#                 first_small=arr[i]
#     return second_small


# arr = [1,9,4,8,5,0,3,8]
# print(second_small(arr))


# def second_ele(arr):
#     first_large = -sys.maxsize
#     second_large = -sys.maxsize

#     first_small = sys.maxsize
#     second_small = sys.maxsize

#     for i in range(len(arr)):

#         if arr[i]<second_small:
#             second_small=arr[i]
#             if arr[i]<first_small:
#                 second_small=first_small
#                 first_small=arr[i]

#         if arr[i]>second_large:
#             second_large=arr[i]
#             if arr[i]>first_large:
#                 second_large=first_large
#                 first_large=arr[i]
#     return second_large, second_small

# arr = [1,9,4,8,5,3,8]
# print(second_ele(arr))