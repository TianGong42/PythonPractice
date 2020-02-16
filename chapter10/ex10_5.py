# 编写一个while循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
filename = 'favorite_reason.txt'
with open(filename, 'w',encoding='utf-8') as file_object:
    reason = input("请输入您为什么喜欢编程，按q停止输入：")
    while reason != 'q':
        file_object.write(reason + "\n")
        reason = input("请输入您为什么喜欢编程，按q停止输入：")