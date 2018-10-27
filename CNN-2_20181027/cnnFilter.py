

from scipy.signal import  convolve2d
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# method
def show_diff(image, kernel):
    con = convolve2d(image,kernel)
    fig = plt.figure(figsize=(8,8))
    plt.subplot(121)
    plt.title("original")
    plt.axis("off")
    plt.imshow(image,cmap="gray")

    plt.subplot(122)
    plt.title("After")
    plt.axis("off")
    plt.imshow(con, cmap="gray")
    plt.show()
    return con


# load image
pic_gray = np.array(Image.open("dog.jpg").convert("L"))

print(pic_gray)
plt.imshow(pic_gray, cmap="gray")
plt.show()

# create a filter
kernel = np.array([[1,0,1],[-2,0,-2],[-1,0,1]], np.float32)
dx = show_diff(pic_gray,kernel)


