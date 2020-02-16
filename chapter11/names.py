from name_function import get_formatted_name
print("输入q停止程序")
while True:
    first = input("\n请输入您的姓氏：")
    if first == 'q':
        break
    last = input("\n请输入您的名字：")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\t完整的名称：" + formatted_name + '.')
