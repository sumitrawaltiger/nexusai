l=[1,1,1,1,2,2,2,3,3,3]
print("Before removal",l)
x=int(input("Enter element to remove"))
while True:
    if x in l:
        l.remove(x)
    else:
        break
print("After removal",l)