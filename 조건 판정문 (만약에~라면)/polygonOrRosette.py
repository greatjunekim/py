import turtle as turtle
t = turtle.Pen()
number = int(turtle.numinput("Number of sides or circles,몇 개의 변 또는 원이 있습니까",6))
shape = turtle.textinput("어떤 모양을 원하세요?","다각형은 'p',장미모양은'r'입력하세요:")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward (150)
    t.left(360/number)
