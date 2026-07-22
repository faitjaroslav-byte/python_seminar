import turtle as t
from random import randint, random

t.bgcolor("midnightblue")
t.speed("fastest")
t.hideturtle()

def draw_star(points, size, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)

    for point in range(points):
        t.forward(size)
        t.right(180 - 180 / points)

while True:
    points = randint(5, 8)
    size = randint(20, 80)
    color = (random(), random(), random())
    x = randint(-300, 300)
    y = randint(-250, 250)
    draw_star(points, size, color, x, y)
