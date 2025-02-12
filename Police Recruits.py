n = int(input())
m = list(map(int,input().split()))
p = 0
u = 0
for i in (m):
    if i == -1 :
        if p > 0 :
            p -= 1
        else:
            u += 1
    else :
        p += i

print(abs(u))
