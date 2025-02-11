matrix = []
for  i in range (5):
        matrix.append(input() .split())
row,column = (0 , 0)


for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':
            row = i
            column = j
r = abs(2-row) + abs(2-column)
print(r)
