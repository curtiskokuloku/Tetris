from block import *


class Game:
    def __init__(self):
        """
        Initialize the game environment, setup Turtle graphics, and initialize game components.
        """
        self.set_up()  # Setup Turtle environment and window
        self.draw_play_area()  # Draw the game play area

        # Initialize game components
        self.active = Block()
        self.score = 0
        self.occupied = [[False for _ in range(10)] for _ in range(20)]

        # Start the game loop
        turtle.ontimer(self.game_loop, 300)  # Set up the game loop with a delay
        turtle.listen()  # Allow Turtle to listen for events

        # Keep the game running
        turtle.mainloop()


    def set_up(self):
        """
        Set up the Turtle graphics window with appropriate configurations.
        """
        turtle.setup(SCALE * 12 + 20, SCALE * 22 + 20)  # Set window dimensions
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)  # Set coordinate system
        cv = turtle.getcanvas()  # Get the canvas for further adjustments
        cv.adjustScrolls()  # Adjust canvas settings

        turtle.hideturtle()  # Hide the Turtle cursor
        turtle.delay(0)  # Set the delay to 0 for maximum speed
        turtle.speed(0)  # Set the animation speed to 0 (fastest)
        turtle.tracer(0, 0)  # Turn off automatic screen updates


    def draw_play_area(self):
        """
        Draw the rectangular play area with specified dimensions (height: 20, width: 10).
        """
        turtle.bgcolor("black")
        turtle.pencolor("white")
        turtle.penup()
        turtle.setpos(-0.525, -0.525)  # Start drawing from the bottom left corner
        turtle.pendown()

        # Draw the play area boundary
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)


    def move_left(self):
        """
        Move the active block one unit to the left if the movement is valid.
        """
        if self.active.valid(-1, 0, self.occupied):
            self.active.move(-1, 0)
            turtle.update()


    def move_right(self):
        """
        Move the active block one unit to the right if the movement is valid.
        """
        if self.active.valid(1, 0, self.occupied):
            self.active.move(1, 0)
            turtle.update()


    def drop(self):
        """
        Move the active block down until it reaches an occupied position or the bottom boundary.
        """
        while self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
        turtle.update()


    def rotate(self):
        """
        Rotate the active block clockwise by 90 degrees if the rotation is valid.
        """
        # Get the center square (index 1) for rotation
        center_square = self.active.squares[1]
        center_x, center_y = center_square.xcor(), center_square.ycor()

        # Calculate new positions for each square relative to the center square
        new_positions = [
            (
                center_x + (square.ycor() - center_y),
                center_y - (square.xcor() - center_x),
            )
            for square in self.active.squares
        ]

        # Check if all new positions are within the game boundaries
        if all(0 <= new_x <= 9 and new_y >= 0 for new_x, new_y in new_positions):
            # Update positions for each square
            for square, (new_x, new_y) in zip(self.active.squares, new_positions):
                square.goto(new_x, new_y)

            # Update the screen
            turtle.update()
            return True  # Return True if rotation is successful

        return False  # Return False if rotation is not valid


    def display_score(self):
        """
        Display the score at the top of the window.
        """
        turtle.undo()
        turtle.pencolor("white")
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(6.5, 19.75)
        turtle.pendown()
        turtle.write(f"Score: {self.score}", font=("Arial", 16, "bold"))


    def display_game_over(self):
        """
        Display game over message to user.
        """
        self.score = 0  # Reset score

        turtle.pencolor("red")
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(0.5, 10)
        turtle.pendown()
        turtle.write("Game Over!", font=("Arial", 36, "bold"))
        turtle.penup()
        turtle.goto(2, 9)
        turtle.pendown()
        turtle.write(f"You scored: {self.score}", font=("Arial", 18, "bold"))


    def get_key_bindings(self):
        """
        Set up event bindings for user interactions.
        """
        turtle.onkeypress(self.move_left, "Left")
        turtle.onkeypress(self.move_right, "Right")
        turtle.onkeypress(self.drop, "Down")
        turtle.onkeypress(self.rotate, "Up")
        turtle.onkeypress(self.exit, "q")


    def disable_keys(self):
        """
        Disable key bindings to prevent further user inputs during specific game states.
        """
        turtle.onkeypress(None, "Left")
        turtle.onkeypress(None, "Right")
        turtle.onkeypress(None, "Down")
        turtle.onkeypress(None, "Up")


    def eliminate_and_update(self):
        """
        Check for any completed rows and update the game grid accordingly.
        """
        # List to store indices of rows that need to move down
        rows_to_move = []

        # Loop through the grid backwards to check for completed rows
        for i in range(len(self.occupied) - 1, -1, -1):
            if all(self.occupied[i]):
                # Remove and hide squares from the completed row
                for j in range(len(self.occupied[i])):
                    if self.occupied[i][j]:
                        self.occupied[i][j].hideturtle()  # Hide the turtle object
                        self.occupied[i][j] = False  # Remove the object from the grid

                rows_to_move.append(i)

        # Move down the rows above the eliminated ones
        for i in rows_to_move:
            for j in range(i, len(self.occupied) - 1):
                for k in range(len(self.occupied[j])):
                    if self.occupied[j + 1][k]:
                        x, y = (
                            self.occupied[j + 1][k].xcor(),
                            self.occupied[j + 1][k].ycor() - 1,
                        )
                        self.occupied[j + 1][k].goto(x, y)
                        self.occupied[j][k] = self.occupied[j + 1][k]
                        self.occupied[j + 1][k] = False

        turtle.update()


    def is_valid_move(self):
        """
        Check if the current move by the active block is valid within the game grid.
        """
        self.eliminate_and_update()  # Check for any completed rows

        # Check if the active block can move down or needs to be placed
        if self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
            turtle.update()
        else:
            # If the block cannot move down, place it in the grid and spawn a new block
            self.score += 2  # Increase the score
            for square in self.active.squares:
                x, y = int(square.xcor()), int(square.ycor())
                if y >= 19:
                    # Block reaches the top
                    return False
                elif x >= 0 and x <= 9:
                    # Place the block in the grid
                    self.occupied[y][x] = square
            self.active = Block()  # Spawn a new block

        return True


    def game_loop(self):
        """
        Main game loop that updates the active block's position and manages block placement.
        """
        if self.is_valid_move():
            self.get_key_bindings()
            self.display_score()
            turtle.ontimer(self.game_loop, 300)
        else:
            self.disable_keys()
            self.display_score()
            self.display_game_over()


    def exit(self):
        """
        Close the Turtle graphics window to stop the game
        """
        turtle.bye()
