import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing ball simulator")
wn.tracer(0)

balls = []
number = 0
    
def _bounce(num):
    for i in range(number):
        balls.append(turtle.Turtle())

    for ball in balls:
        ball.shape("circle")
        ball.color("green")
        ball.penup()
        ball.speed(0)
        x = random.randint(-290, 290)
        y = random.randint(200, 400)
        ball.goto(x,y)
        ball.dy = 0
        ball.dx = random.randint(-3, 3)
        return

    gravity = 0.1

    while True:
        wn.update()
        
        for ball in balls:
            ball.dy -= gravity
            ball.sety(ball.ycor() + ball.dy)
        
            ball.setx(ball.xcor() + ball.dx)
        #check for wall collision
            if ball.xcor() > 300:
                ball.dx *= -1
            
            if ball.xcor() < -300:
                ball.dx *= -1
        #check for a bounce
            if ball.ycor() < -300:
                ball.dy *= -1
            
     
_bounce(num =)  


wn.mainloop()








# from turtle import Screen, Turtle

# CURSOR_SIZE = 20

# screen = Screen()
# screen.setup(600, 600)  # 12 x 24 bricks
# screen.setworldcoordinates(0, 0, 12, 24)  # coordinates based on bricks
# screen.bgcolor('black')

# turtle = Turtle('square', visible=False)
# turtle.penup()
# turtle.speed('fastest')
# turtle.color('black', 'red')
# turtle.shapesize(25 / CURSOR_SIZE, 50 / CURSOR_SIZE, 5)  # turn cursor into brick

# for y in range(24):
#     turtle.setposition(-0.5 * (y % 2), y + 0.3)

#     for x in range(13):  # baker's dozen due to brick skew
#         turtle.stamp()
#         turtle.forward(1)

# screen.mainloop()