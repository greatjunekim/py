name = input("이름이 무었입니까? ")
while name != "":
    for x in range(10):
        print(name, end = " ")
    print()
    name = input("다른 이름을 입력하세요. 종료하고 싶다면 엔터키를 누르세요:")
print("놀아줘서 고마워")