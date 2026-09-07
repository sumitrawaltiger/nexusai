s={2**i for i in range(1,6)}
print(s)
l=[10,10,20,30,10,20,30]
s=set(l)
print(s)
l1=list(s)
print(l1)
l=[10,20,30,40,50,50]
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)