class Figure:
    def __init__(self, ftype, color):
        self.ftype = ftype
        self.color = color

class Square:
    def __init__(self, color):
        self.color = color
        self.figure = None

    def set_figure(self, figure):
        self.figure = figure

    def get_figure(self):
        return self.figure

class Board:
    def __init__(self):
        self.squares = [[Square('Beyaz' if (i + k) % 2 == 0 else 'Siyah' ) for i in range(8)] for k in range(8)]
        self.squares[0][0].figure = Figure('Kale', 'Siyah')
        self.squares[0][1].figure = Figure('At', 'Siyah')
        # ....

board = Board()
#print(board)
