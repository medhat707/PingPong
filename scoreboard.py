from turtle import  Turtle

class Scoreboard(Turtle):
    #inherits from turtle class
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle() #turtle hidden
        self.lscore=0
        self.rscore=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(self.lscore, align="center" , font=("Courier" , 80 , "normal"))
        self.goto(100,200)
        self.write(self.rscore, align="center" , font=("Courier" , 80 , "normal"))


    def l_points(self):
        self.lscore+=1
        self.clear()
        self.update_scoreboard()

    def r_points(self):
        self.rscore+=1
        self.clear()
        self.update_scoreboard()