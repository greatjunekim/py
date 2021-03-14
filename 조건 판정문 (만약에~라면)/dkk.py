import time
글 = input("글을 쓰시오")
time.sleep(0.7)
#색깔 = input("어떤 색으로 할까요?")#2
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.penup
t.forward(0)
#colors = [색깔]#2
colors = ["green","yellow","blue","orange"]#1
for x in range(100000):
    #t.pencolor(colors[1])#2
    t.pencolor(colors[x%4])#1
    t.penup
    t.forward(0)
    t.pendown
    t.write(글 , font = ("Arial", int((360) / 4),"bold"), align="center",)

    


    