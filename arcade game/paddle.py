import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4,0.7)
        self.penup()
        self.goto(position)
        self.setposition(position)
    def up(self):
        x=self.xcor()
        y=self.ycor()
        if y<243:
            self.goto(x,y+20)
    def down(self):
        x=self.xcor()
        y=self.ycor()
        if y>-243:
            self.goto(x,y-20)






