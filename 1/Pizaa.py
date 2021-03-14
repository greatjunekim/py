number_of_pizzas = eval(input("피자 몇 판을 주문하시겠습니까?"))
cost_per_pizza = 10
subtotal = number_of_pizzas * cost_per_pizza
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax
print("가격은",total,"달러")
print("이피자 가격에는 피자 가격",subtotal,"과 세금")
print(sales_tax,"이 포함돼 있습니다.")