import turtle
turtle.bgcolor("cyan")
t=turtle.Pen()
t.speed(0)
colors = ["red","blue"]
for x in range(10000):
    t.pencolor(colors[x%2])
    t.forward(x)
    t.right(91)
