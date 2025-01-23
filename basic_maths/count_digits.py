# def count(n):
#     count=0
#     while n>0:
#         n = n//10
#         count+=1
#     return count

# print(count(7789))


from math import log10

def count_digits(n):
    return int(log10(n)) + 1

print(count_digits(7789))



"""Because here in both approaches divison is taking place by 10 so the time complexity would be O(log10(n))
if it was by 5 so O(log5(n)), if it was by 2 so O(log2(n)) and so on...


Always remeber when the number of iterations depends upon division then the time complexity will be always in the
term of log(logrithmic).
"""