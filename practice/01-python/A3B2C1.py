s='ABAABBCA'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
output=""
for k,v in sorted(d.items()):
    output=output+k+str(v)
print(output)