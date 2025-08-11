from turtle import Turtle

# turtles=[]
positions=[(-40,0),(-29,0),(0,0)]
move=20

up =90
down=270
right=0
left=180
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        # hyo spancha head
        self.head=self.turtles[0]

    def create_snake(self):
        for position in positions:
            self.add_body(position)

    def add_body(self,position):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.turtles.append(segment)



    def move(self):
        # hai apan maghana (tail) pasun cha;u kartoy so 
        for curr_tur in range(len(self.turtles)-1,0,-1):
            x_cor=self.turtles[curr_tur-1].xcor()
            y_cor=self.turtles[curr_tur-1].ycor()
            # mnje etha current turtle(tail body)la tya pudchya bodya pashi takla 
            self.turtles[curr_tur].goto(x_cor,y_cor)
        self.head.forward(move)
        # the size of the body part is 20 x 20
    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head=self.turtles[0]


    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
        
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
        
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
        
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
        
    def extend(self):
        self.add_body(self.turtles[-1].position())