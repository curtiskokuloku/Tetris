import random
from square import *
from tetronimos import *

class Block:
    def __init__(self):
        coords, color = random.choice([LINE, BLUEL, ORANGEL, BOX, ESS, TEE, ZEE])
        self.squares = []
        for coord in coords:
            self.squares.append(Square(coord[0], coord[1], color))

    def move(self, dx, dy):
        for square in self.squares:
            new_x = square.xcor() + dx
            new_y = square.ycor() + dy
            square.goto(new_x, new_y)

    def valid(self, dx, dy, occupied):
        for square in self.squares:
            new_x = square.xcor() + dx
            new_y = square.ycor() + dy
            if not (0 <= new_x <= 9 and 0 <= new_y):
                return False
            if (new_x, new_y) in occupied:
                return False
        return True
