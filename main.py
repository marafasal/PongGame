import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.tracer(0)



paddler=Paddle((350,0))
paddlel=Paddle((-350,0))

ball=Ball()
screen.listen()
screen.onkey(paddler.go_up,"Up")
screen.onkey(paddler.go_down,"Down")
screen.onkey(paddlel.go_up,"w")
screen.onkey(paddlel.go_down,"s")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect collision with the vertical wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    #detect collision with the paddles
    if ball.distance(paddler)<50 or ball.xcor()>320 and ball.distance(paddlel)<50 or ball.xcor()<-320:
        ball.bounce_x()




screen.exitonclick()
