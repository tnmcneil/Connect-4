#
# ps10pr1.py - Problem Set 10 Problem 1
#
# Connect Four Board Class
#

class Board:
            """ data type for a Connect Four board with
                arbitrary dimensions
            """
            def __init__(self, height, width):
                        """ constructor for Board objects """
                        self.height = height
                        self.width = width
                        self.slots = [[' ']*self.width for r in range(height)]

            def __repr__(self):
                        """ Returns a string representation for
                            a Board object.
                        """
                        s = ''

                        for row in range(self.height):
                                    s += '|'

                                    for col in range(self.width):
                                                s += self.slots[row][col] + '|'
                                    s += '\n'
                        l = ('|' + ' ')*self.width
                        s += '-'*(len(l) + 1)
                        s += '\n'
                        n = []
                        n += range(self.width)
                        for i in range(len(n)):
                                    s += ' ' + str(n[i] % 10)
                        
                        return s

            def add_checker(self, checker, col):
                        """ adds the specified checker, a string of either 'X'
                            or 'O', to the column of index col on the Board object
                        """
                        assert(checker == 'X' or checker == 'O')
                        assert(0 <= col < self.width)
                        row = 0
                        while self.slots[row][col] == ' ' and row < (self.height - 1):
                                           row += 1
                        if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                                    row -= 1
                        self.slots[row][col] = checker

            def reset(self):
                        """ resets the called Board object to the initial
                            empty setup where every slot is just a single space
                        """
                        self.slots = [[' ']*self.width for r in range(self.height)]

            def add_checkers(self, colnums):
                        """ takes in a string of column numbers and places alternating
                            checkers in those columns of the called Board object,
                            starting with 'X'.
                        """
                        checker = 'X'

                        for col_str in colnums:
                                    col = int(col_str)
                                    if 0 <= col < self.width:
                                                self.add_checker(checker, col)

                                    if checker == 'X':
                                                checker = 'O'
                                    else:
                                                checker = 'X'
            def can_add_to(self, col):
                        """ returns True if it is valid to place a checker in column
                            col on the called Board object, and False otherwise.
                            it is valid if col is in the range from 0 to the last
                            column, and the column is not full
                        """
                        if 0 <= col < self.width and self.slots[0][col] == ' ':
                                    return True
                        else:
                                    return False

            def is_full(self):
                        """ returns True if the called Board object is completely
                            full and False otherwise
                        """
                        count = 0
                        for r in range(self.height):
                                 for c in range(self.width):
                                             if self.can_add_to(c) == True:
                                                         count += 1
                        if count > 0:
                                    return False
                        else:
                                    return True

            def remove_checker(self, col):
                        """ removes the top checker from the column col of the
                            called Board object, and does nothing if the column
                            is empty.
                        """
                        row = 0
                        while self.slots[row][col] == ' ' and row < (self.height - 1):
                                    row += 1
                        self.slots[row][col] = ' '

            def is_horizontal_win(self, checker):
                        """ Checks for a horizontal win for the specified checker
                        """
                        for row in range(self.height):
                                    for col in range(self.width - 3):
                                                if self.slots[row][col] == checker and \
                                                   self.slots[row][col + 1] == checker and \
                                                   self.slots[row][col + 2] == checker and \
                                                   self.slots[row][col + 3] == checker:
                                                            return True
                        return False
            
            def is_vertical_win(self, checker):
                        """ Checks for a vertical win for the specified checker
                        """
                        for row in range(self.height - 3):
                                    for col in range(self.width):
                                                if self.slots[row][col] == checker and \
                                                   self.slots[row + 1][col] == checker and \
                                                   self.slots[row + 2][col] == checker and \
                                                   self.slots[row + 3][col] == checker:
                                                            return True
                        return False

            def is_down_diagonal_win(self, checker):
                        """ Checks for a down diagonal win for the specified checker.
                            (diagonal down left to right)
                        """
                        for row in range(self.height - 3):
                                    for col in range(self.width - 3):
                                                if self.slots[row][col] == checker and \
                                                   self.slots[row + 1][col + 1] == checker and \
                                                   self.slots[row + 2][col + 2] == checker and \
                                                   self.slots[row + 3][col + 3] == checker:
                                                            return True
                        return False

            def is_up_diagonal_win(self, checker):
                        """ Checks for an up diagonal win for the specified checker.
                            (diagonal up left to right)
                        """
                        for row in range(3, self.height):
                                    for col in range(self.width - 3):
                                                if self.slots[row][col] == checker and \
                                                   self.slots[row - 1][col + 1] == checker and \
                                                   self.slots[row - 2][col + 2] == checker and \
                                                   self.slots[row - 3][col + 3] == checker:
                                                            return True
                        return False
                        
                                    

            def is_win_for(self, checker):
                        """ returns True if there are four slots in a row on the
                            called Board object containing the input checker (either
                            'X' or 'O' and False otherwise
                        """
                        assert(checker == 'X' or checker == 'O')
                        if self.is_horizontal_win(checker) == True or \
                           self.is_vertical_win(checker) == True or \
                           self.is_down_diagonal_win(checker) == True or \
                           self.is_up_diagonal_win(checker) == True:
                                    return True
                        else:
                                    return False


                        
