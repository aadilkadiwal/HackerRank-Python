# Nested Lists

l = list()
scores = set()
second_lowest_name = list()

for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
    scores.add(score)

second_lowest = sorted(scores)[1]

for name,score in l:
    if score == second_lowest:
        second_lowest_name.append(name)
        
for name in sorted(second_lowest_name):
    print(name)