from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        y=self.ycor()+MOVE_DISTANCE
        x=self.xcor()
        self.goto(x,y)

    def down(self):
        y = self.ycor() - MOVE_DISTANCE
        x = self.xcor()
        self.goto(x, y)

    def m_left(self):
        y = self.ycor()
        x = self.xcor()-MOVE_DISTANCE
        self.goto(x, y)

    def m_right(self):
        y = self.ycor()
        x = self.xcor()+MOVE_DISTANCE
        self.goto(x, y)


