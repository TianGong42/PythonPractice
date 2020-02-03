# 编写一个程序，调查用户梦想的度假胜地。使用类似于“If youcould visit one place in the world, 
# where would you go?”的提示，并编写一个打印调查结果的代码块。

visit_places = {}
polling_active = True
# 只要标志为True，整个循环会一直执行下去
while polling_active:
    name = input("你叫什么名字?")
    response = input("你最想去度假的地方是哪里？")
    visit_places[name] = response
    judge = input("你好，你还想进行调查吗？yes继续,no不继续")
    if judge == 'no':
        polling_active = False

for name,place in visit_places.items():
    print(name + "度假最想去的地方" + place)