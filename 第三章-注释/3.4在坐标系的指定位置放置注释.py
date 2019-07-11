# 3.4在坐标系的指定位置放置注释
import numpy
import matplotlib.pyplot as plt

'''
plt.text()放置注释
plt.xlabel()横轴下方标签
plt.ylabel()纵轴左侧标签
plt.title()图表上方标题
'''

# 注释如果含有中文字符，一定加下面代码，否则显示乱码或者框框，不显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
X = numpy.linspace(-5,5,1024)
Y = 0.25 * (X + 4) * (X + 1) * (X - 2)
plt.text(-1,-0.3,'新的注释')
# -1,-0.3 表示x轴的区间位置显示后面的注释
plt.title('Power curve')
plt.xlabel('空气速度')
# plt.xlabel('Air speed')
plt.ylabel('Total drag')
plt.plot(X,Y,c='b')
plt.show()


