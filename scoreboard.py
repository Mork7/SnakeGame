from turtle import Turtle
from snake import Snake as snake

ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.refresh_score()
    
    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)