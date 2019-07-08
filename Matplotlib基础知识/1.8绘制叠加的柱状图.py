# 1.8绘制叠加的柱状图

import matplotlib.pyplot as plt
import numpy

A = [5,30,45,22]
B = [5,25,50,20]

'''
X = range(4)
plt.bar(X,A,color='b')
plt.bar(X,B,color='r',bottom=A)   # B抬高到A上面
plt.show()
'''

data = numpy.array([[5,30,45,22],
                   [5,25,50,20],
                   [1,4,5,2]])
color_list = ['b','g','r']
X = numpy.arange(data.shape[1])
for i in range(data.shape[0]):
    print(data[:i])
    S = numpy.sum(data[:i],axis=0) # axis=0 计算列的和
    print("-"*30)
    print(S)
    print("=" * 30)
    # bottom代表从底部什么坐标开始展示当前段的数据，因为是叠加，所以S的值每一次都上升
    plt.bar(X,data[i],bottom=S,color=color_list[i%len(color_list)])
plt.show()