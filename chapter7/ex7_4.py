# 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。
# 每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
while True:
    message = input("请输入披萨配料：")
    if message == 'quit':
        break
    else:
        print("我们在披萨中加入了" + message)