import random
from colorama import init, Fore, Style

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell+ Style.RESET_ALL
        elif cell= '0' :
            return Fore.BLUE + cell + Style.RESET_ALL 
        else:
            reture Fore.YELLOW + cell + Style. RESET_ALL
            print()

         print(''+ board[0] + ' | ' + board[1] + ' | ' + board[2])

         print('———-')

         print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])

         print('———-')

         print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

         print()
def player_choice():
    symbol = ''
    while symbol not in['X', 'O']
        symbol=input(Fore.GREEN + "Do you want to be X or O?").upper()
    if symbol == 'X':
        return ('X','O')
    else:
        return ('O','X')
def player_move(board, symbol):
     move=-1
     while move not in range(1,10) or not board[move-1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range (1,10) or not board[move -1].isdigit
               print("Invalid more. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9")
    board[move-1]  symbol
ef ai_move(board,ai_symbol, player_symbol):
     for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol
               board[i]= ai_symbol
               return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win
            (board_copy, player_symbol):
                board[i] = ai_symbol
                return 
    possible_moves = [i for i in range(9) if board [i].isdigit()]
    move=random.choice(possible_moves)
    board[move] = ai_symbol
def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]  
    for cond in win_condition:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False
def check_full(board):
    return all(not spot.isdigit() for spot in board)
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input (Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        board=['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True
        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if turn check_win(board, player_symbol):
                    display_board(board)
                    print("Congratulation! " + player_name + ", you have won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                 ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol)
                     display_board(board)
                     print("AI won the game!")
                     game_on=False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again = input("Do you want to play again? yes/no")
        if play_again != 'yes':
            print("Thank you for playing?")
            break
if __name__ == "__main__":
    tic_tac_toe()
