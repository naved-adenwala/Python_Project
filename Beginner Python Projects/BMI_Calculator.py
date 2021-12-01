#user input
height = float(input("Enter Your Height\n"))
Weight = float(input("Enter Your Weight\n"))
#formula
height = height /100
BMI = Weight / (height * height)
#BMI
print("Your body mass index is : ",round(BMI,2))

#conditions
if BMI > 0:
    if BMI <=16:
        print("you are severely underweight")
    elif BMI <=18.5:
        print("You are underweight")

    elif BMI <=25:
        print("you are healthy")

    elif BMI <=30:
        print("you are overweight")

    else:
        print("you are severely overweight")

else:
    print("Enter valid details")
