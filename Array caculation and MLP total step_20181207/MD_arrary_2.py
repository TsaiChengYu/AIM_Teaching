import numpy as np

A = np.array([1,2,3,5])
print(A)
print(np.ndim(A))
print(A.shape)
print("======================")

B = np.array([[1,2,3],[3,4,5],[2,2,1],[3,4,3],[1,2,3]])
print(B)
print(np.ndim(B))
print(B.shape)
print("======================")

C = np.array([[[100,0],[0,0],[0,100]],[[0,50],[50,0],[0,0]],
              [[100,0],[0,0],[0,100]],[[0,50],[50,0],[0,0]]])
print(C)
print(np.ndim(C))
print(C.shape)
print("======================")
