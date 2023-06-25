class Square:
    pass

class Board:
    def __init__(self):
        self.squares = [[Square()] * 8 for i in range(8)]
        
board = Board()
print(board)

