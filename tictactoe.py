"""
Author: Chris Lynch
Project: Tic Tac Toe

"""



def main():
    game_board = make_game_board()
    print(f'Welcome to Tic Tac Toe!\n')
    player1 = player_input()
    if player1 == 'X':
        player2 ='O'
    else: player2 = 'X'

    while not (if_you_won(game_board) or (tie(game_board))):
        print()
        show_game_board(game_board)
        print()
        player_move(player1, game_board)
        print()
        show_game_board(game_board)
        if if_you_won(game_board) or tie(game_board):
            if if_you_won(game_board):
                print('Congradulations For Winning!')
            if tie(game_board):
                print('Game Ended In A Tie!')
            break
        print()
        player_move(player2, game_board)


def make_game_board():
    board = []
    for i in range(9):
        board.append(i+1)
    return board


def show_game_board (game_board):
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}")
    print('--+---+--')
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}")
    print('--+---+--')
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}")
    

def player_input():
    player1 = input("Please pick a marker 'X' or 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print()
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper()
        elif player1.upper() == 'O':
            player2='X'
            print()
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper()
        else:
            print()
            player1 = input("Please pick a marker 'X' or 'O' ")


def player_move(player, board):
    num = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[num - 1] = player


def if_you_won(game_board):
    if game_board[0] == game_board[1] == game_board[2]:
        return True
    if game_board[0] == game_board[3] == game_board[6]:
        return True
    if game_board[0] == game_board[4] == game_board[8]:
        return True
    if game_board[2] == game_board[5] == game_board[8]:
        return True
    if game_board[6] == game_board[7] == game_board[8]:
        return True
    if game_board[2] == game_board[4] == game_board[6]:
        return True
    return False
    


def tie(game_board):
    for num in range(9):
        if game_board[num] != "X" and game_board[num] != "O":
            return False
    return True


if __name__ == "__main__":
    main()