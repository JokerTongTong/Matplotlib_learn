import matplotlib.pyplot as plt
# 1.1Matplotlib简介(绘制第一个图形)

'''
a = [1,2,3,4]
b = [6,7,8,9]
plt.plot(a,b)
plt.show()
'''

X = range(-100,101)
Y = [x ** 2 for x in X ]
plt.plot(X,Y)
plt.savefig('result.jpg')
plt.show()