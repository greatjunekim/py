import random

def 주사위굴리기(count):
    result = [0] * count

    for x in range(count):
        result[x] = random.randint(1,6)

    return result


# 주사위 = [0,0,0,0,0]

# for x in range(5):
#     주사위[x] = random.randint(1,6)

#     print(주사위)

주사위 = 주사위굴리기(3)
print(주사위)


if 주사위[0] != 주사위[1]:
    print("실패")
elif 주사위[1] != 주사위[2]:
    print("실패")
else:
    print("야찌")
    
print(6/45*5/44*4/43*3/42*2/41*1/40)

