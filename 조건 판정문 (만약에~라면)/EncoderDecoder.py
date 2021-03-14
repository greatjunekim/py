message = input("암호화 또는 해독할 매시지를 입력하세요:")
키 = eval(input("키를입력하세요"))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + (키)
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("Output message: ", output)