#imports 
from turtle import Screen
from PythonClasses.Snake import Snake
from PythonClasses.Food import Food
from PythonClasses.GameTimer import GameTimer
from PythonClasses.Scoreboard import Scoreboard, ALIGNMENT, FONT
from colorama import Fore, Style, init
import time
import os
import pygame

# Initialize colorama
init(autoreset=True)

#declare constants and create paths independent of os
GAMEOVER = os.path.join("GameSounds", "game_over.wav")
FOODSOUND = os.path.join("GameSounds", "food_sound.wav")

#intialize pygame.mixer and load up game sounds 
pygame.mixer.init()
game_over_sound = pygame.mixer.Sound(GAMEOVER)
food_sound = pygame.mixer.Sound(FOODSOUND)

#This takes input from user and set a difficulty, the lower the sleep time the faster the snake moves
def set_difficulty():

    print(Fore.GREEN + "easy" + ", " + Fore.YELLOW + "med" + ", "  + Fore.RED +" hard")
    choice = input("Choose a difficulty: ")
    Style.RESET_ALL
    
    if choice == "easy":
        return 0.1
    elif choice == "medium":
        return 0.07
    elif choice == "hard":
        return 0.05 
    else:
        # Handle invalid input (e.g., user entered something other than 'easy', 'medium', or 'hard')
        print("Invalid choice. Defaulting to medium difficulty.")
        return 0.07

#set difficulty before screen is created
difficulty = set_difficulty()

#set up screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(10)

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
    time.sleep(difficulty)
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