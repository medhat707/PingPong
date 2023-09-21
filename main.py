from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor("orange")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# collision with wall at x=0 and y=300

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreObj = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
game_is_on = True

# update the screen as soon as an action happens e.g. ball/paddle moves
while game_is_on:
    time.sleep(ball.mov_speed)
    screen.update()
    ball.refresh()

    # detecting ball collision
    if ball.ycor()> 300 or ball.ycor()<-300:
        # needs to bounce_y
        ball.bounce_y()
    # detecting collision with r_paddle using distance function [measures are from centers]
    if ball.distance(r_paddle) < 40 and ball.xcor()>320 :
        ball.bounce_x()
    elif ball.distance(l_paddle) < 40 and ball.xcor()<-320 :
        ball.bounce_x()

#l_paddle misses
    if ball.xcor()<-380:
        scoreObj.r_points()
        ball.reset_position()
# r_paddle misses
    if ball.xcor() > 380:
        scoreObj.l_points()
        ball.reset_position()










screen.exitonclick()
