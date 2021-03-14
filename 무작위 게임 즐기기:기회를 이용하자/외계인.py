import random
def alien():
    language = ["가","나","다","라","마","바","사","아","자","차","카","타","파","하"]
    input("아가우너")
    count = random.randint(1, len(language))
    print(f'len(language) is {len(language)} count is {count}')
    language = random.choices(language, k=count)
    print("".join(language))

while True:
    alien()
    # if  input("라가라") not in ["라가라","fkrkfk"]:
    #     break
