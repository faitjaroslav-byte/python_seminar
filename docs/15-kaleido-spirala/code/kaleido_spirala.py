import turtle
from random import randint

turtle.bgcolor("black")
turtle.speed("fastest")
turtle.hideturtle()

def draw_shape(size, angle, shift, shape):
    turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    turtle.shape(shape)

turtle.colormode(255)
size = 10
angle = 0
shift = 1

while True:
    draw_shape(size, angle, shift, "circle")
    size += 1
    angle += 1
    shift += 1
