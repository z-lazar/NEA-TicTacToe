from abc import ABC, abstractmethod
from Game import Game, InvalidMoveError
from tkinter import *
from tkinter.ttk import *

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Square(Button):
    def __init__(self, master, r, c):
        Button.__init__(self, command=self.move, master=master, text=self._state, height=100, width=100)
        self._row = r
        self._col = c
        self._state = ''
    
    def change_state(self, new_state):
        self._state = new_state
        
    def move(self):
        pass

class Gui(Ui):
    def __init__(self):
        self._board = Game('x', 'o')
        self._squares = []

    def run(self):
        window = Tk()
        play = Button(
            text='Play',
            command=lambda:[window.destroy(), self.play_callback()])
        quit_ = Button(
            text='Quit',
            command=window.destroy
        )
        play.pack()
        quit_.pack()
        mainloop()

    #change this to use the square class which inherits from the tk Button class
    def play_callback(self):
        window_play = Tk()
        for r in range(3):
            for c in range(3):
                b = Button(
                    text='', 
                    master = window_play,
                    command=self.move 
                )
                b.grid(row=r, column=c)
        mainloop()
    
    def move(self):
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





