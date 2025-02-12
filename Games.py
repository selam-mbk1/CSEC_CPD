n = int(input())
hm = []
away = []
change = 0
for i in range(n):
    ho, aw = list(map(int, input().split()))
    hm.append(ho)
    away.append(aw)
for i in hm:
    change += away.count(i)
print(change)
