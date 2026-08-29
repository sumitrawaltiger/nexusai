s="ABCABACABC"
i=s.find("ABC",3,9)
print(i)
i=s.find("ABC",6,10)
print(i)
subs=input("Enter substring to search")
i=s.find(subs)
if i ==-1:
    print("Substring not found")
c=0
while i!=-1:
    c+=1
    print('{} present at index:{}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))

print('The number of occurrences',c)