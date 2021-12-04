# palindrome
# A palindrome is a word, number, phrase, or
# other sequence of characters which reads the same backward as forward, such as madam or racecar.
def palindrome(self1):
    r =""
    #here I have loop each element and reversed
    for i in self1:
        r=i+r
    if self1 == r:
        print(f"{r} is palindrome")
    else:
        print(f"{r} is Not palindron")


palindrome("wow")