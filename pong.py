import turtle

# Creating a game window

window = turtle.Screen()
window.title("Classic Pong Game : By Gaurav")  # layout or Game title
window.bgcolor("grey")  # layout background color
window.setup(width=800, height=600)  # layout size

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()  # turtle is module name and Turtle() is class name
paddleA.speed(0)  # For speed of animation
paddleA.shape("square")  # using preset shape here
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("red")
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()  # turtle is module name and Turtle() is class name
paddleB.speed(0)  # For speed of animation
paddleB.shape("square")  # using preset shape here
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("red")
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()  # turtle is module name and Turtle() is class name
ball.speed(0)  # For speed of animation
ball.shape("circle")  # using preset shape here
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3  # here dx means Change in x coordinate
ball.dy = -3  # here dy means Change in y coordinate

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function

# for right paddle
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


# for left paddle

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Key Bindings
window.listen()  # it tells to read user input keyword values.
window.onkeypress(paddleA_up, "w")
window.onkeypress(paddleA_down, "s")
window.onkeypress(paddleB_up, "Up")
window.onkeypress(paddleB_down, "Down")

# Game Loop
while True:
    window.update()  # it updates the window/layout every time when loop runs

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # corner and border checking up and down
    if ball.ycor() > 260:
        ball.sety(260)
        ball.dy *= -1

    elif ball.ycor() < -260:
        ball.sety(-260)
        ball.dy *= -1

    # corner and border checking right and left
    if ball.xcor() > 330:
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreB, scoreA), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -330:
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreB, scoreA), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision

    if (ball.xcor() > 330 and ball.xcor() < 330) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -330) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
