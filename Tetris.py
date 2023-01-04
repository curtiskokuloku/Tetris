import turtle, random

SCALE = 32 #Controls how many pixels wide each grid square is

#Define the Tetronimos
LINE = [(3,21), (4,21), (5,21), (6,21)], 'cyan'
BLUEL = [(4,22), (4,21), (5,21), (6,21)], 'blue'
ORANGEL = [(6,22), (4,21), (5,21), (6,21)], 'orange'
BOX = [(4,22), (4,21), (5,21), (5,22)], 'yellow'
ESS = [(4,21), (5,21), (5,22), (6,22)], 'green'
TEE = [(5,22), (4,21), (5,21), (6,21)], 'purple'
ZEE = [(4,22), (5,21), (5,22), (6,21)], 'red'

class Game:
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
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
        turtle.ontimer(self.gameloop, 300)

        #bindings
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.drop, 'Down')
##        turtle.onkeypress(self.rotate, 'space')

        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.active.valid(0,-1, self.occupied):
            self.active.move(0,-1)
        else:
            for square in self.active.squares:
                self.occupied.append((square.xcor(), square.ycor()))
            self.active = Block()
            
        turtle.update()
        turtle.ontimer(self.gameloop, 300)
    
    def move_left(self):
        if self.active.valid(-1,0, self.occupied):
            self.active.move(-1, 0)
        turtle.update()
        
    def move_right(self):
        if self.active.valid(1, 0, self.occupied):
            self.active.move(1, 0)
        turtle.update()

    def drop(self):
        while self.active.valid(0,-1, self.occupied):
            self.active.move(0, -1)
        turtle.update()

##    def rotate(self):
##        self.active.rotate()
##        turtle.update


class Square(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
        self.goto(x,y)

                
class Block:
    def __init__(self):
        coords, color = random.choice([LINE,BLUEL,ORANGEL,BOX,ESS,TEE,ZEE])
        self.squares = []
        for coord in coords:
            self.squares.append(Square(coord[0],coord[1], color))

    def move(self, dx, dy):
        for square in self.squares:
            new_x = square.xcor() + dx
            new_y = square.ycor() + dy
            square.goto(new_x, new_y)

    def valid(self, dx, dy, occupied):
        for square in self.squares:
            new_x = square.xcor() + dx
            new_y = square.ycor() + dy
            if not (0 <= new_x <=9 and 0 <= new_y):
                return False
            if (new_x, new_y) in occupied:
                return False
        return True

##    def rotate(self):
##        if self.squares[0].fillcolor() == 'cyan':
##            self.squares[0].goto(self.squares[0].xcor(), self.squares[0].
##        coords = []
##        center_x = 0
##        center_y = 0
##        for square in self.squares:
##            coords.append(np.array([[square.xcor()], [square.ycor()]]))
##            center_x += square.xcor()
##            center_y += square.ycor()
##        center = np.array([[center_x/4], [center_y/4]])
##        for i, coord in enumerate(coords):
##            coords[i] = np.array([[0, 1],[-1,0]])*(coord - center) + center
##            self.squares[i].goto(coords[i][0][0], coords[i][1][0])

if __name__ == '__main__':
    Game()
