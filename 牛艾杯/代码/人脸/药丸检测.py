from typing import ItemsView
import cv2
import numpy as np
import os

#判断是否为空胶囊函数
def empty_detection(img_path, img_file, im, im_gray):
    # 判断空胶囊, 需要提取药丸.外壳的轮廓, 先做轮廓
    im_blur = cv2.GaussianBlur(im_gray, (3, 3), 0)
    cv2.imshow("im_blur", im_blur)
    
    #二值化
    ret, im_bin = cv2.threshold(im_gray,
                                210, 255,
                                cv2.THRESH_BINARY)
    cv2.imshow("im_bin", im_bin)   
    
    #查找轮廓
    img, cnts, hie = cv2.findContours(
        im_bin, #图像
        cv2.RETR_CCOMP, #提取两层轮廓
        cv2.CHAIN_APPROX_NONE), #存储所有轮廓坐标点
    #绘制轮廓
    im_cnt = cv2.drawContours(im, cnts, -1,
                              (0, 0, 255), 1)
    cv2.imshow("im_cnt", im_cnt)
    
    #按照周长对轮廓进行过滤
    new_cnts = []
    for i in range(len(cnts)):
        cir_len = cv2.arcLength(cnts[i], True)#计算周长
        #print("cir_len:", cir_len)
        if cir_len > 1000:
            new_cnts.append(cnts[i])
            
    #绘制轮廓
    im_cnt = cv2.drawContours(im, new_cnts, -1,
                              (0, 0, 255), 2)
    cv2.imshow("im_cnt", im_cnt)
    
    if len(new_cnts) == 1:#筛选轮廓
        print("空胶囊:", img_path)
        return True
    else:
        
    
    
    
    
    
    
    
    
    
    
#判断是否为空胶囊函数
def bib_detection(img_path, img_file, im, im_gray):
    pass

#判断是否为空胶囊函数
def balance_detection(img_path, img_file, im, im_gray):
    pass

 
 
 
if __name__ == "__main__":
    # 加载所有图像
    img_dir = "" #图像目录
    img_files = os.listadir(img_dir) #输出所有图像
    
    for img_file in img_files:
        # 拼接完整路径
        img_path = os.path.join(img_dir, img_files)
        if os.path.isdir(img_files):
            continue
            
        #1.读取图像
        im = cv2.imread(img_path)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("im_gray", im_gray)
        
        #2.判断是否是空胶囊(按照判断难度)
        is_empty = False
        is_empty = empty_detection(img_path,
                                   img_file,
                                   im,
                                   im_gray)
        
        #3.判断是否有气泡
        if not is_empty: # 不是空胶囊,在判断没有气泡
            is_bub = bib_detection(img_path,
                                   img_file,
                                   im,
                                   im_gray)
            
        #4.判断是否有大小头
        if (not  is_empty) and (not is_bub): # 不是空胶囊,在判断没有气泡
            balance_detection(img_path,
                                   img_file,
                                   im,
                                   im_gray)
            
        cv2.waitKey()
        cv2.destroyAllWindows()