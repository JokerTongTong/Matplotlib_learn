# 1.5绘制随机点

# plot 将所有的点连成一条曲线
# scatter 绘制随机点

import random
import matplotlib.pyplot as plt

count = 1024
X = [random.random() * 100 for i in range(count)]
Y = [random.random() * 100 for i in range(count)]
print(X)
print(Y)
plt.scatter(X,Y)
plt.show()
