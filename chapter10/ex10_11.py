# 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know yourfavorite number! It's _____.”。
import json
filename = 'number.json'
def save_number():
    favorite_number = input("请输入你最喜欢的数字:")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number,f_obj)
def get_number():
    try:
        with open(filename) as f_obj:
            print("你最喜欢的数字是" + json.load(f_obj))
    except FileNotFoundError:
        print("文件没找到")
save_number()
get_number()