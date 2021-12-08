# random module
import random
#generating random number
num = random.randrange(1,1000)
print(num)
#user input

wrong_guess = 0 #count the no of attempt
while True: #run till it is egual to guess
    guess = int(input("Guess the number: "))

    if guess > num:#guessed number is greater
        wrong_guess +=1
        print("Too High")
    elif guess < num:#guessed number is lower
        wrong_guess += 1
        print("Too Low")
    elif guess == num:
        break


print(f"you guessed it in {wrong_guess} attempt")
print("Thank You!!!")