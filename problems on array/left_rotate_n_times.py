def left_rotate(arr, d):
    n = len(arr)

    d = d % n  # Sometimes value of 'd' can be more than 'n'.

    # temp = arr[:d]ss
    temp = [0]*d
    for i in range(d): # O(d)
        temp[i]=arr[i]

    for i in range(d, n): # O(n-d)
        arr[i-d]=arr[i]
        
    for i in range(n-d, n): # range(9-3, 9)-->(6, 9) ## O(d)
        arr[i]=temp[i+d-n]


arr = [1,2,3,4,5,6,7,8,9,10,11]
# arr = [1, 2, 3, 4, 5]
# d = 4  # Rotate by 4
left_rotate(arr, 4)
print(arr)

"""TC of this algo is O(n+d) you can see the comments with the code and extra sapce taken 'd' so the SC will be O(d)"""





# # Optimal Solution (For SC becase we will not use an extra array but TC will be O(2n) from O(n+d).

# # """
# # Algorithm:
# # ----------
# # reverse(0, d)
# # reverse(d, n)
# # reverse(0,n)
# # """

# def reverse(arr, start, end):
#     # n = (start+end)//2
#     # j = end-1
#     # for i in range(start, n):
#     #     arr[i], arr[j] = arr[j], arr[i]
#     #     j-=1
#     while start<end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start+=1
#         end-=1

# def left_rotate(arr, d):
#     n = len(arr)
#     d = d % n

#     reverse(arr, 0, d-1)
#     reverse(arr, d, n-1)
#     reverse(arr, 0, n-1)

# def right_rotate(arr, d):
#     n=len(arr)
#     left_rotate(arr, n-d)



# arr = [1,2,3,4,5,6,7,8,9,10]
# # left_rotate(arr, 14)
# # print(arr)
# right_rotate(arr, 4)
# print(arr)

