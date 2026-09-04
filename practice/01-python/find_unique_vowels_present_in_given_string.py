
vowels=['a','e','i','o','u','A','E','I','O','U']
word=input("Enter any string to search for vowels")
result=[]
for ch in vowels:
    if ch in word:
        if ch not in result:
            result.append(ch)
print(result)
print("No of unique vowels:", len(result))
#unique_vowels=[i for i in word if i in vowels]
unique_vowels=[ch for ch in vowels if ch in word]
print(unique_vowels)