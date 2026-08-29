s='Learning Python is very difficult'
s1=s.replace('difficult','easy')
print(s1)
print('The no of spaces is ',s.count(' '))
print('The no of spaces is ',len(s)-len(s1))
s='ABABABA'
print('B4 replacement ',id(s))
s1=s.replace('A','B')
print('After replacement',id(s))
print(s)
print(s1)