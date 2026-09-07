word=input("Enter any word to search for vowels: ")
s=set(word)
v={'a','e','i','o','u'}
result=s&v
print(result)