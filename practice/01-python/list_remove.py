l=[10,20,30,20,40]
l.remove(20)
#l.remove(50)
print(l)
l=[1,2,3,4,5,6]
print("Before removal",l)
x=int(input("Enter element to remove"))
if x in l:
    l.remove(x)
else:
    print(f"Element {x} not found in the list.")
print("After removal",l)