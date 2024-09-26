from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore = 0
        self.rscore = 0

        self.show_score()
    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, font=("Arial", 50, "normal"))

    def up_lscore(self):
        self.lscore +=1
        self.show_score()
    def up_rscore(self):
        self.rscore +=1
        self.show_score()






