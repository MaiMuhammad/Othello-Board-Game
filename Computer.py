import copy
from Player import Player

class Computer(Player):
    
    def __init__(self, color,difficulty):
        super().__init__(color)
        self.difficulty_level = difficulty  # Default difficulty level

    def make_move(self, board):
        # self.difficulty_level = self.choose_difficulty_level()
        # Call Alpha-Beta Pruning to determine the best move
        best_move = self.alpha_beta_pruning(board, self.difficulty_level, float('-inf'), float('inf'), True)[1]
        return best_move

    def alpha_beta_pruning(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or not self.has_valid_move(board):
            return self.Utility(board), None

        if maximizingPlayer:
            max_eval = float('-inf')
            best_move = None
            for move in self.findValidMoves(board):
                new_board = self.make_move_on_board(board, move, self.color)#take board as colors
                eval, _ = self.alpha_beta_pruning(new_board, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.findValidMoves(board):
                new_board = self.make_move_on_board(board, move, self.opposingColor)
                eval, _ = self.alpha_beta_pruning(new_board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval, best_move

    def make_move_on_board(self, board, move, color):#colors
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = color
        self.flip(move[0], move[1], new_board)
        return new_board

    def Utility(self, board):#colors
        num_black = sum(row.count('B') for row in board)
        num_white = sum(row.count('W') for row in board)
        return num_black - num_white if self.color == 'B' else num_white - num_black

    def is_game_over(self, board):
        return len(self.get_valid_moves(board, 'B')) == 0 and len(self.get_valid_moves(board, 'W')) == 0
        
    
    # def choose_difficulty_level(self):
    #     print("Choose difficulty level:")
    #     print("1. Easy")
    #     print("2. Medium")
    #     print("3. Hard")
    #     choice = input("Enter your choice (1-3): ")
    #     if choice == '1':
    #         self.dificullty_level = 1
    #     elif choice == '2':
    #         self.dificullty_level =  3
    #     elif choice == '3':
    #         self.dificullty_level = 5
    #     else:
    #         print("Invalid choice. Defaulting to medium.")
    #         self.dificullty_level = 3