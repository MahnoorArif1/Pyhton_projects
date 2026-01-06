from turtle import Turtle

import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.movement=5
        self.shape("square")
        self.shapesize(2.5,1)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.left(90)
        self.move()

    def move(self):
        x1=self.xcor()
        if x1>280:
            x1=-280
        y = self.ycor()
        x2 =x1+self.movement
        self.goto(x2,y)
    def lev_up(self):
        self.movement+=MOVE_INCREMENT







