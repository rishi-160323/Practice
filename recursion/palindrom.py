"""A string on reversal reads the same."""

# def check_palindrom(input, s=0, e=0):
#     if e == 0:
#         e = len(input)-1
#     if s == e:
#         print("String is palindrom.")
#         return
    
#     if input[s] == input[e]:
#         check_palindrom(input, s+1, e-1)
#     else:
#         print("String is not palindrom")
#         return
    
# check_palindrom("abcba")




def check_palindrom(input, i=0):
    if i==len(input)//2:
        print("String is palindrom.")
        return
    
    e = len(input)-1-i
    
    if input[i] == input[e]:
        check_palindrom(input, i+1)
    else:
        print("String is not palindrom")
        return
    
check_palindrom("ylooly")