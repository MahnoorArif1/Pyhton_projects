import turtle
from turtle import Turtle

import paddle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_t=5
        self.y_t=5

    def move(self):
        x=self.xcor()+self.x_t
        y=self.ycor()+self.y_t
        self.goto(x,y)
    def detect_collision(self):
        y=self.ycor()
        if y>=290.0 :
            return "t"
        elif y<=-290.0 :
            return "t2"
        else:
            return "m"
    def bounce(self):
        self.y_t = - 5
    def bounce_in(self):
        self.x_t = - 5
    def bounce_up(self):
        self.y_t=5
        self.x_t=-5
    def bounce_out(self):
        self.x_t=5
        self.y_t=5
    def restart(self):
        self.goto(0,0)
        self.bounce_in()
        self.move()

