class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def is_valid_move(self, row, col, board):

        pass

    def has_valid_move(self, board):
        for row in range(8):
            for col in range(8):
                if board.is_valid_move(row, col, self.color):
                    return True

        return False

    def count_score(self, board):
        score = sum(row.count(str(self.color)) for row in board)
        return score
