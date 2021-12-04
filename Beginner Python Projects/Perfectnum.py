#perfect number
num=int(input("Enter the number: "))
sum_v=0
output = ""
for i in range(1,num):
    if (num%i==0):#if the remainder is 0 then add
        sum_v=sum_v+i
        output +=str(i)
output = str(output)
output_f ="+".join(output)
#comparing
if(sum_v==num):
    print(f"{output_f} - {num} is a perfect number",sep="")
else:
    print("The entered number is not a perfect numb")