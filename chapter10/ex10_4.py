# 编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，
# 并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
filename = 'guest_book.txt'
with open(filename,'w') as file_object:
    name = input("请输入你的名字,输入q停止输入:")
    while name != 'q':
        print("Hi! " + name )
        file_object.write(name + "\n")
        name = input("请输入你的名字,输入q停止输入:")
