num = int(input("Enter any number number to find factorial ? "))

def fact(num):
    f = 1
    for i in range(num):
        f = f * (i+1)#we are adding one because range is exclusive
    print(f"The factorial of {num} is {f}")
    return f

fact(num)