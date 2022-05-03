from abc import ABC, abstractmethod
from Game import Game, InvalidMoveError
import tkinter as tk

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        self._board = Game('x', 'o')

    def run(self):
        window = tk.Tk()
        play = tk.Button(
            text='Play',
            command=self.play_callback).pack()
        quit_ = tk.Button(
            text='Quit',
            command=window.quit
        )

    def play_callback():
        pass
    


class Terminal(Ui):
    def __init__(self):
        self._board = Game('x', 'o')

    def run(self):
        print('RUNNING...')
        while not self._board.check_winner() and not self._board.full():
            print(self._board)
            inp = [char for char in input(f'Player {self._board.turn + 1} (give a grid reference from 1,1 to 3,3): ').strip()]
            try:
                self._board.do_move(int(inp[0])-1, int(inp[-1])-1)
            except InvalidMoveError:
                print("There is already a token there")
        print(self._board)
        if self._board.full():
            print('Draw')
        else:
            print(f'Player {self._board.check_winner()} has won')
        
def Debugging():
    te = Gui()
    te.run()

Debugging()





