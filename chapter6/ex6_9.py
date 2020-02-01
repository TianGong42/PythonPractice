# 创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；
# 对于其中的每个人，都存储他喜欢的1～3个地方。为让这个练习更有趣些，
# 可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
place1 = ['上海', '北京', '哈尔滨市']
place2 = ['前池', '鲍田', '仙甲']
place3 = ['曼联', '慢城', '热刺']
favorite_places = {
    '张三':place1,
    '李四':place2,
    '王五':place3,
}
for name, places in favorite_places.items():
    print(name)
    for place in places:
        print('\t' +  place)