# Lists

N = int(input())
L = list()

for _ in range(N):
    s = input().split(" ")
    if s[0] == 'append':
        L.append(int(s[1]))
    if s[0] == 'remove':
        L.remove(int(s[1]))
    if s[0] == 'insert':
        L.insert(int(s[1]), int(s[2]))
    if s[0] == 'sort':
        L.sort()
    if s[0] == 'pop':
        L.pop()
    if s[0] == 'reverse':
        L.reverse()
    if s[0] == 'print':
        print(L)