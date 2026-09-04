l1=[10,20,30,40]
l2=l1
l1[1]=7777
print(l2)
print(l1)
print(id(l1),id(l2))
print(l1 is l2)
l1=[10,20,30,40]
l2=l1[::]
print(id(l1),id(l2),l1 is l2)
l1[1]=7777
print(l1)
print(l2)
l2=l1.copy()
print(l2)