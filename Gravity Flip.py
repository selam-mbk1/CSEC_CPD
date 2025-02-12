n = int(input())
c = input()
lis = list(map(int , c.split()))
lis.sort()
for i in range(n):
    print(lis[i] , end = " ")
