t=(10,10,'Durga',20,10)
t1=10,'durga',20,10
print(type(t))
print(t1)
print(type(t1))
print(t1[0])
print(t1[-1])
l=(10,20,30,40)
# l[0]=777  # This will raise an error because tuples are immutable
print(l)
t=(10,20,30,40)
t[0]=777
print(t)