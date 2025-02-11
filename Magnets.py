n = int(input())
v =0
p = ''
for i in range(n):
    m = input()
    if m != p:
        v += 1
        p = m
    
print(v)
