# 创建一个名为cities的字典，其中将三个城市名用作键；对于每座城市，
# 都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country、population和fact等键。将每座城市的名字以及有关它们的信息都打印出来。

beijing = {'country':'中国', 'population':'2000000', 'fact': '开国大典'}
shanghai = {'country':'中国', 'population':'3000000' , 'fact':'几百位教授一致通过'}
hangzhou = {'country':'中国', 'population':'40000000', 'fact':'断桥残雪'}
cities = {'beijing':beijing, 'shanghai':shanghai , 'hangzhou' :hangzhou}
for city in cities.values():
    print(city['country'])
    print(city['population'])
    print(city['fact'])



