import turtle
import time

turtle_instance = turtle.Turtle()
turtle_instance.pensize(5)
turtle_instance.speed(5)
turtle_instance.hideturtle()

def movement(x,y):
    turtle_instance.penup()
    turtle_instance.goto(x,y)
    turtle_instance.pendown()
    turtle_instance.setheading(360)

def draw_rectangle(length, breadth, color):
    turtle_instance.begin_fill()
    turtle_instance.color(color)
    turtle_instance.forward(length)
    turtle_instance.left(90)
    turtle_instance.forward(breadth)
    turtle_instance.left(90)
    turtle_instance.forward(length)
    turtle_instance.left(90)
    turtle_instance.forward(breadth)
    turtle_instance.end_fill()

movement(-351,80)
## Orange rectangle ##
draw_rectangle(700,200,"orange")

movement(-351,-280)
## Green rectangle ##
draw_rectangle(700,200,'green')
time.sleep(2)

movement(0,0)
## make Ashoke chakra ##
turtle_instance.color("navy blue")
for i in range(24):
    turtle_instance.forward(80)
    turtle_instance.backward(80)
    turtle_instance.left(15)
movement(0,-80)
turtle_instance.circle(80,360)

