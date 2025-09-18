def maximum_consecutive_onse(arr):
    count = 0
    max_count = 0
    for i in range(len(arr)):
        if arr[i]!=1:
            if count>max_count:
                max_count=count
                count=0
        else:
            count+=1
        
    return max_count if max_count>count else count

arr = [1,1,0,1,1,1,0,1,1,1,1,1]
print(maximum_consecutive_onse(arr))
