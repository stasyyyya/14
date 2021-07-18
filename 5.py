mins=1000
for i in range(3, 10+1):
    a=5**54+7**12-6**4+3
    s=0
    while a>0:
        s+=a%i
        a//=i
    if s<mins:
        mins=s
print(mins)
