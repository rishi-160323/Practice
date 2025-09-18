# We will have to find the element whose occurance is one and other elements has occurance two.
"""We can do with so many options using linear search, hashing, mapping and XOR operator(as rest of the elements are repeated twice)."""

def find_element(arr):
    ele = 0
    for i in range(len(arr)):
        ele^=arr[i]
    return ele


arr = [1,1,2,3,3,4,4]
print(find_element(arr))