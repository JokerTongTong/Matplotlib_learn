# 3.1在坐标系上显示标题（英文和中文）
import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-4,4,1024)
Y = 0.25 * (X + 4) * (X + 1) * (X -2)
# plt.title('A ploynomial') # 添加(英文)标题
# 添加(中文)标题  需要加一行代码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('多项式曲线')
plt.plot(X,Y,c='r')
plt.show()







