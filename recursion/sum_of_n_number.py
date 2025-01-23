def sum_till_n(n):
    if n == 0:
        return 0
    return n + sum_till_n(n-1)


print(sum_till_n(8))


# def sum_till_n(n, sum = 0):
#     if n == 0:
#         print(sum)
#         return
#     sum_till_n(n-1, sum+n)

# sum_till_n(0)