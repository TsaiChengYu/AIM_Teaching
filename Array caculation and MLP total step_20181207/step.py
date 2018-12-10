import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp (-x))

def identity_func(x):
    return x

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X,W1)+ B1
Z1 = sigmoid(A1)

print(A1)
print(Z1)
print(Z1.shape)

print("====================")

W2 = np.array([[0.1, 0.5], [0.2, 0.4], [0.8, 0.9]])
B2 = np.array([0.1,0.4])

print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1,W2)+B2
Z2= sigmoid(A2)

print("====================")

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1,0.7])
A3 = np.dot(Z2,W3)+B3
Y1 = identity_func(A3)
Y2 = sigmoid(A3)


print(Y1)
#print(Y2)