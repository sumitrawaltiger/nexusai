city=input("Enter your city name").lstrip()
scity=city.strip()
if scity =='Hyderabad':
    print("Hello Hyderabadi...Aadab")
elif scity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity == "Bangalore":
    print("Hello Kannadiga...namaskara")
else:
    print("Your entered city is invalid")