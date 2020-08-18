# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
winner = None
current_player = "X"


# display's the game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


# handles the next turn
def handle_turn(player):
    print(player + "'s turn")
    position = int(input("Choose a position from 1-9: "))
    valid = False
    while not valid:  # will check if the player used the same space
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # check if the player input from 1-9
            position = int(input(" Invalid input. Choose a position from 1-9: "))
        position = int(position)-1
        if board[position] == '-':
            valid = True
        else:
            print("Invalid input try again")
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():  # check for winner
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

