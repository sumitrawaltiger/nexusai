# fruits=["APPLE","BANANA","MANGO","KIWI"]
#
# print(fruits[0],"->",fruits[1],"->",fruits[2],"->",fruits[3])
#
# for member in fruits:
#     print(f"{member} -> {fruits[fruits.index(member) + 1] if fruits.index(member) < len(fruits) - 1 else 'END'}")

# student={
#     "name": "Rahul",
#     "age": 21,
#     "city": "Delhi"
# }
#
# for i in student.items():
#     key,value=i
#     print(f"{key} >> {value}")
#
#     #name >> Rahul
#
# #range
# for i in range(1,10,3):
#     print(i)

#while
# num=100
# while num>=90:
#     print(f"I will continue {num}")
#     num-=1
# print(f"While loop ended. Latest value of num is {num}")
#
# while True:
#     user_input=input("Ask Vikas for his -> {profession/fav-movie/city/age}").strip().lower()
#
#     if user_input == "profession":
#         print("Vikas is a Software Engineer")
#     elif user_input == "fav-movie":
#         print("Vikas's favorite movie is Inception")
#     elif user_input == "city":
#         print("Vikas lives in Bangalore")
#     elif user_input == "age":
#         print("Vikas is 25 years old")
#     else:
#         print("Invalid input. Please ask about profession, favorite movie, city, or age.")
#         break

# for number in range(1,11):
#     if number  == 5:
#         continue
#     else:
#         print(number)
# def greet(user_name=None, age=None, city=None,my_org="Publicis Sapient"):
#     if user_name is None:
#         user_name = input("Please enter your name => ")
#     if age is None:
#         age = input("Please enter your age => ")
#     if city is None:
#         city = input("Please enter your city => ")
#
#     print(f"Hello everyone, my name is {user_name}. I am {age} years old and I live in {city}. I work at {my_org}.")
#
# greet(user_name="Sumit", age=30, city="Thailand")
# greet(user_name="Goutam", age=45, city="Bangkok")
# greet(user_name="Tiger", age=45, city="Alive")

# def greet(your_list):
#     for i in your_list:
#         print(i,end=" ")
# greet([10,20,30,40,50])

# def factorial(number):
#     if number ==0:
#         return 1
#     return number* factorial(number-1)
#
# num = int(input("Enter the number"))
#
# print(f"The factorial of {num} is {factorial(num)}")

#lambda
# square = lambda a: a * a
# print(square(5))
#
# myadd=  lambda num1,num2: num1 + num2
# print(myadd(10,20))
# student=[
#     {
#         "name":"Rahul",
#         "marks": 18,
#     },
#     {
#         "name":"Priya",
#         "marks": 20
#     },
#     {
#         "name":"Amit",
#         "marks": 30
#      }
#      ]
# sorted_student=sorted(student,key=lambda x:x["name"],reverse=True)
# print(sorted_student)
# print(student)

fruits=["apple","banana","mango","kiwi","tomato"]
for i,val in enumerate(fruits,start=0):
    if i % 2 == 0:
        print(f"{i} , {val}")
