# 2.6使用颜色地图（colormap）定制离散点的颜色
import numpy
import matplotlib.cm as cm  # 颜色地图不同的地图在里面定义
import matplotlib.pyplot as plt


N = 256
# 旋转的角度  2pi 一圈，16pi 八圈
angle = numpy.linspace(0,8*2*numpy.pi,N)
# 半径
radius = numpy.linspace(0.5,1,N)
X = radius * numpy.cos(angle)
Y = radius * numpy.sin(angle)
# plt.scatter(X,Y,c = angle,cmap=cm.hsv)
plt.scatter(X,Y,c = angle,cmap=cm.hot)
plt.show()





