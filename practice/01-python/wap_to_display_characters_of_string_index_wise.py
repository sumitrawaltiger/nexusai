s=input("Enter some string")
i=0
for x in s:
    print("The character present at positive index :{} and at negativve index {} is {}".format(i,i-len(s),x))
    i+=1