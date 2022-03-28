# sWAP cASE

def swap_case(s):
    new_s = ''
    for i in s:
        if i.isupper():
            new_s += i.lower()
        else:
            new_s += i.upper()
    return new_s        

'''            
s = input()
result = swap_case(s)
print(result)
'''