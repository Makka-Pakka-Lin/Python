#*训练好的模型做识别*
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.preprocessing import image
from picture import *
 
# 加载tflite文件模型
tflite_model = tf.lite.Interpreter(model_path="MyModel.tflite")
tflite_model.allocate_tensors()
 
# 获取输入和输出张量
input_details = tflite_model.get_input_details()
output_details = tflite_model.get_output_details()

cv2.imwrite("77.jpg",bit_img)
image_path_test = '77.jpg'#图片路径

#加载图片至内存中并resize和增加维度
img = image.load_img(image_path_test, target_size=(28, 28))
img = image.img_to_array(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.expand_dims(img, 2)
#print(img.shape)#这里直接打印将img转换为数组后的数据维度 (28,28,1)
img = np.expand_dims(img, axis=0)#因为模型的输入是要求四维的，所以我们需要将输入图片增加一个维度，使用 expand_dims接口

#模型预测
tflite_model.set_tensor(input_details[0]['index'], img)
tflite_model.invoke()

output_data = tflite_model.get_tensor(output_details[0]['index'])
print(output_data)

#读取标签文件，返回列表
def read_label_list():
    with open('label.txt', 'r',encoding="utf8") as f:
        data = f.read().splitlines()
    return data

#标签预测
#print(read_label_list())
w = np.argmax(output_data)#值最大的位置
lable_list = read_label_list()#读取标签列表
print(lable_list[w])