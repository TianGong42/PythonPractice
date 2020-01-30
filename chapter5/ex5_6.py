# 设置变量age的值，再编写一个if-elif-else结构，
# 根据age的值判断处于人生的哪个阶段。
age = 15

if age < 2:
    print("他是婴儿")
elif age < 4:
    print("他正在学步")
elif age < 13:
    print("他是儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("他是成年人")
else:
    print("他是老人")