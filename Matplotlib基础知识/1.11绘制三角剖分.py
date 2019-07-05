# 1.11绘制三角剖分
# n个点连接线，分成若干个三角形
import random
import matplotlib.pyplot as plt
import matplotlib.tri as tri

'''
count = 4
X = [1,2,3,4]
Y = [1,5,0,1]
triangles = tri.Triangulation(X,Y)
plt.triplot(triangles,'r-')
    # triangles 划分的三角形
    # 'r-'颜色线，此处为red红色，-直线(-- 这代表虚线)
plt.show()
'''
count = 100
X = [random.random()*20 for i in range(count)]
Y = [random.random()*2 for i in range(count)]
triangles = tri.Triangulation(X,Y)
plt.triplot(triangles,'r-')
    # triangles 划分的三角形
    # 'r-'颜色线，此处为red红色，-直线
plt.show()

