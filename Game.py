class Game:


    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def game_over(self):
        game_over = False
        if self.board.is_full():
            # or (not self.player1.has_valid_move(self.board) and not self.player2.has_valid_move(self.board)):
            game_over = True
        elif not self.current_player.has_valid_move(self.board):
            self.switch_player()
        if not self.current_player.has_valid_move(self.board):
            game_over = True
        return game_over

    def play(self):
        # Choose difficulty level for the computer player
        depth = self.player2.choose_difficulty_level()

        while not self.game_over():
            self.board.update_board(self.current_player)
            if self.current_player == self.player1:  # Human player's turn
                # Get the move input in the format "row,col"
                move_input = input("Enter your move (row,col): ")
                try:
                    # Split the input into row and column
                    row, col = map(int, move_input.split(","))
                    if not (0 <= row < 8 and 0 <= col < 8):
                        raise ValueError("Invalid input. Row and column must be between 0 and 7.")
                except ValueError as e:
                    print(f"Invalid input. {e}")
                    continue

                # Make the move if it's valid
                valid_moves = self.current_player.findValidMoves(self.board.colors)
                if (row, col) in valid_moves:
                    self.board.colors[row][col] = self.current_player.color
                    self.current_player.flip(row, col, self.board)
                    self.switch_player()
                else:
                    print("Invalid move. Try again.")
            else:  # Computer player's turn
                print(end='\n')
                print("Computer's turn...")
                move = self.current_player.make_move(self.board.colors, depth)
                if move is not None:
                    row, col = move
                    self.board.colors[row][col] = self.current_player.color
                    self.current_player.flip(row, col, self.board)
                    self.switch_player()

        # Display the final board and result
        self.board.update_board(self.current_player)
        score = self.board.count_score()
        if score['B'] == score['W']:
            print('Game over!\nDraw!')
        else:
            print(f"Game over! {'Black' if score['B'] > score['W'] else 'White'} wins!")
