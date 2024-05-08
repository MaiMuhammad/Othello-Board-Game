class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def is_valid_move(self, row, col,board):
        # Implement validation logic here
        valid = False
        #directions = {(1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1)}
        if board[row][col] == ' ':
            # Check if the move results in flipping opponent's discs
            # and update valid accordingly
            valid = True  # Temporary placeholder, update with actual logic
        return valid

    def has_valid_move(self, board):
        for row in range(8):
            for col in range(8):
                if board.is_valid_move(row, col, self.color):
                    return True

        return False

    def make_move(self, board, x, y):
        if board.is_valid_move(x, y, self.color):
            board[x][y] = self.color
            #add the logic of how to determine the peices to flip(flip_inBetween())

    def count_score(self, board):
        score = sum(row.count(str(self.color)) for row in board)
        return {str(self.name): score}
