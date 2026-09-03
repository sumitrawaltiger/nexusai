s='ABAABBCA'
output=''
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    output= output +k + str(v)
print(output)