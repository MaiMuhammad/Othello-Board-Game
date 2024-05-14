from Player import Player

class Computer(Player):
    
    def __init__(self, color):
        super().__init__(color)

    def make_move(self, board):
        # Call Alpha-Beta Pruning to determine the best move
        self.dificulltyLevel = self.choose_difficulty_level(self)
        best_move = self.alpha_beta_pruning(board, self.dificulltyLevel, float('-inf'), float('inf'), True)[1]  # Adjust depth as needed
        return best_move

    def alpha_beta_pruning(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.is_game_over(board):
            return self.Utility(board), None
        
        if maximizingPlayer:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_valid_moves(board, self.color):
                new_board = self.make_move_on_board(board, move, self.color)
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
            opponent_color = 'B' if self.color == 'W' else 'W'
            for move in self.get_valid_moves(board, opponent_color):
                new_board = self.make_move_on_board(board, move, opponent_color)
                eval, _ = self.alpha_beta_pruning(new_board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval, best_move

    def Utility(self, board):
        num_black = sum(row.count('B') for row in board)
        num_white = sum(row.count('W') for row in board)
        return num_black - num_white if self.color == 'B' else num_white - num_black

    def is_game_over(self, board):
        return len(self.get_valid_moves(board, 'B')) == 0 and len(self.get_valid_moves(board, 'W')) == 0

    def get_valid_moves(self, board, color):
        self.findValidMoves

    def make_move_on_board(self, board, move, color):
        self.make_move
        
    
    def choose_difficulty_level(self):
        print("Choose difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            self.dificulltyLevel = 0
        elif choice == '2':
            self.dificulltyLevel =  1
        elif choice == '3':
            self.dificulltyLevel = 3
        else:
            print("Invalid choice. Defaulting to medium.")
            self.dificulltyLevel = 1