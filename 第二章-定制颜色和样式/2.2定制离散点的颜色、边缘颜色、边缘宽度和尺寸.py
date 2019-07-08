# 2.2定制离散点的颜色、边缘颜色、边缘宽度和尺寸
import numpy
import matplotlib.pyplot as plt

'''
numpy.random.standard_normal((a,b))
standard_normal()为创建正态分布随机值
    参数为元组，a为产生随机数的个数，b为几维
'''
A = numpy.random.standard_normal((100,2))  # 正态分布，二维，100个点
print(A)
# print(A[:,0])
A += numpy.array((-1,-1))
print(A)

B = numpy.random.standard_normal((100,2))
B += numpy.array((1,1))
colors = ['r','yellow','b','c','#FF00FF','0.75']
plt.scatter(A[:,0],A[:,1],color=colors[0])
plt.scatter(B[:,0],B[:,1],color=colors[2])
plt.scatter(A[:,0],B[:,1],color=colors[4],edgecolor=colors[2],s=200,linewidth=3)
# edgecolor:边缘色,
# s:像素，大小
# linewidth:边缘的线宽度
plt.show()