# Pong in Python 3
# By @TokyoEdTech

# Turtle graphics for Tkinter (Tk)
import turtle
import os

window_width  = 800
window_height = 600

score_p1 = 0
score_p2 = 0

window = turtle.Screen()
window.title = ("Pong by @TokyoEdTech")
window.bgcolor("black")
window.setup(window_width, window_height)
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
# move ball by n pixels
ball.dx = 0.10
ball.dy = -0.10
# END Ball

# START Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# hide turtle so only written text is displayed
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {} | Player 2: {}".format(score_p1, score_p2), \
    align="center", font=("Courier", 24, "normal"))

# END Pen 

# START Functions

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

# END Functions

# Keyboard binding

# listen for keyboard input
window.listen()
# call paddle_a_up() when "w" key is pressed
window.onkeypress(paddle_a_up, "w")
# call paddle_a_up() when "s" key is pressed
window.onkeypress(paddle_a_down, "s")
# call paddle_b_up() when Up-arrow key is pressed
window.onkeypress(paddle_b_up, "Up")
# call paddle_b_up() when Down-arrow key is pressed
window.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    # update screen every time loop runs
  window.update()

  # move ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # border checking

  # top border
  if ball.ycor() > 290:
    ball.sety(290)
    # reverse direction of movement
    ball.dy *= -1
    os.system("aplay blip.wav&")

  # bottom border
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    os.system("aplay blip.wav&")

  # confirm that ball is off screen
  if ball.xcor() > 390:
      # set ball x, y coordinates to zero to restart game
    ball.goto(0, 0)
    ball.dx *= -1
    score_p1 += 1
    pen.clear()
    pen.write("Player 1: {} | Player 2: {}".format(score_p1, score_p2), \
        align="center", font=("Courier", 24, "normal"))

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_p2 +=1
    pen.clear()
    pen.write("Player 1: {} | Player 2: {}".format(score_p1, score_p2), \
        align="center", font=("Courier", 24, "normal"))


  # Paddle and ball collisions

  # Paddle P1
  if (ball.xcor() < -340 and ball.xcor() > -350) and \
  (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
      ball.setx(-340)
      ball.dx *= -1
      os.system("aplay blip.wav&")
  # Paddle P2
  if (ball.xcor() > 340 and ball.xcor() < 350) and \
  (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
      ball.setx(340)
      ball.dx *= -1
      os.system("aplay blip.wav&")
