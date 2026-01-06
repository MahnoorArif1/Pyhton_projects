from turtle import Turtle
class Bridge:
    def __init__(self):
        bridge=Turtle()
        bridge.hideturtle()
        bridge.speed("fastest")
        bridge.color("white")
        bridge.penup()
        bridge.goto(0,400)
        bridge.pendown()
        bridge.left(270)
        for i in range(20):
            bridge.pendown()
            bridge.forward(20)
            bridge.penup()
            bridge.forward(20)