class Piece:
    def __init__(self, color):
        self.color = color

    def flip(self):
        self.color = 'B' if self.color == 'W' else 'W'
