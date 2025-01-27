from random import choice


def new_game():
    '''
    starts a new game
    '''
    global players
    global active_player

    # tictactoe in ascii art
    print("\n  _______ _____ _____   _______       _____   _______ ____  ______ \n |__   __|_   _/ ____| |__   __|/\   / ____| |__   __/ __ \|  ____|\n    | |    | || |         | |  /  \ | |         | | | |  | | |__   \n    | |    | || |         | | / /\ \| |         | | | |  | |  __|  \n    | |   _| || |____     | |/ ____ \ |____     | | | |__| | |____ \n    |_|  |_____\_____|    |_/_/    \_\_____|    |_|  \____/|______|\n\n")
    
    pl1 = input("Name of player 1 (x): ")
    pl2 = input("Name of player 2 (o): ")

    players = [pl1,pl2]
    active_player = choice(players)

    print("Type the coordiantes of cell to mark 'x' or 'o' in that place\n")

    # tictactoe table 
    print(f"\n     |     |     \n 11  | 12  | 13  \n     |     |     \n-----+-----+-----\n     |     |     \n 21  | 22  | 23  \n     |     |     \n-----+-----+-----\n     |     |     \n 31  | 32  | 33  \n     |     |     ")


    print(f"\n{active_player}'s turn")



def is_win():
    '''
    returns true if there is a winning condition
    tie if theres is a tie
    and returns false elsewise
    '''
    
    for row in range(3):
        if game[row][0] == game[row][1] == game[row][2] != " ":
            return True

    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] != " ":
            return True

    if game[0][0] == game[1][1] == game[2][2] != " ":
        return True
    
    elif game[0][2] == game[1][1] == game[2][0] != " ":
        return True
    
    elif empty_space() is False:
        return "Tie"
    
    else:
        return False



def next_turn(row,col):
    '''
    takes parameter of rows and columns 
    puts x and o in that place
    switches turns in player 1 and 2
    '''
    global game
    global active_player

    if game[row][col] == " " and is_win() is False:
        if active_player == players[0]:
            game[row][col] = "x"

            if is_win() is False:
                active_player = players[1]
                # tictactoe table 
                print(f"\n     |     |     \n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n     |     |     ")
                print(f"\n{players[1]}'s turn")
              
            elif is_win() is True:
                # tictactoe table 
                print(f"\n     |     |     \n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n     |     |     ")
                print(f"\n{players[0]} won!")
            
            elif is_win() == "Tie":
                # tictactoe table 
                print(f"\n     |     |     \n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n     |     |     ")
                print("\nIt's a tie!")
                
        else:
            game[row][col] = "o"

            if is_win() is False:
                active_player = players[0]
                # tictactoe table 
                print(f"\n     |     |     \n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n     |     |     ")
                print(f"\n{players[0]}'s turn")
                
            elif is_win() is True:
                # tictactoe table 
                print(f"\n     |     |     \n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n     |     |     ")
                print(f"\n{players[1]} won!")
            
            elif is_win() == "Tie":
                # tictactoe table 
                print(f"\n     |     |     \n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n     |     |     \n-----+-----+-----\n     |     |     \n  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n     |     |     ")
                print("\nIt's a tie!")



def empty_space():
    '''
    looks for empty spaces
    if there are no empty spaces there would be a tie
    '''
    for i in game:
        for j in i:
            if j == " ":
                return True
    else:
        return False




players = ["Player1","Player2"]

game = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]


# main game loop starts here
new_game()


while is_win() is False:
    
    choices = input("> ") # > 11
    while not choices in {"11","12","13","21","22","23","31","32","33"}:
        choices = input("> ")

    next_turn(int(choices[0])-1,int(choices[1])-1)

