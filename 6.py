k1=0
for i in range(17,350+1):
    a=i
    while a>0:
        if a%4==1:
            k1+=1
        a//=4
print(k1)
