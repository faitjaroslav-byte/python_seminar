import turtle
from random import randint

turtle.bgcolor("black")
turtle.speed("fastest")
turtle.hideturtle()
turtle.colormode(255)

def draw_shape(size, angle, shift):
    turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)

size = 30
angle = 59
shift = 1

while True:
    draw_shape(size, angle, shift)
    size = size + 1
    shift = shift + 1
