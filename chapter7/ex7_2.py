# 编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
number = input("请问有多少人用餐:")
number = int(number)
if number > 8:
    print("没有空桌了")
else:
    print("来嘞，有位置")