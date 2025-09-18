"""We can use set here, and after that we wil have to sort that. Union include unique elements."""

# def union_sorted_arrays(arr1, arr2):
#     result = sorted(set(arr1).union(set(arr2)))
#     return result

# # Example usage
# arr1 = [1, 2, 4, 5]
# arr2 = [2, 3, 5, 6]
# print(union_sorted_arrays(arr1, arr2))


# Optimal solution.

def union_sorted_arrays(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i]<arr2[j]:
            if len(result) == 0 or arr1[i] != result[-1]:
                result.append(arr1[i])
                result[-1]=arr1[i]
                i+=1
            else:
                i+=1    
        else:
            if len(result) == 0 or arr2[j] != result[-1]:
                result.append(arr2[j])
                result[-1]=arr2[j]
                j+=1
            else:
                j+=1

    # In the following line we are not comparing whether the element is bigger or not as the arrays are in sorted order.
    while i < len(arr1):
        if len(result) == 0 or arr1[i] != result[-1]:
            result.append(arr1[i])
            result[-1]=arr1[i]
            i+=1
        else:
            i+=1
    
    while j < len(arr2):
        if len(result) == 0 or arr2[j] != result[-1]:
            result.append(arr2[j])
            result[-1]=arr2[j]
            j+=1
        else:
            j+=1

    return result

arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
print(union_sorted_arrays(arr1, arr2))


"""
1. Track the 'last element' in the final array to avoide duplicate elements.
2. len(arr) == 0 condition should be written first while checking for duplicate.
3. Be careful with the space intension while implementing the last two while loops.
4. This code was implemented for sorted arrays.
5. carefully observe the main first while loop.
"""