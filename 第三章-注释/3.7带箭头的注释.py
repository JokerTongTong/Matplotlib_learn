# 3.7带箭头的注释
'''
annotate
需要确定箭头注释的4个数据
1.箭头的起始坐标(xytext)
2.箭头的结束坐标(xy)
3.箭头的类型(arrowprops)
4.指定注释的文本
'''
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
X = numpy.linspace(-4,4,1024)
Y = 0.25 * (X + 4) * (X + 1) * (X -2)

'''
xytext文本坐标
箭头坐标
'''
# my_arrowprops = {'arrowstyle':'<->','facecolor':'b','edgecolor':'r'}
my_arrowprops = {'arrowstyle':'<->','edgecolor':'b'}
# my_arrowprops = {'arrowstyle':'<->','facecolor':'0.5'}
plt.annotate('正态分布',xytext=(-1.8,10),xy=(1,-0.2),
             arrowprops=my_arrowprops)

plt.plot(X,Y,c='r')
plt.show()

