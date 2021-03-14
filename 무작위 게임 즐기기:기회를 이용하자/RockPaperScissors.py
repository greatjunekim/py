import random
choices = ["바위","보","가위"]
while True:
    player = input("가위, 바위, 보 중 하나를 선택하세요(또는 종료로 게임을 종료합니다.")

    if player == "종료":
        break

    computer = random.choice(choices)
    print("나 ",player," 컴퓨터 ",computer,"야")
    if player == computer:
        print("동점")
    elif player == "바위":
        if computer == "가위":
            print("승리")
        else:
            print("패배")
    elif player == "보":
        if computer == "바위":
            print("승리")
        else:
            print("패배")
    elif player == "가위":
        if computer == "보":
            print("승리")
        else:
            print("패배")
    else:
        print("에러")


            
    
    
    
            