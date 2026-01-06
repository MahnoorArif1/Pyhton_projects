from turtle import Turtle
class Score(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.clear()
        self.score=0
        self.goto(pos)
        self.color("White")
        self.update_score()
    def update_score(self):
        self.write(f"SCORE: {self.score}")
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ",align="center",font=("Courier",14,"normal"))



    def cal_score(self):
        self.score+=1
        self.clear()
        self.update_score()
