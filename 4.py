a=6**35+9**8-4**14+1
s=0
while a>0:
    s+=a%4
    a//=4
print(s)
