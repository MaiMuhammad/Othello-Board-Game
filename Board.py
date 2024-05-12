class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'

    def __getitem__(self, key):
        return self.board[key]

    def flip(self, row, col):
        if self[row][col] == 'W':
            self[row][col] = 'B'
        else:
            self[row][col] = 'W'

    def flip_in_between(self):
        # To be implemented
        pass

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False

        return True
