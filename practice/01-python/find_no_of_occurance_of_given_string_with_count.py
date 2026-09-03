s=input("Enter a string: ")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)

for ch in sorted(l):
    print(f"{ch} : {s.count(ch)}")

s1='ABBBSASLDFDS'
s2=set(s1)
for ch in sorted(s2):
    print(f"{ch} occurs {s1.count(ch)} times")