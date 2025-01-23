"""We can use set here, and after that we wil have to sort that. Union include unique elements."""

def union_sorted_arrays(arr1, arr2):
    result = sorted(set(arr1).union(set(arr2)))
    return result

# Example usage
arr1 = [1, 2, 4, 5]
arr2 = [2, 3, 5, 6]
print(union_sorted_arrays(arr1, arr2))