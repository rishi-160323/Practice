"""Without using dictionary. (a-z)=(97-122)"""

def frequency(input):
    arr_size = ord('z')-(ord('a')-1) # -1 as we will have to take 1 step before to get the correct calculation for '26' char.
    arr = [0]*arr_size
    
    for i in input:
        if i != " ":
            index = ord(i)-ord('a')
            arr[index]+=1
    
    for i in range(len(arr)):
        if arr[i] != 0:
            print(f"{chr(i+ord('a'))} repeated {arr[i]} times.")


frequency("hello world") # We strictly say that all the characters are lowercase. 
# if is anyone from ascii table then the array size will be 256.