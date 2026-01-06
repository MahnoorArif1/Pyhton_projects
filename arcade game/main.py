import time
from bridge import Bridge
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

s=Screen()
s.bgcolor("black")
s.tracer(0)
s.setup(800,600)
b=Bridge()
p1_score=Score((200,280))
p2_score=Score((-200,280))
p1=Paddle((370,0))
p2=Paddle((-360,0))
s.listen()
s.onkeypress(p1.up,"Up")
s.onkeypress(p1.down,"Down")
s.onkeypress(p2.up,"d")
s.onkeypress(p2.down,"c")
p_ball=Ball()
Game_is_on=True
while Game_is_on:
    time.sleep(0.05)
    s.update()
    if p_ball.detect_collision()== "t":
        p_ball.bounce()
        p_ball.move()
    elif p_ball.detect_collision()== "t2":
        p_ball.bounce_up()
        p_ball.move()
    elif p_ball.distance(p1)<20 or (p_ball.distance(p1) < 50 and p_ball.xcor() >= 370):
        print("hit by the paddle")
        p1_score.cal_score()
        p_ball.bounce_in()
        p_ball.move()
    elif p_ball.distance(p2)<20 or (p_ball.distance(p2) < 50 and p_ball.xcor() <= -370):
        print("hit by the paddle")
        p2_score.cal_score()
        p_ball.bounce_out()
        p_ball.move()
    elif p_ball.xcor()>370:
        p2_score.cal_score()
        p_ball.restart()
    elif p_ball.xcor()<-370:
        p1_score.cal_score()
        p_ball.restart()
    else:
        p_ball.move()









s.exitonclick()
