# 1.2在数据可视化的过程中使用NumPy（绘制正弦和余弦曲线）

import numpy as np
import math
import matplotlib.pyplot as plt


# 绘制正弦曲线
'''
T = range(100)
X = [(2 * math.pi) * t / len(T) for t in T]
Y = [math.sin(value) for value in X]
Z = [math.cos(value) for value in X]
print(X)
print("---------------------")
print(Y)
plt.plot(X,Y)
plt.plot(X,Z)
plt.show()
'''
X = np.linspace(0, 2 * np.pi, 100) # 把一个范围分成多少份
                                  # 将 0-2pi 分成100份 返回一个numpy数组
# print(type(X))
# print(X)
Y = np.sin(X)
plt.plot(X,Y)
plt.show()
