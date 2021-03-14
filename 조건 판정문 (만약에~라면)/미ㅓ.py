import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["blue","green","yellow"]
졸업_축하1 = "지" 
졸업_축하2 = "졸"
졸업_축하3 = "업"
졸업_축하4 = "축"
졸업_축하5 = "하"   
졸업_축하6 = "해" 
t.speed(1)
t.forward(-700)
for x in range(100):
    t.pencolor(colors[x%3])
    t.penup
    t.forward(150)
    t.pendown
    t.write(졸업_축하1, font = ("Arial", int((600) / 4),"bold"))
    t.pencolor(colors[x%3])
    t.penup
    t.forward(150)
    t.pendown
    t.write(졸업_축하2, font = ("Arial", int((600) / 4),"bold"))
    t.pencolor(colors[x%3])
    t.penup
    t.forward(150)
    t.pendown
    t.write(졸업_축하3, font = ("Arial", int((600) / 4),"bold"))
    t.pencolor(colors[x%3])
    t.penup
    t.forward(150)
    t.pendown
    t.write(졸업_축하4, font = ("Arial", int((600) / 4),"bold"))
    t.pencolor(colors[x%3])
    t.penup
    t.forward(150)
    t.pendown
    t.write(졸업_축하5, font = ("Arial", int((600) / 4),"bold"))
    t.pencolor(colors[x%3])
    t.penup
    t.forward(150)
    t.pendown
    t.write(졸업_축하6, font = ("Arial", int((600) / 4),"bold"))
    



