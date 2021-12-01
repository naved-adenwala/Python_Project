

#Question & answer using dictionary
dictio = {"How many hours are there in a day?":"24","Which is the largest continent?":"Asia",
                    "Who founded Facebook?":"Mark Zuckerberg","Which is the longest river on Earth?":"Nile",
                    "Who was the first woman Prime Minister of India?":"Indira Gandhi",
                    "What is the National Animal of India?":"Tiger"}

same = True

#typecasting to list
question = list(dictio.keys())

#counting question number
question_count = 1
attempt = 1

#User have to guess in 3 attempt
while attempt <=3:
    # exception handling
    if len(question) == 0:
        print("Thank You !!! You have Guessed all the Questions")
        break

    # Question will be same if it is True
    if same == True:
        print(f"{question_count}.{question[0]}")
    #Taking User input and converting to title case
    guess = input("Enter Your Answer ").title()

    #it will exicute if user have guessed right answer
    if guess == dictio[question[0]]:
        same = True
        question.pop(0)
        print("Correct Answer (:")
        print(f"You have Guessed the answer in {attempt} attempt")
        question_count += 1  # for question number
    # if user have enter wrong input
    else:
        same = False
        print(f"Wrong Answer,Try Again {3 - attempt} attempts left ")
        attempt += 1




