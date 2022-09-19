from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.hight_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Hight score {self.hight_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.hight_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()







