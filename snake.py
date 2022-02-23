from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        initial_x = 0

        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(initial_x)
            self.segments.append(new_segment)
            initial_x -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(20)
