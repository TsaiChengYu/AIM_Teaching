from keras import backend as K
from keras.models import  Sequential
from keras.layers.core import Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def show_img(model,img):
    plt.figure(figsize=(8,8))
    img_batch = np.expand_dims(img, axis=0)
    conv_img = model.predict(img_batch)
    conv_img = np.squeeze(conv_img, axis=0)
    print(conv_img.shape)
    conv_img = conv_img.reshape(conv_img.shape[:2])
    plt.imshow(conv_img)
    plt.show()


pic = np.array(Image.open("dog.jpg"))
plt.imshow(pic)
plt.show()

# follow the CNN process
model = Sequential()
model.add(Conv2D(3, (3,3),padding="same",
                 data_format= "channels_last",
                 activation= "relu",
                 input_shape=pic.shape ))

print(model.summary())

# input the image to CNN
dog_batch = np.expand_dims(pic, axis=0)
print(dog_batch.shape)
conv_dog = model.predict(dog_batch)
print(conv_dog.shape)
img = np.squeeze(conv_dog,axis=0)
print(img.shape)
plt.imshow(img)
plt.show()

# try to remove the RGB
model2 = Sequential()
model2.add(Conv2D(1,
                  (3,3),
                 padding="same",
                 data_format= "channels_last",
                 input_shape= pic.shape ))
show_img(model2,pic)


model3 = Sequential()
model3.add(Conv2D(1,(3,3),
                 padding="same",
                 data_format= "channels_last",
                 input_shape= pic.shape ))
model3.add(MaxPooling2D(pool_size=(20,20),data_format="channels_last"))
show_img(model3,pic)
