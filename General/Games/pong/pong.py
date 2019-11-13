# Simple Pong

import turtle, os, winsound, playsound

# Wimdow
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()  # no lines
left_paddle.goto(-350, 0)

# Other Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()  # no lines
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  # no lines
ball.goto(0, 0)
ball.dx = 0.3  # How many pixels of delta on screen movement
ball.dy = -0.3  # How many pixels of delta on screen movement

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 20, "normal"))

# Paddle movements funcs

# Left
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Right
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Keyboard bindings
window.listen()
#Right
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
#Left
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main Game Loop
while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
    # Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
    # Left
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
    # Right
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    # Paddle collision
    # Right
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 55 and ball.ycor() > right_paddle.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.mp3', winsound.SND_ASYNC)
        # os.system("start bounce.mp3")

    # Left
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 55 and ball.ycor() > left_paddle.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.mp3', winsound.SND_ASYNC)
        # os.system("start bounce.mp3")
