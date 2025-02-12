x = list(map(int,input() .rstrip() .split()))
if len(set(x))==1:
    print(3)
elif len(set(x))==2:
    print(2)
elif len(set(x))==3:
    print(1)
elif len(set(x))==4:
    print(0)
