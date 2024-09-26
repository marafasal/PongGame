import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.tracer(0)



paddler=Paddle((350,0))
paddlel=Paddle((-350,0))

ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(paddler.go_up,"Up")
screen.onkey(paddler.go_down,"Down")
screen.onkey(paddlel.go_up,"w")
screen.onkey(paddlel.go_down,"s")

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with the vertical wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    #detect collision with the paddles
    if ball.distance(paddler)<50 and ball.xcor()>320 or ball.distance(paddlel)<50 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor()>380:
        ball.reposition()
        scoreboard.up_lscore()

        # ball.write(f'{ball.score}',align="center",font=("Arial",8,"normal"))
    if ball.xcor()<-380:
        ball.reposition()
        scoreboard.up_rscore()





screen.exitonclick()
