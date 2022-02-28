from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up turtle screen 600x600px
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")

# Turn off automatic screen update to smooth out snake movements.
screen.tracer(0)

snek = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up event listener and assign key strokes to movement functions.
screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

# Initialize main game loop.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # Detect collisions with food
    if snek.head.distance(food) < 15:
        scoreboard.increase_score()
        snek.extend()
        food.refresh()

    # Detect collisions with walls
    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snek.segments[2:]:
        if snek.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
