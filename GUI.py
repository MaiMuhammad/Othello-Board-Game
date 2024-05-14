import tkinter as tk

class OthelloGUI:

    def __init__(self, master, game):
        self.master = master
        self.master.title("Othello")
        self.game = game
        self.create_board()

    def create_board(self):
        self.master.configure(bg='gray14')
        self.cells = [[None for _ in range(8)] for _ in range(8)]
        valid_moves = self.game.current_player.findValidMoves(self.game.board.colors)

        # Create a frame to hold the score labels
        score_frame = tk.Frame(self.master, bg='gray22')
        score_frame.grid(row=0, column=0, columnspan=100, sticky="ew", padx=80, pady=20)


        # Frame for player 1's score
        player1_frame = tk.Frame(score_frame,bg='gray22')
        player1_frame.pack(side=tk.LEFT, anchor=tk.W,pady=30,padx=30)  # Adjust padx here

        # Left-aligned label for player 1's score
        self.player1_score = tk.StringVar()
        player1_label = tk.Label(player1_frame, text='Player 1\n', font=('Arial', 14, 'bold'), fg='sea green',bg='gray22')
        player1_label.pack(side=tk.TOP, anchor=tk.W)

        player1_score_label = tk.Label(player1_frame, textvariable=self.player1_score, font=('Arial', 12,), padx=10,fg='white',bg='gray22')
        player1_score_label.pack(side=tk.TOP,anchor=tk.W)

        # Frame for player 2's score
        player2_frame = tk.Frame(score_frame,bg='gray22')
        player2_frame.pack(side=tk.RIGHT, anchor=tk.E, padx=(5, 0))

        # Right-aligned label for player 2's score
        self.player2_score = tk.StringVar()
        player2_label = tk.Label(player2_frame, text='Player 2\n', font=('Arial', 14, 'bold'),padx=30, fg='sea green',bg='gray22')
        player2_label.pack(side=tk.TOP, anchor=tk.E)

        player2_score_label = tk.Label(player2_frame, textvariable=self.player2_score, font=('Arial', 12), padx=30,anchor='center',fg='white',bg='gray22')
        player2_score_label.pack(side=tk.TOP)

        for i in range(8):
            for j in range(8):
                cell = tk.Canvas(self.master, width=55, height=55, bg='sea green', highlightthickness=1,
                                 highlightbackground='black')
                cell.grid(row=i + 1, column=j)
                if (i, j) in valid_moves:
                    cell.config(bg='dark sea green')
                    cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                self.cells[i][j] = cell

        self.draw_filled_circle('W', 3, 3)
        self.draw_filled_circle('B', 4, 3)
        self.draw_filled_circle('B', 3, 4)
        self.draw_filled_circle('W', 4, 4)

        # Update the scores initially
        self.update_scores()

    def update_scores(self):
        self.player1_score.set(f"Color: {self.game.player1.color}\nScore: {self.game.player1.count_score(self.game.board.colors)}")
        self.player2_score.set(f"Color: {self.game.player2.color}\nScore: {self.game.player2.count_score(self.game.board.colors)}")

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
                        cell.config(bg='dark sea green')
                        cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                    else:
                        cell.config(bg='sea green')
                    cell.delete("circle")
                else:
                    cell.config(bg='sea green')

                    self.draw_filled_circle(self.game.board.colors[i][j], i, j)

        # Update the scores initially
        self.update_scores()

        # After updating the board, check if the game is over
        if self.game.game_over():
            self.show_message()

    def draw_filled_circle(self, color, x, y):
        if color == "W":
            circle_color = "white"
        else:
            circle_color = "black"
        cell_size = 55
        circle_radius = cell_size // 2
        canvas = self.cells[x][y]
        canvas.create_oval(4, 4, cell_size - 4, cell_size - 4, outline='black', width=1, fill=circle_color)


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
