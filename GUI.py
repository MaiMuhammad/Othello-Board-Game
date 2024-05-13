import tkinter as tk
from input import NameDialog

class OthelloGUI:

    def __init__(self, master, game):
        self.master = master
        self.master.title("Othello")
        self.game = game
        self.create_board()

    def create_board(self):
        self.cells = [[None for _ in range(8)] for _ in range(8)]
        valid_moves = self.game.current_player.findValidMoves(self.game.board)
        for i in range(8):
            for j in range(8):
                cell = tk.Label(self.master, text=self.game.board[i][j], width=8, height=4, bg='green', relief=tk.RIDGE)
                cell.grid(row=i, column=j)
                if (i, j) in valid_moves:
                    cell.config(bg='light green')
                cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                self.cells[i][j] = cell

    def handle_click(self, row, col):
        if self.game.board[row][col] == ' ':
            valid_moves = self.game.current_player.findValidMoves(self.game.board)
            if (row, col) in valid_moves:
                self.game.board[row][col] = str(self.game.current_player.color)
                self.game.switch_player()
                self.update_board()

    def update_board(self):
        for i in range(8):
            for j in range(8):
                cell = self.cells[i][j]
                if self.game.board[i][j] == ' ':
                    valid_moves = self.game.current_player.findValidMoves(self.game.board)
                    if (i, j) in valid_moves:
                        cell.config(bg='light green')
                    else:
                        cell.config(text=' ', bg='green')
                else:
                    cell.config(text=self.game.board[i][j], bg='green')

    def show_message(self):
        if self.game.game_over():
            if self.game.player2.count_score(self.game.board) == self.game.player1.count_score(self.game.board):
                message = 'Game over!\nDraw!'
            else:
                message = f"Game over! {'Black' if self.game.player1.count_score(self.game.board) > self.game.player2.count_score(self.game.board) else 'White'} wins!"
        else:
            message = 'Game is still in progress'

        popup = tk.Toplevel(self.master)
        popup.attributes('-topmost', True)
        popup.attributes('-topmost', False)
        popup.title("Message")
        label = tk.Label(popup, text=message, font=("Helvetica", 12), padx=20, pady=10, width=20)
        label.pack()

        ok_button = tk.Button(popup, text="OK", command=popup.destroy, width=6, height=1)
        ok_button.pack(pady=8)