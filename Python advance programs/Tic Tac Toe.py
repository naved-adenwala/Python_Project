#tic tac toe


board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
#to print board
def print_board():
    for outer in board:
        for inner in outer:
            print(f"{inner} ",end="")
        print()

#variable for checking
range_check = True
number_check = True


#let x is true and o is false
choice = True


#function for checking
def num_checking(inp):
    global range_check
    global number_check
    #checking range and number
    if inp.isdigit() == True:
        number_check = True
        con = int(inp)
        if con >=1 and  con<=9:
            range_check = True
        else:
            range_check = False#out of range then it is false

    else:
        number_check = False#is not a num then it is false

#setting rows and column
def indexing(user_inp):
    rows =int(user_inp / 3) #output will be 0,1 or 2
    col = user_inp #inp as columns
    if col > 2: col = col%3 #change col if it is greater than 2
    return (rows,col) #it will return rows and col

#adding user input
def add_to_board(indexing,board,choice):
    #tuple unpacking
    row = indexing[0]
    col = indexing[1]

    board[row][col] = choice


#checking if user already gave input
def check_input(indexing,board):
    row = indexing[0]
    col = indexing[1]

    #if it is not equal to "-" then False
    if board[row][col] != "-":
        return False
    else:
        return True

#if it is true then it is matching else not matching
def check_col(user,board):
    #column
    if board[0][0]== user and board[1][0]== user and board[2][0] == user:
        return True
    elif board[1][1]== user and board[1][1]== user and board[2][1] == user:
        return True
    elif board[0][2]== user and board[1][2]== user and board[2][2] == user:
        return True

    #diagonal
    elif board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True

    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False



#if it is true then it is matching else not matching
def check_row(user,board):
    if board[0][0]==user and board[0][1]==user and board[0][2]==user:
        return True
    elif board[1][0]==user and board[1][1]==user and board[1][2] == user:
        return True
    elif board[2][0]==user and board[2][1]==user and board[2][2] == user:
        return True
    else:
        return False


#choose x or 0
ch = input("Enter 'x' or 'o' before the game start ").lower()

#it assume user will select x
if ch == "o":
    choice = False #but if user selects '0' then it will be false


print(f"Player player_1 {ch}")

#players
player_1 = ch #user choice
player_2 = ""

#deciding player 2 value
if player_1 == "x":
    player_2  = "o"
else:
    player_2 = "x"


while True:
    print_board()
    #User_input
    inp = input("Enter position from 1 to 9  or press \"q\" to quit: ")
    #quit condition if user entered q
    if inp.lower() == "q":
        print("Thanks for playing")
        break
    num_checking(inp)
    #exception
    if range_check == False or number_check==False:
        if range_check == False:
            print("Only Numbers from '1' to '9' is allowed!!!")
        if number_check == False:
            print(inp,"is not a number!!!")
        continue
    # indexing
    inp = int(inp) - 1

    position = indexing(inp)
    #exception if user already gave input
    if check_input(position,board) == False:
        print("You already gave input at that position")

    #logic for appending x and o
    if choice is True:#if choice is false then print 0
        add_to_board(position,board,"x")
        choice = False #change it to True
    else:
        add_to_board(position, board, "o") #if choice is True then print X
        choice = True #change it to False

    print("Next Player turn....")


    if check_col(player_1,board) == True:
        print_board()
        print("Player 1 Win")
        break
    elif check_row(player_1, board) == True:
        print_board()
        print("Player 1 Win")
        break

    elif check_col(player_2,board) == True:
        print_board()
        print("Player 2 Win")
        break
    elif check_row(player_2, board) == True:
        print_board()
        print("Player 2 Win")
        break







