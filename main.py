import tkinter as tk
from Game import Game
from Player import Player
from Board import Board
from GUI import OthelloGUI
from Computer import Computer

if __name__ == "__main__":

    Player1 = Player('B')
    Player2 = Computer('W')
    root = tk.Tk()
    board = Board()
    game = Game(board, Player1, Player2)
    gui = OthelloGUI(root, game)
    root.mainloop()
