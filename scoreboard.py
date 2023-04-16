
from turtle import Turtle
ALIGN='center'
FONT=('Courier', 18, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pencolor("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGN, font=FONT)

    # def detect_collision(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()



