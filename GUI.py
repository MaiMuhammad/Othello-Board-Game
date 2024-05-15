import tkinter as tk
import tkinter.messagebox
import sys
from Computer import Computer  # Import the Computer class for the computer player


class OthelloGUI:

    def __init__(self, master, game, difficulty):
        self.master = master
        self.master.title("Othello")
        self.game = game
        self.create_board()  # Create the game board GUI
        self.difficulty = difficulty

    def create_board(self):
        # Configure the main window
        self.master.configure(bg='gray14')
        self.cells = [[None for _ in range(8)] for _ in range(8)]  # Initialize the cells on the game board
        valid_moves = self.game.current_player.findValidMoves(
            self.game.board.colors)  # Find valid moves for the current player

        # Create a frame to hold the score labels
        score_frame = tk.Frame(self.master, bg='gray22')
        score_frame.grid(row=0, column=0, columnspan=100, sticky="ns", padx=373, pady=(10,10))

        # Frame for player 1's score
        player1_frame = tk.Frame(score_frame, bg='gray22')
        player1_frame.pack(side=tk.LEFT, anchor=tk.W, pady=20, padx=80)

        # Left-aligned label for player 1's score
        self.player1_score = tk.StringVar()
        player1_label = tk.Label(player1_frame, text='Player\n', font=('Arial', 14, 'bold'), fg='sea green',
                                 bg='gray22',padx=10)
        player1_label.pack(side=tk.TOP, anchor=tk.CENTER)

        player1_score_label = tk.Label(player1_frame, textvariable=self.player1_score, font=('Arial', 12,), padx=12,
                                       fg='white', bg='gray22')
        player1_score_label.pack(side=tk.TOP, anchor=tk.W)

        # Frame for player 2's score
        player2_frame = tk.Frame(score_frame, bg='gray22')
        player2_frame.pack(side=tk.RIGHT, anchor=tk.E, pady=20, padx=80)

        # Right-aligned label for player 2's score
        self.player2_score = tk.StringVar()
        player2_label = tk.Label(player2_frame, text='Computer\n', font=('Arial', 14, 'bold'), padx=10,pady=0, fg='sea green',
                                 bg='gray22')
        player2_label.pack(side=tk.TOP, anchor=tk.E)

        player2_score_label = tk.Label(player2_frame, textvariable=self.player2_score, font=('Arial', 12), padx=12,
                                       anchor='center', fg='white', bg='gray22')
        player2_score_label.pack(side=tk.TOP)

        # Create the game board cells
        for i in range(8):
            for j in range(8):

                cell = tk.Canvas(self.master, width=60, height=60, bg='sea green', highlightthickness=1,
                                 highlightbackground='black')
                if j == 0:
                    cell.grid(row=i + 1, column=j, padx=(370, 0))
                else :
                    cell.grid(row=i + 1, column=j)
                if (i, j) in valid_moves:
                    cell.config(bg='dark sea green')
                    cell.bind('<Button-1>', lambda e, row=i, col=j: self.handle_click(row, col))
                self.cells[i][j] = cell

        # Initialize the starting discs on the board
        self.draw_filled_circle('W', 3, 3)
        self.draw_filled_circle('B', 4, 3)
        self.draw_filled_circle('B', 3, 4)
        self.draw_filled_circle('W', 4, 4)

        # Update the scores initially
        self.update_scores()

    def update_scores(self):
        # Update the player scores on the GUI
        self.player1_score.set(
            f"Color: {self.game.player1.color}\nScore: {self.game.player1.count_score(self.game.board.colors)}")
        self.player2_score.set(
            f"Color: {self.game.player2.color}\nScore: {self.game.player2.count_score(self.game.board.colors)}")

    def handle_click(self, row, col):
        # Handle player's move when a cell is clicked

        # checks that the cell is empty
        if self.game.board.colors[row][col] == ' ':

            # get players valid moves
            valid_moves = self.game.current_player.findValidMoves(self.game.board.colors)

            # checks that the chosen move is valid
            if (row, col) in valid_moves:

                # updates the letter based board
                self.game.board.colors[row][col] = str(self.game.current_player.color)

                # draws a circle with the players color in the selected cell
                self.draw_filled_circle(self.game.current_player.color, row, col)

                # appropriate pieces are flipped in the letter based board
                self.game.current_player.flip(row, col, self.game.board.colors)

                # updates gui board
                self.update_board()

                # returns all cells to original color
                for i in range(8):
                    for j in range(8):
                        cell = self.cells[i][j]
                        cell.config(bg='sea green')

                # switch players and  waits 1 sec for the computer to make its move
                self.game.switch_player()
                self.master.after(1000, self.computer_move)

    def update_board(self):
        if not isinstance(self.game.current_player, Computer):
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
                    else:
                        cell.config(bg='sea green')
                        self.draw_filled_circle(self.game.board.colors[i][j], i, j)

        self.update_scores()

        if self.game.game_over():
            self.show_message()
        elif not self.game.current_player.has_valid_move(self.game.board):
            tk.messagebox.showinfo("Oops", "No valid moves for you\nComputer's turn!")
            self.game.switch_player()
            self.computer_move()
            

    def computer_move(self):
        # Perform the computer's move

        # check if the computer is playing
        if isinstance(self.game.current_player, Computer):

            # gets best move via alpha beta pruning
            move = self.game.current_player.make_move(self.game.board.colors, self.difficulty)
            print(move)

            # if there is a valid move then the boards a re updated and appropriate pieces are flipped else if the game
            # is not over and the is no valid move then a message is printed

            if move is not None:
                row, col = move
                self.game.board.colors[row][col] = self.game.current_player.color
                self.game.current_player.flip(row, col, self.game.board)
            else:

                if self.game.game_over():
                    print("game over")
                    self.show_message()
                    pass
                tk.messagebox.showinfo("oops", "No valid moves for Computer\nYou're turn!")

            # players are switched and gui board is updated to show players valid moves
            self.game.switch_player()
            self.update_board()

    def draw_filled_circle(self, color, x, y):
        # Draw a filled circle on the canvas

        # takes color
        if color == "W":
            circle_color = "white"
        else:
            circle_color = "black"

        # prints circle based on the cell size, position and color
        cell_size = 60
        circle_radius = cell_size // 2
        canvas = self.cells[x][y]
        canvas.create_oval(5, 5, cell_size - 5, cell_size - 5, outline='black', width=1, fill=circle_color)

    def show_message(self):

        # print a message when the game is over, stating the winner or if it is a draw

        if self.game.player2.count_score(self.game.board.colors) == self.game.player1.count_score(
                self.game.board.colors):
            message = 'Game over!\nDraw!'
        else:
            message = f"Game over! {'Black' if self.game.player1.count_score(self.game.board.colors) > self.game.player2.count_score(self.game.board.colors) else 'White'} wins!"

        popup = tk.Toplevel(self.master)
        popup.title("Message")
        label = tk.Label(popup, text=message, font=("Helvetica", 12), padx=20, pady=10, width=20)
        label.pack()

        # closes popup , the game window and stops the system when button is clicked
        def close_windows():
            popup.destroy()
            self.master.destroy()
            sys.exit()

        ok_button = tk.Button(popup, text="OK", command=close_windows, width=6, height=1)
        ok_button.pack(pady=8)

        self.master.wait_window(popup)

