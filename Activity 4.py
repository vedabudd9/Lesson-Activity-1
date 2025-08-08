import random
from colorama import init, Fore, Style

def display_board(board):
    print()
    def colored(cell):
        if cell= 'X':
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
 