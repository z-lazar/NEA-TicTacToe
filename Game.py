import numpy as np
from pprint import pprint as pp

NULL_CHAR = '-'

class Game:
    def __init__(self, token_1, token_2):
        self._data = np.array([NULL_CHAR for _ in range(9)]).reshape((3,3))
        self.turn = 0
        self._token_1 = token_1
        self._token_2 = token_2

    def __repr__(self):
        out = ''
        for row in self._data:
            for item in row:
                out += f'[{item}] '
            out += '\n'
        return out

    def full(self):
        if NULL_CHAR not in self._data:
            return True
        return False


    def print_game_for_debugging(self):
        pp(self._data)

    def do_move(self, row, col):
        try:
            if self._data[row][col] != NULL_CHAR:
                raise InvalidMoveError
            if self.turn == 0:
                self._data[row][col] = self._token_1
            else:
                self._data[row][col] = self._token_2
        except IndexError:
            print('row and or column out of range')
        self.turn = (self.turn+1)%2
    
    def check_winner(self):
        token_1 = self._token_1
        token_2 = self._token_2
        """Function which checks winner - returns None for no winner, 1 for player 1 and 2 for player 2"""
        #check rows and columns
        data_copy = self._data[:]
        for row in data_copy:
            if ''.join(row) == token_1*3:
                return 1
            if ''.join(row) == token_2*3:
                return 2
        np_array = np.array(data_copy)
        for column in range(0, 3):
            if ''.join(np_array[:,column]) == token_1*3:
                return 1
            if ''.join(np_array[:,column]) == token_2*3:
                return 2

        #check diagonals
        if ''.join(np.diagonal(np_array)) == token_1*3 or ''.join(np.flipud(np_array).diagonal()) == token_1*3:
            return 1
        if ''.join(np.diagonal(np_array)) == token_2*3 or ''.join(np.flipud(np_array).diagonal()) == token_2*3:
            return 2
        
        #return none if no winner
        return None

class InvalidMoveError(Exception):
    pass

if __name__ == "__main__":
    pass

#If you see this the commit worked
