# An anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once. For example fried-fired

def anagram(one,two):
    one= sorted(one)
    two= sorted(two)
    if one == two:
        print(f"it is anagram")
    else:
        print(f"It is not anagram")


anagram("silent","listen")
