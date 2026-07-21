import turtle as t
from random import randint

t.bgcolor("black")
t.speed("fastest")
t.hideturtle()
t.colormode(255)

def get_line_length():
    choice = input("Choose line length: long, medium, or short: ")
    if choice == "long":
        return 250
    if choice == "medium":
        return 100
    return 50

def get_line_width():
    choice = input("Choose line width: thick, medium, or thin: ")
    if choice == "thick":
        return 40
    if choice == "medium":
        return 25
    return 10

line_length = get_line_length()
line_width = get_line_width()

while True:
    t.pensize(line_width)
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    t.forward(line_length)
    t.right(randint(1, 360))

    x, y = t.position()
    if x > 300 or x < -300 or y > 300 or y < -300:
        t.penup()
        t.goto(randint(-300, 300), randint(-300, 300))
        t.pendown()
