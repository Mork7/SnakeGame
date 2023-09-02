from turtle import Turtle

TIMERFONT = ("Courier",16,"normal")

class GameTimer(Turtle):

    def __init__(self) -> None:
        self.timer = Turtle()
        self.timer.penup()  # Lift the pen to prevent drawing lines
        self.timer.goto(0,-300)  # Set the initial position
        self.timer.color("white")
        self.timer.hideturtle()

    def update_timer(self,time):
        self.timer.clear()
        if time == 1:
            self.timer.write(f"Time: {time} second", align="center", font=TIMERFONT)
        else:
            self.timer.write(f"Time: {time} seconds", align="center", font=TIMERFONT)
