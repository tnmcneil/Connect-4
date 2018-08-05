#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for use in Connect Four
#

import random
from playgame import *

class AIPlayer(Player):
            """ an "intelligent" computer player that uses artificial
                intelligence techniques to look head some number of
                moves into the future to make its move. inherits
                from Player class.
            """
            def __init__(self, checker, tiebreak, lookahead):
                        """ constructs a new AIPlayer object
                        """
                        assert(checker == 'X' or checker == 'O')
                        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
                        assert(lookahead >= 0)
                        Player.__init__(self, checker)
                        self.tiebreak = tiebreak
                        self.lookahead = lookahead

            def __repr__(self):
                        """ Returns a string representation for
                            the AIPlayer object
                        """
                        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')')

            def max_score_column(self, scores):
                        """ takes a list scores of the score for each
                            column in the board and returns the index of
                            the column with the max score
                        """
                        max_score = max(scores)
                        max_index_list = []
                        for i in range(len(scores)):
                                    if scores[i] == max_score:
                                                max_index_list += [i]
                                                
                        if len(max_index_list) == 1:
                                    max_index = max_index_list[0]
                        else:
                                    if self.tiebreak == 'LEFT':
                                                max_index = max_index_list[0]
                                    elif self.tiebreak == 'RIGHT':
                                                max_index = max_index_list[-1]
                                    elif self.tiebreak == 'RANDOM':
                                                max_index = random.choice(max_index_list)

                        return max_index

            def scores_for(self, board):
                        """ takes a Board object and returns a list of the AIPlayer's
                            scores for each column in the board
                        """
                        scores = [50] * board.width
                        for i in range(board.width):
                                    if board.can_add_to(i) == False:
                                                scores[i] = -1
                                    elif board.is_win_for(self.checker) == True:
                                                scores[i] = 100
                                    elif board.is_win_for(self.opponent_checker()) == True:
                                                scores[i] = 0
                                    elif self.lookahead == 0:
                                                scores[i] = 50
                                    else:
                                                board.add_checker(self.checker, i)
                                                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead -1)
                                                opp_scores = opponent.scores_for(board)
                                                if max(opp_scores) == 100:
                                                            scores[i] = 0
                                                elif max(opp_scores) == 0:
                                                            scores[i] = 100
                                                elif max(opp_scores) == 50:
                                                            scores[i] = 50
                                                board.remove_checker(i)  
                        return scores

            def next_move(self, board):
                        """ overrides the next_move inherited from Player so that it
                            uses the AIPlayer's judgement to decide its next move instead
                            of asking the user for a column
                        """
                        scores = self.scores_for(board)
                        print(scores)
                        max_index = self.max_score_column(scores)
                        return max_index
                        

class RandomPlayer(Player):
            """ can be used for an unintelligent computer
                player that makes moves at random. Inherits
                from the Player class
            """
            def next_move(self, board):
                        """ replaces the next_move method from player.
                            chooses a column to add a checker to at random
                            from the columns that have space
                        """
                        cols = []
                        for i in range(board.width):
                                 if board.can_add_to(i) == True:
                                             cols += [i]
                        col = int(random.choice(cols))
                        return col
                        board.add_checker(self.checker, col)
                        self.num_moves += 1
                        
