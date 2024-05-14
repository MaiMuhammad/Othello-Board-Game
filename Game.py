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
        return game_over
