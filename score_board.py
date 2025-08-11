from turtle import Turtle
import random

class Scr_Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0,290)      
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"score : {self.score} High score : {self.highscore}", align="center", font=('Arial',20,'normal'))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"score : {self.score} High score : {self.highscore}", align="center", font=('Arial',20,'normal'))
        # self.write(f"score = {self.score}",align="center", font=('Arial',20, 'normal'))

    def score_war(self):
        self. goto(0,0)
        self.write(f"Game Over",align="center", font=('Arial',20, 'normal'))
        # self.write(f"score : {self.score} High score :{self.highscore}", align="center", font=('Arial',20,'normal'))

    def resetSc(self):
        
        self.highscore=max(self.score,self.highscore)
        self.score=0
        self.update_score()