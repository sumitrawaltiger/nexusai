l1=[10,20,30,40]
l2=[30,40,50,60]
l3=[i for i in l1 if i  in l2]
print(l3)
l=['Baliah','Nag','Venki','Chiru']
l1=[x[0] for x in l]
print(l1)
l="The quick brown fox jumps over lazy dog"
s=l.split()
print(s)
len=[[x.upper(), len(x)] for x in s]
print(len)