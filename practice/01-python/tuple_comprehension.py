from collections.abc import Hashable

# l=(x*x for x in range(1,6))
# print(tuple(l))
# print(type(l))
# s={10,20,30,40,50}
# s.add(5)
# print(s)
l=[10,20,30]
t=(10,20,30)
print(isinstance(l,Hashable))
print(isinstance(t,Hashable))
print(hash(t))
s={10,20}
l=[10,20,30]
t=(10,20,30)
s.add(t)
print(s)
d={}
l=[10,20,30]
t=(10,20,30)
d[t]='A'
print(d)