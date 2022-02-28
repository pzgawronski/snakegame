from turtle import Screen
from snake import Snake
from food import Food
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

    # Detect collisions
    if snek.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
