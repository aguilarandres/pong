# Pong in Python 3
# By @TokyoEdTech

# Turtle graphics for Tkinter (Tk)
import turtle

window = turtle.Screen()
window.title = ("Pong by @TokyoEdTech")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# START Paddle A

# turtle object
paddle_a = turtle.Turtle()
# annimation speed set to maximum
paddle_a.speed(0)
# default square 20px by 20px
paddle_a.shape("square")
# stretch shape to emulate pong paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
# Pull the pen up - no drawing when moving
paddle_a.penup()
# set x y coordinates goto(x, y)
paddle_a.goto(-350, 0)

# END Paddle A

# START Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
# END Paddle B

# START Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
# center of screen
ball.goto(0, 0)
# END Ball

# Function

def paddle_a_up():
    # determine current Y coordinate
    y = paddle_a.ycor()
    # add 20px to the Y coordinate
    paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    paddle_a.sety(y - 20)

def paddle_b_up():
    # determine current Y coordinate
    y = paddle_b.ycor()
    # add 20px to the Y coordinate
    paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    paddle_b.sety(y - 20)

# Keyboard binding
# listen for keyboard input
window.listen()
# call paddle_a_up() when "w" key is pressed
window.onkeypress(paddle_a_up, "w")
# call paddle_a_up() when "s" key is pressed
window.onkeypress(paddle_a_down, "s")
# call paddle_a_up() when Up-arrow key is pressed
window.onkeypress(paddle_b_up, "Up")
# call paddle_a_up() when Down-arrow key is pressed
window.onkeypress(paddle_b_down, "Down")
# main game loop
while True:
    # update screen every time loop runs
  window.update()
