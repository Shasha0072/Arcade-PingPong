from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

score_board = Scoreboard()

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)

pong = Pong()
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()
    if pong.ycor() >= 290 or pong.ycor() <= -290:
        pong.bounce_y()

    if pong.distance(paddle_r) < 50  and pong.xcor() > 320 or pong.distance(paddle_l) < 50 and pong.xcor() < - 320:
        pong.bounce_x()

    if pong.xcor() >= 380:
        pong.reset_position()
        score_board.l_point()
    if pong.xcor() < -380:
        pong.reset_position()
        score_board.r_point()





screen.exitonclick()