# 2.4用颜色集合定制饼图颜色
import random
import matplotlib.pyplot as plt


values = [random.random() for i in range(15)]
color_set = ['r','b','y','0.5','#F0F0F9']
plt.pie(values,colors=color_set)
# 注意参数 colors   有s
plt.show()


