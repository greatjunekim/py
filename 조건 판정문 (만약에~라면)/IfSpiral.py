answer = input("나선형을보고 싶나요? y/n:")
if answer == 'y':
    print("동작중입니다...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("끝")
