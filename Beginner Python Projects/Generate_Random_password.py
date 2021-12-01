#Module
import random
try:
    #Input
    user = int(input("Enter the length to create random password "))
    if user < 30:
        probability = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        # according to the user input it will
        password = random.sample(probability,k=user)
        pasgenerator = "".join(password)
        print(f"The random password is '{pasgenerator}'")
#Exception Handling
except ValueError as v:
    print("Error Length shoud be less than '30' and should be a 'numeric' value")