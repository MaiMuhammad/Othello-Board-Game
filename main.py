
import tkinter as tk
from Game import Game
from Player import Player
from Board import Board
from GUI import OthelloGUI
from Computer import Computer
from Difficulty import DifficultyLevelWindow


if __name__ == "__main__":
    # def on_difficulty_selected(difficulty):
    #     print(difficulty)
    #     return difficulty
    #
    # difficulty_window = DifficultyLevelWindow(on_difficulty_selected)
    # difficulty_window.mainloop()
    Player1 = Player('B')
    Player2 = Player('W')
    # Player2 = Computer('W', on_difficulty_selected)
    # print(str(Player2.difficulty_level))
    root = tk.Tk()
    board = Board()
    game = Game(board, Player1, Player2)
    gui = OthelloGUI(root, game)
    root.mainloop()
