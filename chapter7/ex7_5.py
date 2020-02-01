# 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；
# 3～12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
while True:
    active = True
    age = input("请输入您的年龄：")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("您不需要钱，免费勒，您")
    elif age < 12:
        print("请付10美元")
    else:
        print("请付15美元")