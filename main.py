from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

initial_x = 0

segments = []

for _ in range(3):
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.setx(initial_x)
    segments.append(new_segment)
    initial_x -= 20


game_on = True
while game_on:
    screen.update()
    time.sleep(1)

    for seg_num in range(len(segments)-1,0,-1):
        new_pos = segments[seg_num-1].pos()
        segments[seg_num].goto(new_pos)

screen.exitonclick()
