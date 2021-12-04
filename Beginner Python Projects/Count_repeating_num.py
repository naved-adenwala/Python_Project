#enter multiple bumber
inp = input("Enter numbers to count the repetation of that number ")

li = list(inp)
#unique
unique = []
for l in li:
    if l not in unique:
        unique.append(l)


length = len(unique)
#counting repeating numbers
for x in range(0,length):
    find = unique[x]
    count = -1
    #checking if number is repeating or not
    for y in li:
        if y == find:
            count +=1
    if count ==1:
        print(f"{find} is repeated {count} time")
    elif count >1:
     print(f"{find} is repeated {count} times")
