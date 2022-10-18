import cv2

img = cv2.imread('./2.jpg')
g0 = img

g1 = cv2.pyrDown(g0)  # 计算下采样

laplacian0 = g0 - cv2.pyrUp(g1)  # 计算拉普拉斯

# 通过拉普拉斯还原原图像
origin = laplacian0 + cv2.pyrUp(g1)

cv2.imshow('g0', g0)
cv2.imshow('origin', origin)
cv2.imwrite('13579.jpg',origin)
cv2.waitKey()
cv2.destroyAllWindows()

