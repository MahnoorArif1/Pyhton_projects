from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-260,250)
        self.update_score()
    def cal_score(self):
        self.level+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f" Game Over ",False,"center",FONT)
    def game_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"You Win  ",False,"center",FONT)
    def update_score(self):
        self.write(f"LEVEL :{self.level} ",False,"left",FONT)






