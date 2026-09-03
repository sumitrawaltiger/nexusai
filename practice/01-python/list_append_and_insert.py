l=[]
l.append(10)
print(l)
l.append(20)
print(l)
l.append(30)
print(l)
l=[]
for x in range(1,101):
    if x%10==0:
        l.append(x)
print(l)
print(l.insert(3,10))
print(l)
l=[10,20,30,40]
l.insert(100,777)
l.insert(-100,9999)
print(l)