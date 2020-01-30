# 按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。

current_users = ["张三", "李四", "王五", "赵六", "七七"]
new_users = ["张三", "李四", "原始天尊" , "通天教主", "太上老君"]

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " 这个名字已经被使用")
    else:
        print(new_user + " 这个名字可以使用")