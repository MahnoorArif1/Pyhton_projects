from turtle import Turtle
import time
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.clear()
        self.score=0
        self.highscore=0
        self.goto(0,280)
        self.color("White")
        self.update_score()
    def update_score(self):
        file=open("data.txt")
        self.write(f"SCORE: {self.score}    HIGH SCORE: {file.read()}",align="center",font=("Courier",14,"normal"))
        file.close()
    def game_reset(self):
        file=open("data.txt","r")
        self.clear()
        self.goto(0,0)
        scor=file.read()
        scort=int(scor)
        if self.score > scort:
            self.highscore=str(self.score)
            self.score=0
            file.close()
            file=open("data.txt","w")
            file.write(self.highscore)
        file.close()

    def ref(self):
        file=open("data.txt")
        self.clear()
        self.goto(0, 280)
        self.score = 0
        self.write(f"SCORE: {self.score}    HIGH SCORE: {file.read()}",align="center",font=("Courier",14,"normal"))
        file.close()
    def cal_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over_text(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER\nPress SPACE to Continue",
                   align="center",
                   font=("Courier", 18, "bold"))
        self.time.sleep(10000)
