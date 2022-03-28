# Text Wrap

import textwrap

def wrap(string, max_width):
    string_wrap = textwrap.wrap(string, max_width)
    string_fill = textwrap.fill(string, max_width)
    return string_fill

'''
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
'''