from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []#list of position of coordinates snake is moving to
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("dark goldenrod")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def snake_reset(self):
        if self.head.xcor() > 295 or self.head.xcor() < -295:
            self.head.goto(self.head.xcor()*-0.9322033898305085,self.head.ycor())
        elif self.head.ycor()>295 or self.head.ycor()<-295:
            self.head.goto(self.head.xcor(),self.head.ycor()*-0.9322033898305085)
    def new_snake(self):
            # Trim the snake to the specified length
            new_length=3
            while len(self.segments) > new_length:
                segment_to_remove = self.segments.pop()
                segment_to_remove.hideturtle()




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


