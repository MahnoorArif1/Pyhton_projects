import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
cars=[]
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
me=Player()
screen.listen()
screen.onkeypress(me.up,"Up")
screen.onkeypress(me.down,"Down")
screen.onkeypress(me.m_left,"Left")
screen.onkeypress(me.m_right,"Right")
sc=Scoreboard()
for i in range(1,20):
    c1=CarManager()
    cars.append(c1)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in cars:
        i.move()
        if me.distance(i)<20:
            sc.game_over()
            game_is_on = False
    if me.ycor()>250:
        me.goto(0,-280)
        sc.cal_score()
        for i in cars:
            i.lev_up()


screen.exitonclick()


