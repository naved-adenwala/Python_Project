#function
def fizz_buzz():
    #User Input
    inp = int(input("Enter Any Number : "))

    #If 3 and 5 is divisible by number
    if inp%3 == 0 and inp%5 == 0:
        return "Fizz_Buz"
    # If 3 is divisible by number
    elif inp%3 == 0:
        return "Fizz"
    # If 5 is divisible by number
    elif inp%5 == 0:
        return "Buzz"
    #else return userinput
    else:
        return inp
print(fizz_buzz())