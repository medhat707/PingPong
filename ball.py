
from turtle import Turtle

# methods run in the main() don't need to be introduced inside the class e.g. refresh and bounce_y_y

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmov = 10
        self.ymov = 10
        self.mov_speed = 0.1 #defining a speed var

    def refresh(self):
        new_x= self.xcor() + self.xmov
        new_y=self.ycor() + self.ymov
        self.goto(new_x,new_y)


    def bounce_y(self):
        # if ball bounces with wall then y dir changes to -ve by changing the self.ymov
        self.ymov *= -1

    def bounce_x(self):
        # if ball bounces with paddles then x dir changes to -ve by changing the self.xmov
        self.xmov *= -1
        self.mov_speed*=0.9 #speed inc as soon as it touches the paddle

    def reset_position(self):
        self.goto(0,0)
        self.mov_speed=0.1
        self.bounce_x()

    # def go_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)
    #
    # def go_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)
