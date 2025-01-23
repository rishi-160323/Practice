# def find_divisors(n):
#     result = []
#     for i  in range(1,n):
#         if n%i==0:
#             result.append(i)
#     return result


# Optimised code.
def find_divisors(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            if i !=n//i:
                result.append(n//i)
    result.sort()
    return result

print(find_divisors(36))



# 1 x 36 = 36
# 2 x 18 = 36
# 3 x 12 = 36
# 4 x 9 = 36
# 6 x 6 = 36 ----> no need to go beyond this. So we will itrerate till n**(1/2).
# 9 x 4 = 36
# 12 x 3 = 36
# 18 x 2 = 36
# 36 x 1 = 36