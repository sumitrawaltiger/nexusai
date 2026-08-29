mail= input("Enter your email id")
try:
    i=mail.index("@")
    print("Mail contains @ symbol which is mandatory")
except ValueError:
    print("Mail id does not contain @symbol")