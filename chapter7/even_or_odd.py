number = input("输入一个数字，我告诉你它是偶数还是奇数：")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is 偶数.")
else:
    print("\nThe number " + str(number) + " is 奇数.")