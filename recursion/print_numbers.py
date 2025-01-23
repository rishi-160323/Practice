# count = 0
# def print_num(n):
#     global count
#     if count == n:
#         return
#     print(count)
#     count += 1
#     print_num(n)


# print_num(5)


count = 0  # Define global variable

def print_num():
    global count  # Declare count as global to modify it
    if count == 7:  # Base case
        return
    print(count)  # Print current value of count
    count += 1  # Increment count
    print_num()  # Recursive call with the same limit

print_num()
