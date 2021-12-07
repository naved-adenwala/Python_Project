from textblob import TextBlob

from textblob import TextBlob

inp = input("Enter words seprated by space to check spelling : ")
words = inp.split()

corrected_words = []

for word in words:
    corrected_words.append(TextBlob(word))

print("Wrong words",words)

print("Corrected words are : ")
print("--------------------------------------------")
for i in corrected_words:
    print(i.correct())