from itertools import permutations
data = [1,2,3,4]
for per in permutations(data):
    print(per)

#--------------------------------------------------------------------
def get_permutations(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in get_permutations(rest):
            result.append([arr[i]] + p)
    return result

data = [1, 2, 3]
for p in get_permutations(data):
    print(p)