#module
from textblob import TextBlob

#multiple input
inp = input("Enter words seprated by space to check spelling : ")
words = inp.split()
#variable
corrected_words = []
#convert
for word in words:
    corrected_words.append(TextBlob(word))
#input words
print("Wrong words",words) 

print("Corrected words are : ")
print("--------------------------------------------")
for i in corrected_words:
    #correct words
    print(i.correct())
