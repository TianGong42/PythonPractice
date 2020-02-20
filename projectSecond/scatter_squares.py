#!/usr/bin/python
# -*- coding: UTF-8 -*-
from matplotlib import font_manager
import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,edgecolors='none', s=10,c=y_values, cmap=plt.cm.Blues)
#设置图表图标并给坐标轴加上标签
zh_font = font_manager.FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)
plt.title("求平方的数", fontsize=24,fontproperties=zh_font)
plt.xlabel("数", fontsize=14,fontproperties=zh_font)
plt.ylabel("平方值", fontsize=14,fontproperties=zh_font)
#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0,1100,0,1100000])    #设置x轴和y轴的最大值
#plt.show()
plt.savefig("squares_plot.png",bbox_inches='tight')