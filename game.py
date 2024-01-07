from block import *

class Game:
    def __init__(self):
        # Setup window size based on SCALE value.
        turtle.setup(SCALE * 12 + 20, SCALE * 22 + 20)

        # Bottom left corner of screen is (-1.5,-1.5)
        # Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        # Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        # Draw rectangular play area, height 20, width 10
        turtle.bgcolor("black")
        turtle.pencolor("white")
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)

        self.active = Block()
        self.occupied = []
        turtle.ontimer(self.game_loop, 300)

        # bindings
        turtle.onkeypress(self.move_left, "Left")
        turtle.onkeypress(self.move_right, "Right")
        turtle.onkeypress(self.drop, "Down")
        ##        turtle.onkeypress(self.rotate, 'space')

        # These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()

    def game_loop(self):
        if self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
        else:
            for square in self.active.squares:
                self.occupied.append((square.xcor(), square.ycor()))
            self.active = Block()

        turtle.update()
        turtle.ontimer(self.game_loop, 300)

    def move_left(self):
        if self.active.valid(-1, 0, self.occupied):
            self.active.move(-1, 0)
        turtle.update()

    def move_right(self):
        if self.active.valid(1, 0, self.occupied):
            self.active.move(1, 0)
        turtle.update()

    def drop(self):
        while self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
        turtle.update()

    # TODO: Implement rotation feature
    # def rotate(self):
