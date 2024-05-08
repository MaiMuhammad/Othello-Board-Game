class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'

    def __getitem__(self, key):
        return self.board[key]

    def display(self):
        print('    0   1   2   3   4   5   6   7')

        print('  ---------------------------------')
        for i in range(8):
            print(i, end=' | ')
            for j in range(8):
                print(f'{self.board[i][j]}', end=' | ')
            print()
            print('  ---------------------------------')

    def flip(self, row, col):
        if self[row][col] == 'W':
            self[row][col] = 'B'
        else:
            self[row][col] = 'W'

    def filp_inBeween(self):
        #to be implemented
        pass

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False

        return True
