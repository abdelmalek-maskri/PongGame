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

    # Detect collision with wall
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()
    
    if(ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if(ball.xcor() > 380):
        ball.reset_position()
    
    if(ball.xcor() < -380):
        ball.reset_position()`














screen.exitonclick()