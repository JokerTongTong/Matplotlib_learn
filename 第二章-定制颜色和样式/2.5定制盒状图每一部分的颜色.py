# 2.5定制盒状图每一部分的颜色
import random
import matplotlib.pyplot as plt
'''
高斯分布
gauss(num1,num2)
num1:平均值
num2:标准差
'''
# 0 是平均值    1 是标准差
values = [random.gauss(0,1) for i in range(100)]
# print(values)
b = plt.boxplot(values)
colorList = ['r','b','g','y']
i = 0
for name,line_list in b.items():
    # print(name)
    # print(line_list)
    # print("****"*10)
    color = colorList[i % len(colorList)]
    i += 1
    for line in line_list:
        line.set_color(color)

plt.show()






