import turtle
t = turtle.Pen()
turtle.speed(0)
number_of_circles = int(turtle.numinput("number of circles",
"장미에 몇 개의 우너을 그리기 우너하세요",6))
for x in range(number_of_circles): 
    t.circle(100)
    t.left(360/number_of_circles)
