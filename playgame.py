#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game
#

from BoardClass import Board
from PlayerClass import Player
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(player, board):
            """ Takes a Player object and Board object as input and
                prints whose turn it is, gets their next move, applies
                it and then prints the board and evaluates if their was
                a tie or a win and returns the appropriate response, or
                False otherwise.
            """
            print(str(player) + "'s turn")
            col = player.next_move(board)
            board.add_checker(player.checker, col)
            player.num_moves += 1
            print()
            print(board)
            if board.is_win_for(player.checker) == True:
                        print(player, 'wins in', player.num_moves, 'moves.')
                        print('Congratulations!')
                        return True
            elif board.is_full() == True:
                        print("It's a tie!")
                        return True
            else:
                        return False                        
            
            
            
