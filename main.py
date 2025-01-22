from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.goUp, "Up")
screen.onkey(r_paddle.goDown, "Down")

screen.onkey(l_paddle.goUp, "w")
screen.onkey(l_paddle.goDown, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()















screen.exitonclick()