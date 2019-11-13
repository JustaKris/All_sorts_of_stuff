# Simple Pong

import turtle

# Wimdow
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

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
ball.dx = 2  # How many pixels of delta on screen movement
ball.dy = 2  # How many pixels of delta on screen movement

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
window.onkeypress(left_paddle_up, "s")
#Left
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main Game Loop
while True:
    window.update()

    # Move ball
    # ball.setx(ball.xcor() + ball.dx)
    # ball.sety(ball.ycor)