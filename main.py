
import tkinter as tk
from Game import Game
from Player import Player
from Board import Board
from GUI import OthelloGUI
from Computer import Computer
from Difficulty import DifficultyLevelWindow

if __name__ == "__main__":
    board = Board()
    player1 = Player('B')
    player2 = Computer('W')

    game = Game(board, player1, player2)
    #
    # print("Welcome to the game!\n")
    # print("Player 1 please enter your name:")
    # player1.name = input()
    # print(f"Player 1's name: {player1.name}\nPlayer 1's color: {player1.color}")

    # game.play()


if __name__ == "__main__":

    difficulty_window = DifficultyLevelWindow()
    difficulty_window.mainloop()
    Player1 = Player('B')
    # Player2 = Player('W')
    Player2 = Computer('W')

    root = tk.Tk()
    board = Board()
    game = Game(board, Player1, Player2)
    gui = OthelloGUI(root, game,difficulty_window.difficulty)
    print(gui.difficulty)
    root.mainloop()


