s=input("Enter any string")
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
output = " ".join(l1)
print(output)