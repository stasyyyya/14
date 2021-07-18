a=4**3012+2**2144-15
k1=0
while a>0:
    if a%2==1:
        k1+=1
    a//=2
print(k1)
