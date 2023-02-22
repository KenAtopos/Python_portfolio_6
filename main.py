import turtle
import time
import random

# Set up the game window
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(5):
    for j in range(-3, 4):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(j * 100, 150 - i * 40)
        bricks.append(brick)


# Define the paddle movement function
def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


# Keyboard bindings
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# Set up the player lives
lives = 3
win.title(f"Lives: {lives}")

# Main game loop
try:
    while True:
        win.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Check for border collisions
        if ball.xcor() > 290:
            ball.setx(290)
            ball.dx *= -1
        elif ball.xcor() < -290:
            ball.setx(-290)
            ball.dx *= -1
        elif ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        elif ball.ycor() < -290:
            ball.goto(0, 0)
            ball.dy *= -1

        # Check for paddle collision
        if ball.ycor() < -240 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            ball.dy *= -1

        # Check for brick collisions
        for brick in bricks:
            if ball.distance(brick) < 30:
                bricks.remove(brick)
                brick.hideturtle()
                ball.dy *= -1

        # Check if player wins
        if len(bricks) == 0:
            ball.goto(0, 0)
            ball.dx = 0
            ball.dy = 0
            win.title("You Win!")
            time.sleep(3)
            break

        # Check if ball falls out of screen
        if ball.ycor() < -300:
            ball.goto(0, 0)
            ball.dy = -ball.dy

            # Reduce player's lives by one
            lives -= 1
            win.title(f"Lives: {lives}")

            # Game over if no lives left
            if lives == 0:
                win.title("Game Over")
                time.sleep(3)
                break

        # Delay to control the speed of the game
        time.sleep(0.01)
except turtle.Terminator:
    pass

# close the game window
win.bye()

