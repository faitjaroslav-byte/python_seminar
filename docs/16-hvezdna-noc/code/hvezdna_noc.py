import turtle as t
from random import randint, random

t.speed("fastest")
t.bgcolor("midnight blue")
t.hideturtle()

def draw_star(points, size, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    angle = 180 - (180 / points)
    for _ in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

while True:
    points = randint(2, 5) * 2 + 1
    size = randint(10, 50)
    color = (random(), random(), random())
    x = randint(-350, 300)
    y = randint(-250, 250)
    draw_star(points, size, color, x, y)
