#module
import random
import time
while True:
    #User Input
    user = input("Enter To Roll the Dice or Enter quit to exit ").lower()
    #it will quit the game
    if user =="quit":
        print("You Quit the Game!!","Thank You")
        break
    else:
        #it will generate number
        dice = random.randint(1,6)
        print("Rolling the Dice !!!!!!!")
        #after 2 sec delay it will display
        time.sleep(2)
        print(f"Dice: {dice}")

