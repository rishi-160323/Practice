# # Print n times
# count = 0
# def print_n_times(n):
#     global count
#     if count == n:
#         return
#     print("Hello")
#     count += 1
#     print_n_times(n)

# print_n_times(2)



# # Without any global variable
# def print_n_times(n, count = 1):
#     if count > n:
#         return
#     print("Hello")
#     count += 1
#     print_n_times(n, count)

# print_n_times(5)


# # print till n
# def print_till_n(n, count = 0):
#     if count==n:
#         return
#     count += 1
#     print(count)
#     print_till_n(n, count)

# print_till_n(6)



# # Reverse n to 1
# def print_n_to_1(n):
#     if n == 0:
#         return
#     print(n)  # Remeber here you are changing the input itself which is not a good practice so you should go with two parameter function.
#     print_n_to_1(n-1)

# print_n_to_1(5)


"""Using backtracking""" 
# for general understanding we are doing something after calling the fucnction 
# so when all the function will be returning all that remaining code will be executed that we have written after calling the functions.

# # from 1 to n
# def print_till_n(n):
#     if n == 0:
#         return
#     print_till_n(n-1)
#     print(n)

# print_till_n(4)



# # from 1 to n using backtracking.
# def print_1_to_n(n, count = 0):
#     if count == n:
#         return
    
#     print_1_to_n(n, count+1)
#     print(n-count)

# print_1_to_n(5)


# from n to 1 using backtracking.
def print_till_1(n, count = 0):
    if count == n:
        return
    print_till_1(n, count+1)
    print(count+1)

print_till_1(4)


"""Here the time complexity for every code is O(n) and same for the space complexity also
All function call gets stored in the stack space untill they return something."""