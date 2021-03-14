비번 = ord('a') * 100 + ord('U')
비번맟추기 = eval(input("비밀번호를 대시오"))
while 비번 != 비번맟추기:
    if 비번 != 비번맟추기:
        print("왜 틀리냐")
    비번맟추기 = eval(input("다시"))
print(비번,"통과")
import random
the_number = random.randint(1, 11)
guess = int(input("1부터 11사이의 숫자를 맟춰보세요"))
while guess != the_number:
    if guess > the_number:
        print( guess,"너무커요")
    if guess < the_number:
        print(guess,"너무작아요")
    guess = int(input("다시"))
print(guess,"성공")