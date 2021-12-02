import random
import time


name = input("Enter Your name ").capitalize()
print(f"Welcome To hanggame {name}")
time.sleep(2)
print("Starting...")
time.sleep(2)
wrong_guesses = 0

def hangmangame(wrong_guesses):
    #random words
    ran = random.choice(["NICE","BYE","WONDERFUL","JOY","SAD","ENJOY"])
    secret_word = ran
    li = list(secret_word)
    #creating blanks
    no_of_blank = "_" * len(li)
    blank = list(no_of_blank)
    temp = []
    #if number of wrong guesses is 8 then game will be over
    while wrong_guesses <= 8:

        if wrong_guesses == 8:
            print("_______________")
            print("|              |")
            print("|              0")
            print("|             \|/")
            print("|              |")
            print("|              |")
            print("|             / \  ")
            print("_______________")
            print("You are Hanged !!!!, GAME OVER!!!")
            print(f"You Lost {name},Better Luck next time")
            print("\n")
            print(f"The Secret word was \"{secret_word}\".\n")
            #asking user to play again or not
            user = input("Would you like to play this game again ? \n").lower()
            if user == "yes":
                wrong_guesses = 0
                hangmangame(wrong_guesses)
            break


        print(blank)
        print(li)
        time.sleep(1)
        guess = input("Guess the Character ? \n").upper()
        #restrictions for user
        if len(guess) > 1:
            print("Only one letter at a time is allowed")
        #checking if it is character or not
        if guess.isalpha() != True:
            print(f"'{guess.lower()}'is not a character")
        #if user repeat same guess
        if guess in blank:
            print(f"{guess} is already present !!!")

        #comparing secret word to the input word
        if guess in li:
            for i in range(len(li) ):
                if guess == li[i]:
                    blank[i] = li[i]
                    break

        #user guessed all the character
        if blank == li:
            print("Congratulatons!!! Well Played")
            user = input("Would you like to play this game again ? \n").lower()
            if user == "yes":
                wrong_guesses = 0
                hangmangame(wrong_guesses)
            else:
                print("See you again")
                break


        elif guess not in li:
            wrong_guesses +=1
            hangmanFailure(wrong_guesses, secret_word)


#hangman output setup
def hangmanFailure(wrong_guesses,secret_word):
    if wrong_guesses == 1:
        print("_______________")
        print("|              |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_______________")
        print("Failed! the rope is tied for you")

    elif wrong_guesses == 2:
        print("_______________")
        print("|              |")
        print("|              0")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_______________")
        print("Your head is hanged")

    elif wrong_guesses == 3:
        print("_______________")
        print("|              |")
        print("|              0")
        print("|              |")
        print("|              |")
        print("|              |")
        print("|")
        print("_______________")
        print("Now your body is hanged")

    elif wrong_guesses == 4:
        print("_______________")
        print("|              |")
        print("|              0")
        print("|             \|")
        print("|              |")
        print("|              |")
        print("|")
        print("_______________")
        print("Your right hand is hanged")

    elif wrong_guesses == 5:
        print("_______________")
        print("|              |")
        print("|              0")
        print("|             \|/")
        print("|              |")
        print("|              |")
        print("|")
        print("_______________")
        print("Your left hand is hanged")

    elif wrong_guesses == 6:
        print("_______________")
        print("|              |")
        print("|              0")
        print("|             \|/")
        print("|              |")
        print("|              |")
        print("|")
        print("_______________")
        print("Your left hand is hanged")

    elif wrong_guesses == 7:
        print("_______________")
        print("|              |")
        print("|              0")
        print("|             \|/")
        print("|              |")
        print("|              |")
        print("|             / ")
        print("_______________")
        print("Your Right leg is hanged")




hangmangame(wrong_guesses)


















