# 2.10在曲线上建立步长标记
# 在曲线上每隔一段距离加一个标记

import numpy
import matplotlib.pyplot as plt
'''
markevery = int
传入一个int值
每相隔一段距离做一个标记，这段距离指的是横轴坐标
'''

X = numpy.linspace(-6,6,1024)
Y1 = numpy.sinc(X) # 辛格函数 sinc(X) = sin(X) / X
Y2 = numpy.sinc(X) + 1
plt.plot(X,Y1,marker='x',color='r',markevery=50)
plt.plot(X,Y2,marker='o',color='b',markevery=32)
plt.show()





