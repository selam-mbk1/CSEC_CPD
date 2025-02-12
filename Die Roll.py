import math
y,w = list(map(int,input().rstrip() .split()))
n = 7- max(y,w)
g = math.gcd(n,6)
print(f"{n//g}/{6//g}")
