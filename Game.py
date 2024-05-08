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
        if not self.board.is_full() or (not self.player1.has_valid_move(self.board) and not self.player2.has_valid_move(self.board)):
            game_over = True
        return game_over

    def play(self):
        while not self.game_over():
            self.board.display()
            print(str(self.current_player.name) + "'s turn")
            print('row')

            row = int(input("Row:"))
            col = int(input("Column:"))
            self.current_player.make_move(self.board, row, col)
            if self.current_player.is_valid_move(row, col, self.current_player.color):
                self.board.flip(row, col)
                self.switch_player()

        self.board.display()
        if self.game_over():
            score = self.board.count_score()
        if score['B'] == score['W']:
            print('Game over!\nDraw!')
        else:
            print(f"Game over! {'Black' if score['B'] > score['W'] else 'White'} wins!")
