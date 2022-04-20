from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        with open("data.txt", mode="r") as game_data:
            raw_data = game_data.read()
            conv_data = int(raw_data)
            self.high_score = conv_data
        self.pencolor("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as game_data:
                saved_score = str(self.high_score)
                game_data.write(saved_score)
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
