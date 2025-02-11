n = input()
low = 0
up = 0
for i in n:
    if i.islower():
        low +=1
    else:
        up +=1
if low >= up:
    print(n.lower())
else:
    print(n.upper())
        
