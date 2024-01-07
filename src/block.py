import random
from square import Square, turtle, SCALE
from tetronimos import TETRONIMOS


class Block:
    """
    Represents a block in the Tetris game, composed of multiple squares (Tetronimo).
    """

    def __init__(self):
        """
        Initialize a Block by selecting a random Tetronimo and creating squares based on its coordinates.
        """
        # Select a random Tetronimo object from the list of instantiated Tetronimos.
        tetronimo = random.choice(TETRONIMOS)

        # Access the coordinates and color of the selected Tetronimo.
        coords = tetronimo.coordinates
        color = tetronimo.color

        # Create squares based on the Tetronimo's coordinates and color.
        self.squares = []
        for coord in coords:
            self.squares.append(Square(coord[0], coord[1], color))

    def move(self, dx, dy):
        """
        Move the Block by a given displacement (dx, dy).

        :param dx: Displacement in the new_x-direction.
        :param dy: Displacement in the new_y-direction.
        """
        for square in self.squares:
            new_x, new_y = square.xcor() + dx, square.ycor() + dy
            square.goto(new_x, new_y)

    def valid(self, dx, dy, occupied):
        """
        Check if moving the Block by a given displacement (dx, dy) is valid.

        :param dx: Displacement in the new_x-direction.
        :param dy: Displacement in the new_y-direction.
        :param occupied: List of occupied coordinates.
        :return: True if the move is valid, False otherwise.
        """
        for square in self.squares:
            new_x, new_y = square.xcor() + dx, square.ycor() + dy
            if (new_x < 0 or new_x > 9) or new_y < 0:
                return False
            elif new_y < 20 and occupied[new_y][new_x]:
                return False
        return True
