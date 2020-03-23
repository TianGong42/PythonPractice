import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
# 然后我们打开这个文件，并将结果文件对象存储在f中
with open(filename) as f:
    # 调用csv.reader()，并将前面存储的文件对象作为实参传递给它，并且创建一个reader
    reader = csv.reader(f)
    # 调用next函数，并且将阅读器对象传递给它时，它将返回文件中的线下一行
    header_row = next(reader)
    # 创建两个空列表，用于存储从文件中提取的日期和最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # 将日期信息转换为datetime对象
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # 根据数据绘制图形
    fig = plt.figure(dpi = 128, figsize=(10,6))
    # 通过alpha指定颜色的透明度
    plt.plot(dates, highs, c='red',alpha=0.5)
    plt.plot(dates, lows, c='blue',alpha=0.5)
    # fill_between填充颜色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    #设置图形的格式
    plt.title("Daily hight and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
    plt.xlabel("", fontsize=16)
    # 绘制斜的日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()