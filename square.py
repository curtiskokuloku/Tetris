import turtle

# Define the scale for each grid square (number of pixels)
SCALE = 32


class Square(turtle.Turtle):
    """
    Represents a single grid square using Turtle graphics.

    Attributes:
    - x, y (int): Coordinates of the square.
    - color (str): Color of the square.
    """

    def __init__(self, x, y, color):
        """
        Initialize the Square with its position and color.

        :param x: x-coordinate position.
        :param y: y-coordinate position.
        :param color: Color of the square.
        """
        # Initialize the Turtle object
        super().__init__()

        # Set the shape to a square
        self.shape("square")

        # Adjust the size of the square based on the SCALE
        self.shapesize(SCALE / 20)

        # Set the animation speed to 0 (fastest)
        self.speed(0)

        # Set the color of the square
        self.fillcolor(color)

        # Set the pen color (border color) of the square to gray
        self.pencolor("gray")

        # Lift the pen to avoid drawing lines while moving
        self.penup()

        # Move the turtle to the specified x, y coordinates
        self.goto(x, y)
