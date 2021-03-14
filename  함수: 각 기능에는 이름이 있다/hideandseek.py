import random
import time
def game1():
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

def add(score):
    return score + 10

def game2():
    print("숨바꼭질을 시작 한다")
    time.sleep(0.5)
    점수 = 0
    방들 = ["거실","안방","주방","화장실","침실2","침실3"]
    while True:
        숨은장소 = input("숨을곳을 거실,안방,주방,화장실,침실2,침실3 중에 선택하세요 점수는"+str(점수)+" 입니다.")
        
        if 숨은장소 not in 방들:
            print('잘못 입력했네, 다시 입력해봐')
            continue
        
        술래위치 = random.choice(방들)
        print("술래가 ",술래위치," 로 이동한다.")
        if 숨은장소 == 술래위치:
            print("걸렸다ㅠㅠ 너의 점수는",점수," 야")
            if 10 >= 점수:
                print("운이 없구나")
            elif 50 >= 점수:
                print("더 잘 숨어봐")
            elif 70 >= 점수:
                print("오~ 꽤 잘숨었는데")
            elif 90 >= 점수:
                print("대박")
            elif 100 <= 점수:
                print("숨바꼭질의 달인이다")
            break
        else:
            점수 = add(점수)

    # while True:
    #     game2()
    #     if input("다시할거야? y/n") not in ['y', 'Y', 'ㅛ', '예']:
    #         break
print("어떤 게임을 하실건가요?")
time.sleep(1)
print("가위바위보 게임 숨바꼭질 게임이 있습니다")
time.sleep(1.5)
print("가위바위보게임을 하고싶다면 가위라고쓰세요")
time.sleep(1.4)
print("숨바꼭질게임을 하고싶다면 숨기라고쓰세요")
if input("여기에 쓰세요") == "가위":
    game1()
if input("여기에 쓰세요") == "숨기":
    game2()





