from turtle import Turtle

PACE = 20
DIRECTIONS = {
    "RIGHT": 0,
    "UP": 90,
    "LEFT": 180,
    "DOWN": 270,
}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        initial_x = 0
        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(initial_x)
            self.segments.append(new_segment)
            initial_x -= PACE

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(PACE)

    def _turn(self, direction):
        self.segments[0].setheading(DIRECTIONS[direction])

    def up(self):
        self._turn("UP")

    def down(self):
        self._turn("DOWN")

    def left(self):
        self._turn("LEFT")

    def right(self):
        self._turn("RIGHT")