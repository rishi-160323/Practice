def frequency(input):
    result = {}
    for i in input:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    return result


print(frequency("Hello World"))