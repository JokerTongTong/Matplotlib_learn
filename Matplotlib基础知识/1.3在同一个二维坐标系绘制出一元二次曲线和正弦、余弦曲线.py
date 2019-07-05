# 1.3在同一个二维坐标系绘制出一元二次曲线和正弦、余弦曲线
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-3,3,200)
Y = X ** 2 - 2 * X +1
print(X)
print("-"*20)
print(Y)
plt.plot(X,Y)

newX = np.linspace(0,2 * np.pi ,100)
newY1 = np.sin(newX)
newY2 = np.cos(newX)
plt.plot(newX,newY1)
plt.plot(newX,newY2)

plt.show()