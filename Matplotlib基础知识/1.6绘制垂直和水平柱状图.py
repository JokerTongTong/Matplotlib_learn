# 1.6绘制垂直和水平柱状图
# 垂直/水平 柱状图
# bar 垂直
# barh 水平


import matplotlib.pyplot as plt
# bar(X,Y) X横坐标，Y纵坐标(值)
data = [30,53,12,45]
# X = [0,1,2,3]
# Y = [30,53,12,45]
# plt.bar(range(len(data)),data)
# plt.barh([1980,1988,1997,2001],[2000,3894,1999,5000],height=3)

hdata = [30,53,12,45]
plt.barh(range(len(hdata)),hdata)

plt.show()
