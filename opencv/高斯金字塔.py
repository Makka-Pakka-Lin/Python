import numpy as np
import cv2
import matplotlib.pyplot as plt
def gaussian(original_image,down_times=5):
    temp = original_image.copy()
    gaussian_pyramid = [temp]
    for i in range(down_times):
        temp = cv2.pyrDown(temp)
        gaussian_pyramid.append(temp)
    return gaussian_pyramid
if __name__ == "__main__":
    a = cv2.imread("./NO3.jpg", -1)
    gaussian_pyramid = gaussian(a, down_times=5)
    plt.subplot(2, 3, 1), plt.imshow(a, cmap='gray')
    plt.subplot(2, 3, 2), plt.imshow(gaussian_pyramid[2], cmap='gray')
    plt.subplot(2, 3, 3), plt.imshow(gaussian_pyramid[4], cmap='gray')
    cv2.imwrite("1.jpg",a)
    cv2.imwrite("2.jpg", gaussian_pyramid[0])
    cv2.imwrite("3.jpg", gaussian_pyramid[1])
    cv2.imwrite("4.jpg", gaussian_pyramid[2])
    cv2.imwrite("5.jpg", gaussian_pyramid[3])
    cv2.imwrite("6.jpg", gaussian_pyramid[4])
    cv2.imwrite("7.jpg", gaussian_pyramid[5])
    plt.show()
    gaussian_pyramid[4].save("1.jpg")
    print(gaussian_pyramid[0].shape, gaussian_pyramid[1].shape, gaussian_pyramid[5].shape)
