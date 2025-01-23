"""Euclidean algorithmm says that
if a > b,
gcd(a,b) == gcd(a-b, b)
"""
# https://youtu.be/1xNbjMdbjug?si=3ni2hLRlU1-Ple0x

# def gcd(a, b):
#     while b:
#         a, b = b, a % b  # Replace a with b and b with a % b
#     return a

# # Example usage
# print(gcd(56, 98))  # Output: 14



# from functools import reduce

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def gcd_multiple(numbers):
#     return reduce(gcd, numbers)

# # Example usage
# print(gcd_multiple([56, 98, 42]))  # Output: 14

"""Euclidean algorithmm says that
if a > b,
gcd(a,b) == gcd(a-b, b) and we can extend this as (a%b, b) watch the video
# https://youtu.be/1xNbjMdbjug?si=3ni2hLRlU1-Ple0x
"""

def gcd(a, b):
    while a > 0 and b > 0:
        if a > b: a = a % b
        else: b = b % a
    if a == 0: return b
    return a

print(gcd(56, 98))