# 绘制折线图
import matplotlib.pyplot as plt
from matplotlib import font_manager
input_values = ["0110-0116","0117-0123","0124-0130","0131-0206","0207-0213",
"0214-0220"]
squares1 = [2384933,2173209,697201,669763,718213,1000800]
squares2 = [41177,30719,4854,6116,7900,15601]
squares3 = [35241,27638,5589,13300,9488,11493]
def showp(input_values,squares,title,name):
    plt.plot(input_values, squares, linewidth=5)  #调用plot函数，生成图片
    # 设置图表标题，并给坐标加上标签
    zh_font = font_manager.FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)
    plt.title(title, fontsize = 24,fontproperties=zh_font)
    plt.xlabel("日期", fontsize=14, fontproperties=zh_font)
    plt.ylabel(name, fontsize=14, fontproperties=zh_font)
    # 设置可读标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.show()
    #plt.savefig("squares_plot1.png",bbox_inches='tight')
showp(input_values,squares1,"发票开具数量","开具数量")
showp(input_values,squares2,"发票作废数量","作废数量")
showp(input_values,squares3,"发票红冲数量","红冲数量")
