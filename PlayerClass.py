#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#

from BoardClass import Board

# Write your class below.

class Player:
            """ Player class to represent a player of
                the Connect Four game
            """
            def __init__(self, checker):
                        """ constructor for player object """
                        assert(checker == 'X' or checker == 'O')
                        self.checker = checker
                        self.num_moves = 0

            def __repr__(self):
                        """ returns a string representation for
                            the player object
                        """
                        return 'Player ' + self.checker

            def opponent_checker(self):
                        """ returns a string representation for
                            the Player object opponent's checker
                        """
                        if self.checker == 'X':
                                    return 'O'
                        elif self.checker == 'O':
                                    return 'X'

            def next_move(self, board):
                        """ asks the user for a column to put a
                            checker in the board object input and
                            returns the column number if it is valid,
                            and will ask for a column until a valid
                            one is given
                        """
                        col = eval(input('Emter a column: '))
                        col = int(col)
                        if board.can_add_to(col) == True:
                                    return col
                        else:
                                    a = False
                                    while a == False:
                                                print('Try again!')
                                                col = eval(input('Enter a column: '))
                                                col = int(col)
                                                if board.can_add_to(col) == True:
                                                            a = True
                                                            self.num_moves += 1
                                                            return col
                        
                        
                        
