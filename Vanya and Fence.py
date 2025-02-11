x,n=list(map(int,input().rstrip().split()))
c= list(map(int,input().rstrip() .split()))
k = 0
for i in range(x):
    if c[i] <= n:
        k +=1
    else:
        k +=2
print(k)
