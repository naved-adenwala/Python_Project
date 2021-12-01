# An acronym is a word formed by abbreviating a phrase by combining certain
# letters of words in the phrase (often the first initial of each) into a single term.

# Example acronym of naved rashid adenwala is - "NRA"

#User Input
user = input("Enter to get acronyms of a sentence ")
#splitting letter
spl = user.upper().split(" ")
#taking first letter from each word
for i in spl:
    print(i[0],end="")