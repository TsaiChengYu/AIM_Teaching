# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def tan(x):
    return  np.tanh(x)


x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)
y3 = tan(x)

plt.plot(x, y1, "ro")
#plt.plot(x, y2, color="red")
plt.plot(x, y3)
plt.ylim(-0.1, 1.1) #y軸指定
plt.show()
