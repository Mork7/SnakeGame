from turtle import Screen
from snake import Snake
from food import Food
from game_timer import GameTimer
from scoreboard import Scoreboard, ALIGNMENT, FONT
import time
import os
import pygame


#declare constants
GAMEOVER = os.path.join("SnakeGame", "GameSounds", "game_over.wav")
FOODSOUND = os.path.join("SnakeGame", "GameSounds", "food_sound.wav")

#intialize pygame.mixer and load up game sounds 
pygame.mixer.init()
game_over_sound = pygame.mixer.Sound(GAMEOVER)
food_sound = pygame.mixer.Sound(FOODSOUND)

#set up screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#create objects
snake = Snake()
food = Food()
score = Scoreboard()
game_timer = GameTimer()

#listen for keystrokes 
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#start the timer
start_time = time.time()


#the game loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    current_time = time.time()

    snake.move()

    #detect collision with food
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.extend()
        food_sound.play()
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
    
    #update timer as game isn't over
    elapsed_time = int(current_time - start_time)
    game_timer.update_timer(elapsed_time)
    
    #stop game loop if game is over
    if game_is_on == False:
        game_over_sound.play()

screen.exitonclick()