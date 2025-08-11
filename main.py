from turtle import Turtle , Screen
from food import Food
from snake import Snake
from score_board import Scr_Board
import time

screen =Screen()


screen.bgcolor("black")
screen.screensize(650,650)
screen.title("Friends Game ")
screen.tracer(0)# turned offf the tracer 


tim_the_snake=Snake()
food=Food()
score=Scr_Board()

screen.listen()
screen.onkey(tim_the_snake.up,"Up")
screen.onkey(tim_the_snake.down,"Down")
screen.onkey(tim_the_snake.right,"Right")
screen.onkey(tim_the_snake.left,"Left")
with open("txt_storage",mode='a') as file:
    file.write("ganpati Bappa")
is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    tim_the_snake.move()

    if tim_the_snake.head.distance(food) < 15 :
        food.refresh()
        # body bi vadvyche
        tim_the_snake.extend()
        # etha call hoel score board update
        score.increase_score()
    # Check for self-collision

    # Check for wall collision
    if (tim_the_snake.head.xcor() > 350 or 
        tim_the_snake.head.xcor() < -350 or 
        tim_the_snake.head.ycor() > 350 or 
        tim_the_snake.head.ycor() <-350):
        # is_game_on = False
        tim_the_snake.reset()
        score.resetSc()

    for segment in tim_the_snake.turtles:
        if segment== tim_the_snake.head:
            continue
        if tim_the_snake.head.distance(segment) < 5:
            score.resetSc()
            tim_the_snake.reset()
            # is_game_on = False


screen.exitonclick()