def panlindrom(n):
    temp = n
    result = 0
    while temp > 0:
        last_digit = temp%10
        result = result*10+last_digit
        temp=temp//10

    return True if result == n else False

print(panlindrom(1901))
