# 1.9在同一个窗口绘制直方图和盒状图
# 直方图与柱状图类似，柱状图主要关注X/Y值
# 直方图主要关注趋势
import numpy as np
import matplotlib.pyplot as plt

'''
hist:绘制直方图
    hist(data,value)
        data列表 同时也是x轴的值, value 平均分成多少份来显示
        example:
            hist([-1,1],100) 将-1到1这个区间等分成100份
boxplot:绘制盒状图
    boxplot(data)  看数据主要集中在哪个区域，可以看平均线
    
'''

data = np.random.randn(100)
print(data)
print(np.average(data))

# 分成网格
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,4))
    # 窗口，1行，2列 figsize(800*400)
print(fig)
ax1.hist(data,100)
ax2.boxplot(data)
plt.show()
