# 3.5设置文本注释的水平和垂直对齐方式
import matplotlib.pyplot as plt
# va 垂直/上下对齐||center/bottom/top/baseline
# ha 水平/左右对其||center/left/right

# 左右对齐
align_list = ('center','left','right')
for i,align in enumerate(align_list):
    plt.text(0,i,'align=\'%s\'' % align,ha=align)
plt.plot([0,0],[-1,len(align_list)],c = 'r',ls = '--')
plt.scatter([0,0,0],range(len(align_list)))

# 上下对齐
align_list_another = ('center','bottom','top','baseline')
for i,align in enumerate(align_list_another):
    plt.text(3 * i,0,'align=\'%s\'' % align,va=align)
plt.plot([-3,3 * len(align_list_another)],[0,0],c = 'b',ls = '--')
plt.scatter([3 * i for i in range(len(align_list_another))],[0,0,0,0])

# 隐藏坐标轴
ax1 = plt.axes()
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

plt.show()







