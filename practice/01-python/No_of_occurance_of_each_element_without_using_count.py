s="Adfadsflasdfljksadflasdjfas"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(f"{k} : {v}")