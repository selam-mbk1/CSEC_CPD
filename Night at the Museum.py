z = input()
le ="abcdefghijklmnopqrstuvwxyz"
n = len(z)
pointer = "a"
count = 0
for i in range(n):
    if z[i] == pointer:
        count = count
    else:
        distance = abs(le.index(pointer)-le.index(z[i]))
        if distance <= 13:
            count = count + distance
            pointer = z[i]
        else:
            distance = 26 - distance
            count = count + distance
            pointer = z[i]
print(count)
