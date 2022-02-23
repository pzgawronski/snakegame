from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")

initial_x = 0
for _ in range(3):
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.setx(initial_x)
    initial_x -= 20

screen.exitonclick()
