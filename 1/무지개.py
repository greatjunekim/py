import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red","orange","yellow","green","blue"]
for x in range(100):
    t.forward(4)
    t.pencolor(colors[x%5])
    t.left(x/10)
