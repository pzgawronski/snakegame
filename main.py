from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

snek = Snake()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

screen.exitonclick()
