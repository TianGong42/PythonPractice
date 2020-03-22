# 数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值
import matplotlib.pyplot as plt
input_vlaue = range(1,5001)
cubes = [x*x*x for x in input_vlaue]
plt.scatter(input_vlaue, cubes,edgecolors='none',c=cubes,cmap=plt.cm.Reds)
plt.axis([0,5001,0,5000*5000*5000])
plt.show()
