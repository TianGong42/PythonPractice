# 加法计算器
while True:
    try:
        first_number = input("请输入第一个数字,输入q停止程序：")
        if first_number == 'q':
            break
        second_number = input("请输入第二个数字，输入q停止程序：")
        if second_number == 'q':
            break
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("请输入正确的数字！")
    else:
        print(answer)