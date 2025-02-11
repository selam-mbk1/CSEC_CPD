n = int (input())
st = input()
a = 0
for i in st:
    if i =='A':
        a += 1
d = n-a
if a > d:
    p = "Anton"
elif a<d:
    p = "Danik"
else:
    p = "Friendship"
print(p)
