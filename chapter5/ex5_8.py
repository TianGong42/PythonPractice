# 创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'。
# 想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
# users = ['张三', '李四', '王五', '赵六', 'admin']
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some users!")
