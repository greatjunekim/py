import random
import time
스파이 = 0
시민 = 0
while True:
    input("js")
    직업 = ["스파이","시민"]
    직업 = random.choice(직업)
    print(직업)
    if 직업 == "스파이":
        스파이 = 스파이 + 1
    if 스파이 == 2:
        print("스파이 아니고 시민이에요")
    if 직업 == "시민":
        시민 = 시민 + 1
    if 시민 == 2:
        print("시민 아니고 스파이에요")


