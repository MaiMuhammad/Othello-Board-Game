import copy
class Player:
    def __init__(self, color):
        self.color = color

    def findValidMoves(self, board):
        valid_moves = []
        for x in range(8):
            for y in range(8):
                if board[x][y] == " ":
                    if self.findValidMovesX(x, y, board) or self.findValidMovesY(x, y,
                                                                                 board) or self.findValidMovesDiagonal(
                            x, y, board):
                        valid_moves.append((x, y))

        return valid_moves

    def findValidMovesX(self,x, y, board):
        if x + 1 < 8 and board[x + 1][y] == "W":
            for x1 in range(x + 2, 8):
                if board[x1][y] == "W":
                    continue
                if board[x1][y] == " ":
                    break
                if board[x1][y] == "B":
                    return True
        elif x - 1 > 0 and board[x - 1][y] == "W":
            for x1 in range(x - 2, -1, -1):
                if board[x1][y] == "W":
                    continue
                if board[x1][y] == " ":
                    break
                if board[x1][y] == "B":
                    return True
        return False

    def findValidMovesY(self, x, y, board):
        if y + 1 < 8 and board[x][y + 1] == "W":
            for y1 in range(y + 2, 8):
                if board[x][y1] == "W":
                    continue
                if board[x][y1] == " ":
                    break
                if board[x][y1] == "B":
                    return True
        elif y - 1 > 0 and board[x][y - 1] == "W":
            for y1 in range(y - 2, -1, -1):
                if board[x][y1] == "W":
                    continue
                if board[x][y1] == " ":
                    break
                if board[x][y1] == "B":
                    return True
        return False

    def findValidMovesDiagonal(self, x, y, board):
        if y + 1 < 8 and x + 1 < 8 and board[x + 1][y + 1] == "W":
            for x1, y1 in zip(range(x + 2, 8), range(y + 2, 8)):
                if board[x1][y1] == "W":
                    continue
                if board[x1][y1] == " ":
                    break
                if board[x1][y1] == "B":
                    return True
        elif y - 1 > 0 and x - 1 > 0 and board[x - 1][y - 1] == "B":
            for x1, y1 in zip(range(x - 2, -1, -1), range(y - 2, -1, -1)):
                if board[x1][y1] == "W":
                    continue
                if board[x1][y1] == " ":
                    break
                if board[x1][y1] == "B":
                    return True
        elif y - 1 > 0 and x + 1 < 8 and board[x + 1][y - 1] == "W":
            for x1, y1 in zip(range(x + 2, 8), range(y - 2, -1, -1)):
                if board[x1][y1] == "W":
                    continue
                if board[x1][y1] == " ":
                    break
                if board[x1][y1] == "B":
                    return True
        elif y + 1 < 8 and x - 1 > 0 and board[x - 1][y + 1] == "W":
            for x1, y1 in zip(range(x - 2, -1, -1), range(y + 2, 8)):
                if board[x1][y1] == "W":
                    continue
                if board[x1][y1] == " ":
                    break
                if board[x1][y1] == "B":
                    return True
        return False

    def has_valid_move(self, board):
        for row in range(8):
            for col in range(8):
                if board.is_valid_move(row, col, self.color):
                    return True

        return False

    def count_score(self, board):
        score = sum(row.count(str(self.color)) for row in board)
        return score
