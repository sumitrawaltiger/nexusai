s="AAABBBCDDDDDDEEEFFF"
output=''
for ch in s:
    if ch not in output:
        output += ch
print(output)

l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print(''.join(l))

s1=set(s)
output="".join(s1)
