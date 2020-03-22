import pygal
from die import Die
#创建两个D8的骰子
die_1 = Die(8)
die_2 = Die(8)
#投掷骰子多次，将结果存储到一个数据中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#分析数据
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# 先求出每个值出现的次数，然后存入list中
for value in range(2,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果
hist = pygal.Bar()
hist.title = "两个8面骰子投掷1000次"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "结果"
hist.y_labels = "频率分析"
# 将所有值放到图表里
hist.add("D8+D8", frequencies)
hist.render_to_file("dice_visual.svg")