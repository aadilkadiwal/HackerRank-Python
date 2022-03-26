# Find the Runner-Up Score!

n = int(input())
arr = list(map(int, input().split()))

winner = max(arr)

while max(arr) == winner:
    arr.remove(max(arr))
    
print(max(arr)) 