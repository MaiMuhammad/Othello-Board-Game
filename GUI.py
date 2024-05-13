import tkinter as tk

class OthelloGUI:

    def __init__(self, master, game):
        self.master = master
        self.master.title("Othello")
        self.game = game
        self.create_board()

    def create_board(self):
        self.cells = [[None for _ in range(8)] for _ in range(8)]
        valid_moves = self.game.current_player.findValidMoves(self.game.board.colors)
        for i in range(8):
            for j in range(8):
                cell = tk.Canvas(self.master, width=60, height=60, bg='green', highlightthickness=1,
                                 highlightbackground='black')
                cell.grid(row=i, column=j)
                if (i, j) in valid_moves:
                    cell.config(bg='dark green')
                    cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                self.cells[i][j] = cell

        self.draw_filled_circle('W', 3, 3)
        self.draw_filled_circle('B', 4, 3)
        self.draw_filled_circle('B', 3, 4)
        self.draw_filled_circle('W', 4, 4)

    def handle_click(self, row, col):
        if self.game.board.colors[row][col] == ' ':

            valid_moves = self.game.current_player.findValidMoves(self.game.board.colors)
            if (row, col) in valid_moves:
                self.game.board.colors[row][col] = str(self.game.current_player.color)
                self.draw_filled_circle(self.game.current_player.color, row, col)
                self.game.current_player.flip(row, col, self.game.board.colors)
                self.game.switch_player()
                self.update_board()  # Update the board after each move

    def update_board(self):

        for i in range(8):
            for j in range(8):
                cell = self.cells[i][j]
                valid_moves = self.game.current_player.findValidMoves(self.game.board.colors)
                if self.game.board.colors[i][j] == ' ':
                    if (i, j) in valid_moves:
                        cell.config(bg='dark green')
                        cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                    else:
                        cell.config(bg='green')
                    cell.delete("circle")
                else:
                    cell.config(bg='green')

                    self.draw_filled_circle(self.game.board.colors[i][j], i, j)

        # After updating the board, check if the game is over
        if self.game.game_over():
            self.show_message()

    def draw_filled_circle(self, color, x, y):
        if color == "W":
            circle_color = "white"
        else:
            circle_color = "black"
        cell_size = 60
        circle_radius = cell_size // 2
        canvas = self.cells[x][y]
        canvas.create_oval(2, 2, cell_size - 2, cell_size - 2, outline='black', width=1, fill=circle_color)


    def show_message(self):
        if self.game.game_over():
            if self.game.player2.count_score(self.game.board.colors) == self.game.player1.count_score(
                    self.game.board.colors):
                message = 'Game over!\nDraw!'
            else:
                message = f"Game over! {'Black' if self.game.player1.count_score(self.game.board.colors) > self.game.player2.count_score(self.game.board.colors) else 'White'} wins!"
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

        self.master.wait_window(popup)
