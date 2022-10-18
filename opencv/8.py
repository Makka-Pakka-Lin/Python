# 博主微信/QQ 2487872782
# 有问题可以联系博主交流
# 有图像处理需求也可联系博主
# 图像处理技术交流QQ群 271891601

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# OpenCV的版本为4.1

import cv2 as cv

src = cv.imread("./NO3.jpg")

G_0 = src  # 第0层高斯金字塔实际上就是原图像
print('第0层高斯金字塔图像的尺寸：{}'.format(src.shape[:2]))
cv.imshow("G_0", src)

# 生成第1层高斯金字塔G_1
G_1 = cv.pyrDown(G_0)
print('第1层高斯金字塔图像的尺寸：{}'.format(G_1.shape[:2]))
cv.imshow("G_1 ", G_1)

# 为了计算第0层拉普拉斯金字塔，我们需要先计算出Pyrup(G_1)
Pyrup_G_1 = cv.pyrUp(G_1)
print('第1层高斯金字塔进行上采样+高斯卷积模糊滤波后的尺寸：{}'.format(Pyrup_G_1.shape[:2]))
cv.imshow("Pyrup_G_1", Pyrup_G_1)

# 计算第0层拉普拉斯金字塔图像，L_0=G_0-Pyrup(Pyrdown(G_0))
L_0 = cv.subtract(G_0, Pyrup_G_1, dst=None, mask=None, dtype=cv.CV_16S)
print('第0层拉普拉斯金字塔的尺寸：{}'.format(L_0.shape[:2]))

# 以下几行代码是显示出第0层拉普拉斯金字塔的图像
L_0_norm = L_0
cv.normalize(L_0, L_0_norm, 0, 255, cv.NORM_MINMAX)
L_0_norm = L_0_norm.astype('uint8')
L_0_norm_gray = cv.cvtColor(L_0_norm, cv.COLOR_BGR2GRAY)
cv.imshow("L_0_norm_gray", L_0_norm_gray)

# 利用第1层高斯金字塔图像和第0层拉普拉斯金字塔图像重构第0层高斯金字塔
# 第0层高斯金字塔实际上就是原图
G_0_reconstruction = cv.add(Pyrup_G_1, L_0, dst=None, mask=None, dtype=cv.CV_16S)
cv.normalize(G_0_reconstruction, G_0_reconstruction, 0, 255, cv.NORM_MINMAX)
G_0_reconstruction = G_0_reconstruction.astype('uint8')
print('重构的第0层高斯金字塔图像的尺寸：{}'.format(G_0_reconstruction.shape[:2]))
cv.imshow("G_0_reconstruction", G_0_reconstruction)

cv.waitKey()

