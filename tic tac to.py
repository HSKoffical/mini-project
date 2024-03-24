test_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_game(test_board):
    print(test_board[1]+" | "+test_board[2]+" | "+test_board[3])
    print(test_board[4]+" | "+test_board[5]+" | "+test_board[6])
    print(test_board[7]+" | "+test_board[8]+" | "+test_board[9])
display_game(test_board)
def player1_choice_fun():
    player1_choice="wrong"
    while player1_choice not in ["X","O"]:
        player1_choice=input("Player 1 please choice X or O:: ")
        if player1_choice not in ["X","O"]:
            print("Wrong input please X and O")
    if player1_choice=="X":
        return "X"
    if player1_choice=="O":
        return "O"
player1=player1_choice_fun()
def player2_choice_fun():
    if player1=="X":
        return "O"
    elif player1=="O":
        return "X"
player2=player2_choice_fun()

def combination():

    if (test_board[1] == test_board[2] == test_board[3] == 'X') or (test_board[4] == test_board[5] == test_board[6] == 'X') or (test_board[7] == test_board[8] == test_board[9] == 'X') or (test_board[1] == test_board[4] == test_board[7] == 'X') or (test_board[2] == test_board[5] == test_board[8] == 'X') or (test_board[3] == test_board[6] == test_board[9] == 'X') or (test_board[1] == test_board[5] == test_board[9] == 'X') or (test_board[3] == test_board[5] == test_board[7] == 'X'):
        print(" Congarulation The winner is X")
        return True

    elif (test_board[1] == test_board[2] == test_board[3] == "O") or (
                test_board[4] == test_board[5] == test_board[6] == "O") or (
                test_board[7] == test_board[8] == test_board[9] == "O") or (
                test_board[1] == test_board[4] == test_board[7] == "O") or (
                test_board[2] == test_board[5] == test_board[8] == "0") or (
                test_board[3] == test_board[6] == test_board[9] == "O") or (
                test_board[1] == test_board[5] == test_board[9] == "O") or (
                test_board[3] == test_board[5] == test_board[7] == "O"):
        print(" Congraulation The winner is O")
        return True


combination()
def replacement():
        user_input="wrong"
        flag = 1

        while flag<10:

            if combination()==True:
                break
            else:

                    user_input = int(input("enter the number between(1 t0 9):: "))
                    if player1 == "X":
                                if flag in [1, 3, 5, 7, 9]:
                                    test_board[user_input] = "X"
                                elif flag in [2, 4, 6, 8]:
                                    test_board[user_input] = "O"
                    elif player1 == "O":
                                if flag in [1, 3, 5, 7, 9]:
                                    test_board[user_input] = "O"
                                elif flag in [2, 4, 6, 8]:
                                    test_board[user_input] = "X"
                    flag=flag+1
                    combination()
                    display_game(test_board)

replacement()
def yes_no():
    choice="wrong"
    while choice not in ["yes","no"]:
        choice=input("Are you ready to play (yes or no):: ")
        if choice not in ["yes","no"]:
            print("Wrong input please yes and no")
    if choice=="yes":
        return "yes"
    if choice=="no":
        return "no"

choice=yes_no()
while choice=="yes":
    test_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_game(test_board)
    player1_choice_fun()
    player2_choice_fun()
    combination()
    replacement()
    yes_no()







