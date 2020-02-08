# 如果要让函数接受不同类型的实参，必须在函数定义中奖接纳任意数量实参的形参放到最后
def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
