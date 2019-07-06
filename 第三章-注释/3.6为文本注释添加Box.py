# 3.6为文本注释添加Box
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
X = numpy.linspace(-5,5,1024)
Y = 0.25 * (X + 4) * (X + 1) * (X -2)
box = {
    'facecolor':'0.75',   # 背景色
    'edgecolor':'b',    # 盒子边框颜色
    'boxstyle':'round',  # 盒子的样式  圆角
}
plt.text(-0.5,-0.2,'abcde',bbox = box)
plt.plot(X,Y,c='r')
plt.show()

