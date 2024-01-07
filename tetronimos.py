class Tetronimo:
    """
    Base class for Tetronimos. Represents a generic Tetronimo shape.
    """

    def __init__(self, coordinates, color):
        """
        Initialize a Tetronimo with its coordinates and color.

        :param coordinates: List of coordinate tuples representing the blocks of the Tetronimo.
        :param color: Color of the Tetronimo.
        """
        self.coordinates = coordinates
        self.color = color


class Line(Tetronimo):
    """
    Class representing the Line-shaped Tetronimo.
    """

    def __init__(self):
        """
        Initialize the Line-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(3, 21), (4, 21), (5, 21), (6, 21)], "cyan")


class BlueL(Tetronimo):
    """
    Class representing the L-shaped Tetronimo with blue color.
    """

    def __init__(self):
        """
        Initialize the L-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(4, 22), (4, 21), (5, 21), (6, 21)], "blue")


class OrangeL(Tetronimo):
    """
    Class representing the L-shaped Tetronimo with orange color.
    """

    def __init__(self):
        """
        Initialize the L-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(6, 22), (4, 21), (5, 21), (6, 21)], "orange")


class Box(Tetronimo):
    """
    Class representing the Box-shaped Tetronimo.
    """

    def __init__(self):
        """
        Initialize the Box-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(4, 22), (4, 21), (5, 21), (5, 22)], "yellow")


class Ess(Tetronimo):
    """
    Class representing the Ess-shaped Tetronimo.
    """

    def __init__(self):
        """
        Initialize the Ess-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(4, 21), (5, 21), (5, 22), (6, 22)], "green")


class Tee(Tetronimo):
    """
    Class representing the Tee-shaped Tetronimo.
    """

    def __init__(self):
        """
        Initialize the Tee-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(5, 22), (4, 21), (5, 21), (6, 21)], "purple")


class Zee(Tetronimo):
    """
    Class representing the Zee-shaped Tetronimo.
    """

    def __init__(self):
        """
        Initialize the Zee-shaped Tetronimo with its default coordinates and color.
        """
        super().__init__([(4, 22), (5, 21), (5, 22), (6, 21)], "red")


# Instantiate Tetronimo classes to create Tetronimo objects.
LINE = Line()
BLUEL = BlueL()
ORANGEL = OrangeL()
BOX = Box()
ESS = Ess()
TEE = Tee()
ZEE = Zee()

# List of instantiated Tetronimo objects for easy access in the game.
TETRONIMOS = [LINE, BLUEL, ORANGEL, BOX, ESS, TEE, ZEE]
