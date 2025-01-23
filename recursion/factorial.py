def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(6))


# # Parameterized
# def factorial(n, product = 1):
#     if n == 0:
#         print(product)
#         return
#     factorial(n-1, product*n)

# factorial(6)