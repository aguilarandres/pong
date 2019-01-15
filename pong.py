# Pong in Python 3
# By @TokyoEdTech

# Turtle graphics for Tkinter (Tk)
import turtle
import os

window_width  = 800
window_height = 600

score_p1 = 0
score_p2 = 0

font_type  = "Ubuntu Mono"
font_size  = 24
font_style = "normal"

p1_xcor = -350
p2_xcor =  350

# number of pixels to shift paddle by
paddle_shift = 20

# number of pixels to shift ball by
ball_shift_x =  0.20
ball_shift_y = -0.20

window = turtle.Screen()
window.title = ("Pong by @TokyoEdTech")
window.bgcolor("black")
window.setup(window_width, window_height)
window.tracer(0)

# START Paddle P1

# turtle object
paddle_p1 = turtle.Turtle()
# annimation speed set to maximum
paddle_p1.speed(0)
# default square 20px by 20px
paddle_p1.shape("square")
# stretch shape to emulate pong paddle
paddle_p1.shapesize(stretch_wid=5, stretch_len=1)
paddle_p1.color("white")
# Pull the pen up - no drawing when moving
paddle_p1.penup()
# set x y coordinates goto(x, y)
paddle_p1.goto(p1_xcor, 0)

# END Paddle P1

# START Paddle P2
paddle_p2 = turtle.Turtle()
paddle_p2.speed(0)
paddle_p2.shape("square")
paddle_p2.shapesize(stretch_wid=5, stretch_len=1)
paddle_p2.color("white")
paddle_p2.penup()
paddle_p2.goto(p2_xcor, 0)
# END Paddle P2

# START Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
# center of screen
ball.goto(0, 0)
# move ball by n pixels
ball.dx = ball_shift_x 
ball.dy = ball_shift_y
# END Ball

# START Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# hide turtle so only written text is displayed
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), \
    align="center", font=(font_type, font_size, font_style))

# END Pen

# START Functions

def paddle_p1_up():
    # determine current Y coordinate
    y = paddle_p1.ycor()
    # add n pixels to the Y coordinate
    paddle_p1.sety(y + paddle_shift)

def paddle_p1_down():
    y = paddle_p1.ycor()
    paddle_p1.sety(y - paddle_shift)

def paddle_p2_up():
    # determine current Y coordinate
    y = paddle_p2.ycor()
    # add n pixels to the Y coordinate
    paddle_p2.sety(y + paddle_shift)

def paddle_p2_down():
    y = paddle_p2.ycor()
    paddle_p2.sety(y - paddle_shift)

# END Functions

# Keyboard binding

# listen for keyboard input
window.listen()
# call paddle_p1_up() when "w" key is pressed
window.onkeypress(paddle_p1_up, "w")
# call paddle_p1_up() when "s" key is pressed
window.onkeypress(paddle_p1_down, "s")
# call paddle_p2_up() when Up-arrow key is pressed
window.onkeypress(paddle_p2_up, "Up")
# call paddle_p2_up() when Down-arrow key is pressed
window.onkeypress(paddle_p2_down, "Down")

# main game loop
while True:
    # update screen every time loop runs
  window.update()

  # move ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # border checking

  # top border y-axis
  if ball.ycor() > 290:
    ball.sety(290)
    # reverse direction of movement
    ball.dy *= -1
    os.system("aplay blip.wav&")

  # bottom border y-axis
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    os.system("aplay blip.wav&")

  # confirm that ball is off screen
  # Player 1 edge; right hand side; x-axis
  if ball.xcor() > 390:
      # set ball x, y coordinates to zero to restart game
    ball.goto(0, 0)
    ball.dx *= -1
    score_p1 += 1
    pen.clear()
    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), \
        align="center", font=(font_type, font_size, font_style))
  # Player 2 edge; left hand side; x-axis
  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_p2 +=1
    pen.clear()
    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), \
        align="center", font=(font_type, font_size, font_style))


  # Paddle and ball collisions

  # Paddle P1
  if (ball.xcor() < -340 and ball.xcor() > p1_xcor) and \
  (ball.ycor() < paddle_p1.ycor() + 40 and ball.ycor() > paddle_p1.ycor() - 40):
      ball.setx(-340)
      ball.dx *= -1
      os.system("aplay blip.wav&")
  # Paddle P2
  if (ball.xcor() > 340 and ball.xcor() < p2_xcor) and \
  (ball.ycor() < paddle_p2.ycor() + 40 and ball.ycor() > paddle_p2.ycor() - 40):
      ball.setx(340)
      ball.dx *= -1
      os.system("aplay blip.wav&")
