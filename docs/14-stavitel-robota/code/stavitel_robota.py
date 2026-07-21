import turtle as t

t.speed("fastest")
t.bgcolor("Dodger blue")

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

# Feet
t.goto(-100, -150)
rectangle(50, 20, "blue")
t.goto(-30, -150)
rectangle(50, 20, "blue")

# Legs
t.goto(-75, -50)
rectangle(15, 100, "grey")
t.goto(-10, -50)
rectangle(15, 100, "grey")

# Body
t.goto(-90, 100)
rectangle(100, 150, "red")

# Arms
t.goto(-150, 70)
rectangle(60, 15, "grey")
t.goto(10, 70)
rectangle(60, 15, "grey")

# Neck
t.goto(-50, 120)
rectangle(15, 20, "grey")

# Head
t.goto(-85, 170)
rectangle(80, 50, "red")

# Eyes
t.goto(-60, 160)
rectangle(10, 5, "white")
t.goto(-30, 160)
rectangle(10, 5, "white")

# Mouth
t.goto(-65, 135)
rectangle(40, 5, "black")

t.hideturtle()
t.done()
