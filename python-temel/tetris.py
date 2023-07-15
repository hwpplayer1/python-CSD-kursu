class Shape:
    pass

class SquareShape(Shape):
    def move_down(self):
        print('SquareShape moves down')

class BarShape(Shape):
    def move_down(self):
        print('BarShape moves down')

class TShape(Shape):
    def move_down(self):
        print('TShape moves down')

class LShape(Shape):
    def move_down(self):
        print('LShape moves down')

class ZShape(Shape):
    def move_down(self):
        print('ZShape moves down')

import random
import time

class Tetris:
    def get_random_shape(self):
        return random.choice([ZShape, TShape, SquareShape, BarShape, LShape])()

    def run(self):
        while True:
            shape = self.get_random_shape()
            for i in range(20):
                shape.move_down()
                time.sleep(0.5)

tetris = Tetris()
tetris.run()
