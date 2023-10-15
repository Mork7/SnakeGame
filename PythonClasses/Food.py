from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    #create a new food object at random positions within margins (560,560) of the (600,600) screen to avoid collisions with walls 
    def refresh(self):
        random_x = random.randint(-275,275)
        random_y = random.randint(-275,275)
        self.goto(random_x,random_y)