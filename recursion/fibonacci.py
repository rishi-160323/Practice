"""0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, and so on"""


# You can see here that we are not counting the zero here in the series of fibonacci. 
def print_fibonacci(n):
    if n <= 1:
        return n
    return print_fibonacci(n-1) + print_fibonacci(n-2)

print(print_fibonacci(6))

"""As for every n there is two funtion is being called for each step that is n-1 and n-2 so the time complexity
of this code can be considered almost as O(2^n) but not exactly and the nature of the time complexity here is exponential."""