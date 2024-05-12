import tkinter as tk


class OthelloGUI:

    def __init__(self, master, game):
        self.master = master
        self.master.title("Othello")
        self.game = game
        self.create_board()

    def create_board(self):
        self.cells = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                cell = tk.Label(self.master, text=self.game.board[i][j], width=8, height=4, bg='green', relief=tk.RIDGE)
                cell.grid(row=i, column=j)
                cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                self.cells[i][j] = cell

    def handle_click(self, row, col):
        if self.game.board[row][col] == ' ':
            self.game.board[row][col] = str(self.game.current_player.color)
            self.game.switch_player()
            self.update_board()
            # Implement Othello logic to flip opponent's pieces and check for win conditions

    def update_board(self):
        for i in range(8):
            for j in range(8):
                self.cells[i][j].config(text=self.game.board[i][j])

    def show_message(self):
        if self.game.game_over():

            if self.game.player2.count_score() == self.game.player1.count_score():
                message = 'Game over!\nDraw!'
            else:
                message = f"Game over! {'Black' if self.game.player1.count_score() > self.game.player2.count_score() else 'White'} wins!"

        popup = tk.Toplevel(self.master)
        popup.title("Message")
        label = tk.Label(popup, text=message)
        label.pack()
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack()
