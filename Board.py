class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.colors = [[' ' for _ in range(8)] for _ in range(8)]
        self.colors[3][3] = 'W'
        self.colors[3][4] = 'B'
        self.colors[4][3] = 'B'
        self.colors[4][4] = 'W'



    def __getitem__(self, key):
        return self.colors[key]

    def flip(self, row, col):
        if self.colors[row][col] == 'W':
            self.colors[row][col] = 'B'
        else:
            self.colors[row][col] = 'W'

    def is_full(self):
        for row in self.colors:
            for cell in row:
                if cell == ' ':
                    return False

        return True

    def display(self):
        print('    0   1   2   3   4   5   6   7')

        print('  ---------------------------------')
        for i in range(8):
            print(i, end=' | ')
            for j in range(8):
                print(f'{self.colors[i][j]}', end=' | ')
            print()
            print('  ---------------------------------')

    def update_board(self, current_player):
        print('\n    0   1   2   3   4   5   6   7')
        print('  ---------------------------------')
        for i in range(8):
            print(i, end=' | ')
            for j in range(8):
                if self.board[i][j] == ' ':
                    valid_moves = current_player.findValidMoves(self.colors)
                    if (i, j) in valid_moves:
                        print('●', end=' | ')  # Use ● for valid moves
                    else:
                        print(self.colors[i][j], end=' | ')
                else:
                    print(self.colors[i][j], end=' | ')
            print()
            print('  ---------------------------------')
