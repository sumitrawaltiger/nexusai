l=[10,20,30]
print(len(l))
l=[]
l.append(10)
print(sorted(l))
l=[10,20,30,40,50,60,60]
print(l.count(60))
print(l.count(70))
print(l.index(60))
print(l.index(60, 1))
l=[1,2,1,2,3,4]
print(l.index(1))
print(l.index(2))

l=[1,2,2,2,3,3]
x=int(input("Enter element to find:"))
if x in l:
    print(f"{x} is in the list at index {l.index(x)}")
else:
    print(f"{x} is not in the list")