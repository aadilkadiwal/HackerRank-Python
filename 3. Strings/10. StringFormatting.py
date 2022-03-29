# String Formatting

def print_formatted(number):
    width = len(str(bin(number))[2:])
    for i in range(1, number+1):
        decimal = str(i).rjust(width)
        octal = str(oct(i))[2:].rjust(width)
        hexadecimal = str(hex(i)).upper()[2:].rjust(width)
        binary = str(bin(i))[2:].rjust(width)
        
        print('{} {} {} {}'.format(decimal, octal, hexadecimal, binary))
'''
n = int(input())
print_formatted(n)
'''