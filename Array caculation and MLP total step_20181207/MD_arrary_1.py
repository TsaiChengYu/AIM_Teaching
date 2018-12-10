import numpy as np

A = np.array([8,21])
B = np.array([4,7])
print(A+B)
print(A-B)
print(A*B)
print(A/B)

# weight calc
print(np.dot(A,B))

print("=====================")

A2 = np.array([[1,2],[5,6]])
print(A2.shape)
B2 = np.array([[7,8],[3,3]])
print(B2.shape)

print(np.dot(A2,B2))
