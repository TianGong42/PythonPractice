# 检查列表是不是空的
requested_toppings = []
if requested_toppings: # 判断列表是否为空的检查，为空返回false
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")