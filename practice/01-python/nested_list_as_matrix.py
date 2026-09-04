l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print("Elements row wise")
for x in l:
    print(x)

print("Elements in matrix style")
for x in l:
    for y in x:
        print(y,end=" ")
    print()