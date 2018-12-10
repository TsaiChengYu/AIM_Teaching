import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp (-x))
def init_network():
    network={}
    network["w1"] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
    network["b1"] =np.array([0.1, 0.2, 0.3])
    network["w2"] =np.array([[0.1, 0.5], [0.2, 0.3], [0.3, 0.6]])
    network["b2"] =np.array([0.3, 0.5])
    network["w3"] =np.array([[0.5, 0.7],[0.3, 0.4]])
    network["b3"] =np.array([0.2, 0.5])
    return network
def forward(network,x):
    W1,W2,W3 = network["w1"],network["w2"],network["w3"]
    B1,B2,B3 = network["b1"],network["b2"],network["b3"]

    a1 = np.dot(x,W1)+B1
    z1 = sigmoid(a1)
    a2 = np.dot (z1, W2) + B2
    z2 = sigmoid (a2)
    a3 = np.dot (z2, W3) + B3
    z3 = sigmoid (a3)

    y= identity_func(z3)
    return y
def identity_func(x):
    return x

if __name__ == '__main__':
    network = init_network()
    x=np.array([1.0,0.5])
    y=forward(network,x)
    print(y)