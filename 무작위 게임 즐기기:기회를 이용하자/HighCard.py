import random

suits = ["클럽","다이아몬드","하트","스페이트"]
faces = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

나의_점수 = 0
봇의_점수 = 0
게임 = 0
while True:
    게임 = 게임 + 1    
    my_face = random .choice(faces)
    my_suit = random.choice(suits)
    
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("나:내 카드는",my_face," ",my_suit,"입니다")
    
    print("봇:내 카드는",your_face," ",your_suit,"입니다")
    
    if faces.index(my_face) > faces.index(your_face):
        나의_점수 = 나의_점수 + 1
        print("나의 승리 봇의 점수는",봇의_점수,"이고 나의 점수는",나의_점수,"입니다")

    elif faces.index(my_face) < faces.index(your_face):
        봇의_점수 = 봇의_점수 + 1
        print("봇 승리 봇의 점수는",봇의_점수,"이고 나의 점수는",나의_점수,"입니다")
        
    else:
        print("비겼습니다")
    answer = input("[Enter]키를 누르면 계속 진행 15번 뒤에 종료")
    if 게임 == 15: 
        break
if 봇의_점수 > 나의_점수:
    print("봇 승리")
if 봇의_점수 < 나의_점수:
    print("나의 승리")
if 봇의_점수 == 나의_점수:
    print("비겼습니다")


