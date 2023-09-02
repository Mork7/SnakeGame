from turtle import Turtle

#delcare constants
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
#setting headings in degrees for movement
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    #creating a snake using a list of segments, the head will be the first index of segment
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    #create three piece snake at starting positions
    def create_snake(self):

        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    #adding a segment to the snake if food is eaten, create new turtle object and append it to the snake. The position will be the position returned by TurtleObj.position(), in this case the last segment of the snake
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #add segment to extend the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    #moving the snake, starting from the tail end
    def move(self):

        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    

    #setting headings as long as snake isn't being moved in a 180 degree motion
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