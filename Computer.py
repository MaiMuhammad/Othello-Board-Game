from Player import Player

class Computer(Player):
    
    def __init__(self, color):
        super().__init__(color)

    def make_move(self, board):
        # Call Minimax to determine the best move
        pass

    def Minimax(self, board, depth, alpha, beta, maximizingPlayer):
        # Implement the minimax algorithm with alpha-beta pruning here
        pass

    def Utility(self, board):
        num_black = sum(row.count('B') for row in board)
        num_white = sum(row.count('W') for row in board)
        return num_black - num_white if self.color == 'B' else num_white - num_black
