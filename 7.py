maxs=0
for i in range(2,10+1):
    a=(79+128+150+246)**54
    s=0
    while a>0:
        s+=a%i
        a//=i
    if s>maxs:
        maxs=s
        maxst=i
print(maxst)
