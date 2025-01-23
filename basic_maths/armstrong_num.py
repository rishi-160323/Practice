def armstrong_num(n):
    temp = n
    sum = 0
    while temp > 0:
        last_digit = temp%10
        sum = sum+(last_digit)**3
        temp=temp//10
    print(sum)
    return True if sum == n else False

print(armstrong_num(371))

"""An Armstrong number is a positive integer that is equal to the sum of its digits, each raised to the power of the number of digits"""

