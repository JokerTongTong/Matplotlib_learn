# 2.9控制离散点的标记样式
# 默认是一个圆点儿，可以改变样式


import matplotlib.pyplot as plt
import numpy


A = numpy.random.standard_normal((100,2))
print(A)
# print(A[:,0])
A += numpy.array((-1,-1))
print(A)

'''
standard_normal(size=None)
从标准正太分布中绘制样本(均值=0，stdev=1)
参数size：int 或 int的元组，可选
    默认为None：返回一个float
    传入int类型的数，返回一个一维数组，元素个数为8000
    传入int元组(a,b,c,d,e),返回一个数组，数组.shape = (a,b,c,d,e)
'''
B = numpy.random.standard_normal((100,2))
B += numpy.array((1,1))
colors = ['r','yellow','b','c','#FF00FF','0.75']
plt.scatter(A[:,0],A[:,1],color=colors[0],marker='x')
plt.scatter(B[:,0],B[:,1],color=colors[2],marker='^')
plt.scatter(A[:,0],B[:,1],color=colors[4],edgecolor=colors[2],s=200,linewidth=1,marker='*')
# edgecolor:边缘色,
# s:像素，大小
# linewidth:边缘的线宽度
# marker:离散点样式
    # * x ^

plt.show()










