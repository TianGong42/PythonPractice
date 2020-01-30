# 创建一个列表，其中包含数字1～1000000，再使用min()和max()核实该列表确实是从1开始，
# 到1000000结束的。另外，对这个列表调用函数sum()，看看Python将一百万个数字相加需要多长时间。
numbers = []
for value in range(1,1000001):
    numbers.append(value)

print("最小值" + str(min(numbers)))
print("最小值" + str(max(numbers)))
print("和：" + str(sum(numbers)))