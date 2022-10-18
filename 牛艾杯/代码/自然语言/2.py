from tensorflow.keras.datasets import mnist
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
(train_images,train_label),(test_images,test_labels)=mnist.load_data()
train_images = np.reshape(train_images,(train_images.shape[0],train_images.shape[1],train_images.shape[2],1))
test_images = np.reshape(test_images,(test_images.shape[0],test_images.shape[1],test_images.shape[2],1))
def get_train(size):
    index = np.random.randint(0,train_images.shape[0],size)
    resized_image = tf.image.resize_with_pad(train_images[index],227,227)
    return resized_image.numpy(),train_label[index]
def get_test(size):
    index = np.random.randint(0,train_images.shape[0],size)
    resized_image = tf.image.resize_with_pad(train_images[index],227,227)
    return resized_image.numpy(),train_label[index]
train_images,train_label = get_train(256)
test_images,test_labels = get_test(128)
plt.imshow(train_images[4].astype(np.int8).squeeze(),cmap='gray')
    