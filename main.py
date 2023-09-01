from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, ALIGNMENT, FONT
from playsound import playsound

import time

FOODSOUND = "GameSounds/food_sound.wav"
GAMEOVER = "GameSounds/game_over.wav"

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.extend()
        playsound(FOODSOUND, False)
        score.increase_score()
    
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False
    
    #detect collision with tail
    for seg in snake.segments:
        if seg == snake.head:
            continue
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_is_on = False
    
    if game_is_on == False:
        playsound(GAMEOVER, False)

screen.exitonclick()