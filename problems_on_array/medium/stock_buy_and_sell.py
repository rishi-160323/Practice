"""Gain maximum profit and remember you can only sell stock on after buying day."""

# Brute force approach
def stock_buy_sell(arr):
    maxPro = 0
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
                maxPro = max(arr[j]-arr[i], maxPro)
    return maxPro

arr = [7, 1, 5, 3, 6, 4]
print(stock_buy_sell(arr))


# Optimal solution.
def stock_buy_sell(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro


arr = [7, 1, 5, 3, 6, 4]
print(stock_buy_sell(arr))
