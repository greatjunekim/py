driving_age = eval(input("법적으로 운전을 할 수 있는 나이는?"))
your_age = eval(input("당신의 나이는?"))
if your_age >= driving_age:
    print("넌 운전할 수 있어")
if your_age < driving_age:
    print("넌 ",driving_age - your_age,"년 동안 기다려야지 운전할 수 있어")
 
