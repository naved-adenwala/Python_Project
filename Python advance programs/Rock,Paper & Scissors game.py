import random


#User name
name = input("Enter your name ").capitalize()
print(f"Welcome {name} !!!")

# points
computer_point = 0
player_point = 0

#loop
while True:
    game = ["Rock","Paper","Scissors"]
    computer = random.choice(game)
    choice = input("Enter Rock | Paper | Scissors 'Press Enter To Quit' ").capitalize()

    if choice == "Rock" or "Paper" or "Scissors":
        #tie if both have same value
        if choice == computer:
            print("Computer Choice : ", computer)
            print("-------------------------Tie--------------------------")

        #comparing if user select rock
        elif choice == "Rock":
            print("Computer Choice : ", computer)
            #computer will get point if user entered rock
            if computer == "Paper":
                computer_point +=1
                print("Computer Gets Point")
                print("--------------------------------------------------------------")
                print(f"Scores :\n{name}: {player_point}\nComputer : {computer_point}")
                print("--------------------------------------------------------------")
            else:
                #else user will get point
                player_point +=1
                print(f"{name} Gets Point")
                print(f"Scores :\n{name}: {player_point}\nComputer : {computer_point}")

        #comparing with paper
        elif choice == "Paper":
            print("Computer Choice : ", computer)
            if computer == "Scissors":
                computer_point +=1
                print("Computer Gets Point")
                print(f"Scores :\n{name}: {player_point}\nComputer : {computer_point}")
            else:
                player_point +=1
                print(f"{name} Gets Point")
                print(f"Scores :\n{name}: {player_point}\nComputer : {computer_point}")

        #Comparing with scissors
        elif choice == "Scissors":
            if computer == "Rock":
                print("Computer Choice : ", computer)
                computer_point +=1
                print("Computer Gets Point")
                print(f"Scores :\n{name}: {player_point}\nComputer : {computer_point}")
            else:
                player_point +=1
                print(f"{name} Gets Point")
                print(f"Scores :\n{name}: {player_point}\nComputer : {computer_point}")

        if choice == "":
            print(f"Thank you!!,Come back soon!!")
            break

        elif choice not in game:
            print("Wrong Input!!!")





if player_point == computer_point:
    print("Tie")
elif player_point > computer_point:
    print(f"{name} Wins by {player_point-computer_point} points")
else:
    print(f"Computer Wins by {computer_point-player_point} points")

