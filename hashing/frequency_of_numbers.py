"""This is same as mentioned in "mapping folder" but here just we are saying that maximum number from the aar1 has already defined in the question.
we suppose that is 12. Basically here our intension is to not to use dictionary."""

def frequency(arr1):
    result = [0]*(12+1) # 12 is the maximum number in array, +1 beacsue array starts from 0.
    for i in arr1:
        result[i] +=1
    
    for i in range(len(result)):
        if result[i] != 0:
            print(f"{i} repeated {result[i]} times.")


arr1 = [1,2,1,3,2,5,12]
frequency(arr1)
# print(frequency(arr1))