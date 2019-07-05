# 3.2使用LaTeX格式的标题
'''
LaTex格式概述
是一种基于TEX的排版系统（排版系统的一种排版语言）
提供一个待定格式的字符串，会解析成一个数学公式
Y = 0.25 * (X + 4) * (X + 1) * (X -2)

'''
import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(-4,4,1024)
Y = 0.25 * (X + 4) * (X + 1) * (X -2)
plt.title(r'$f(x) = \frac{1}{4}(x+4)(x+1)(x-2)$')
# frac{1}{4}输入一个分数   1/4
# LaTex格式相关···
plt.plot(X,Y,c = 'b')
plt.show()


