# 编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    name = input("请写入你的名字:")
    file_object.write(name)