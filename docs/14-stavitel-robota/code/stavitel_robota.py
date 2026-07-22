import turtle as t

t.speed("fastest")
t.hideturtle()

def rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for side in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move_to(-60, 80)
rectangle(120, 80, "steelblue")
move_to(-35, -5)
rectangle(70, 95, "gray")
move_to(-70, -25)
rectangle(30, 90, "orange")
move_to(40, -25)
rectangle(30, 90, "orange")
move_to(-25, 95)
t.dot(16, "white")
move_to(25, 95)
t.dot(16, "white")
move_to(-25, 45)
rectangle(50, 10, "black")

t.done()
