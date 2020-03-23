import matplotlib.pyplot as plt 
from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的点都绘制出来
def funtion1():
    """使用scatter方法"""
    while True:
        # 创建一个RandomWalk实例，并将其包含的点都绘制出来
        rw = RandomWalk(50000)
        rw.fill_walk()
        # 设置绘图窗口的尺寸
        plt.figure(figsize=(10,6))
        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, s=1,c=point_numbers, cmap=plt.cm.Blues,edgecolors='none')
        # 突出起点和终点，将点的大小设置为100
        plt.scatter(0,0,c='green',edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1],c='red', edgecolors='none', s=100)
        # 隐藏坐标轴,使用plt.axes()函数将每条坐标轴的可见性都设置为False
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()
        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break

def function2():
    """使用plot方法"""
    while True:
        # 创建一个RandomWalk实例，并将其包含的点都绘制出来
        rw = RandomWalk(5000)
        rw.fill_walk()
        # 设置绘图窗口的尺寸
        plt.figure(figsize=(10,6))
        point_numbers = list(range(rw.num_points))
        plt.plot(rw.x_values, rw.y_values, linewidth=500)
        # 突出起点和终点，将点的大小设置为100
        #plt.plot(0,0,c='green',edgecolors='none', s=100)
        plt.plot(rw.x_values[-1], rw.y_values[-1],c='red')
        # 隐藏坐标轴,使用plt.axes()函数将每条坐标轴的可见性都设置为False
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()
        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break
function2()
