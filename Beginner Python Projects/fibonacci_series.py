#fibonacci series

num = int(input("Enter a number to print fibonacci sequence : "))
a = 0
b = 1

for x in range(num):
    print(a)
    c=a+b
    a = b
    b=c