print("MathHomework.py")
problem = input("수학 문제를 입력하거나 'q'를 입력해서 프로그램을 종료해주세요.")
while (problem != "q"):
    print("the answer to",problem,"is",eval(problem))
    problem = input("수학 문제를 입력하거나 'q'를 입력해서 프로그램을 종료해주세요.")