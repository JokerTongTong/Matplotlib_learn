# 1.9在同一个窗口绘制直方图和盒状图
# 直方图与柱状图类似，柱状图主要关注X/Y值
# 直方图主要关注趋势
'''
1.直方图展示数据的分布，柱状图比较数据的大小。
2.直方图X轴为定量数据，柱状图X轴为分类数据。
    因此，直方图上的每根柱子都是不可移动的，X轴上的区间是连续的、固定的。
    而柱状图上的每根柱子是可以随意排序的，有的情况下需要按照分类数据的名称排列，
    有的则需要按照数值的大小排列。
3.直方图柱子无间隔，柱状图柱子有间隔
4.直方图柱子宽度可不一，柱状图柱子宽度须一致。
    柱状图柱子的宽度因为没有数值含义，所以宽度必须一致。
    但是在直方图中，柱子的宽度代表了区间的长度，根据区间的不同，
    柱子的宽度可以不同，但理论上应为单位长度的倍数。
'''
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

data = np.random.randn(100)  # 100个正太分布的随机值
print(data)
print(np.average(data))

# 分成网格
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,4))
    # 窗口，1行，2列 figsize(800*400)
print(fig)
ax1.hist(data,100)
ax2.boxplot(data)
plt.show()
