age=int(input("Enter your age"))

if age>=18:
    print("You are eligible for driving")
elif age<0:
    print("Invalid age")
else:
    print("You are not eligible")
marks = int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Needs Improvement")

age=25
has_id = True
if age>=18:
    if has_id:
        print("You are eligible for driving")
    else:
        print("You have a valid age but no ID")
else:
    print("You are not eligible for driving")