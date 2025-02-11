n = int(input())
l = 0
for i in range(n):
    c,v,m = list(map(int,input().rstrip() .split()))
    if c+v+m >= 2:
        l += 1
    else:
        continue
print(l)
