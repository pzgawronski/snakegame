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
        self.head = self.segments[0]

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
        """
        Moves each segment of the snake to the position to the segment before it.
        Moves the head forward according to the current heading.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(PACE)

    def _turn(self, direction):
        """
        :param direction: Snake heading expressed as degrees
        counter-clockwise from west, retrieved from a dict
        stored in constants.
        """
        self.head.setheading(DIRECTIONS[direction])


    # Specific movement functions calling on the _turn function.
    #
    # Conditional expression added to prevent the snake
    # from going backwards on itself.
    def up(self):
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self._turn("UP")

    def down(self):
        if self.head.heading() != DIRECTIONS["UP"]:
            self._turn("DOWN")

    def left(self):
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self._turn("LEFT")

    def right(self):
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self._turn("RIGHT")