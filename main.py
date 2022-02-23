from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

snek = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snek.move()

screen.exitonclick()
