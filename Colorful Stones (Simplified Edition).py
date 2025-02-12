s = input()
t = input()
p = 0
for i in range(len(t)):
    if t[i] == s[p]:
        p= p + 1
print(p+1)

