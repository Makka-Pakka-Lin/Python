from keras.optimizers.legacy import RMSprop  # 使用 legacy 版本

# 编译模型时使用 learning_rate 而不是 lr 参数
from keras.utils import to_categorical
from keras import models, layers
from keras.optimizers import RMSprop
from keras.datasets import mnist
import tensorflow as tf
from tensorflow.keras.optimizers import legacy
optimizer = legacy.RMSprop()  # 或者 legacy.RestoredOptimizer()

# 加载MNIST数据集，其中train_images和train_labels是训练集，test_images和test_labels是测试集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 定义LeNet网络结构
def LeNet():
    network = models.Sequential()  # 初始化一个顺序模型
    # 第一层卷积层，6个滤波器，卷积核大小为3x3，激活函数为ReLU，输入图像形状为28x28x1
    network.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    # 第二层：平均池化层，池化窗口大小为2x2
    network.add(layers.AveragePooling2D((2, 2)))
    # 第三层卷积层，16个滤波器，卷积核大小为3x3，激活函数为ReLU
    network.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    # 第四层：平均池化层，池化窗口大小为2x2
    network.add(layers.AveragePooling2D((2, 2)))
    # 第五层卷积层，120个滤波器，卷积核大小为3x3，激活函数为ReLU
    network.add(layers.Conv2D(filters=120, kernel_size=(3, 3), activation='relu'))
    # 第六层：展平层，将三维特征图展平为一维
    network.add(layers.Flatten())
    # 第七层：全连接层，有84个神经元，激活函数为ReLU
    network.add(layers.Dense(84, activation='relu'))
    # 第八层：输出层，有10个神经元（对应10个类别），激活函数为softmax，用于多分类
    network.add(layers.Dense(10, activation='softmax'))
    return network

# 实例化LeNet模型
network = LeNet()

# 编译模型，使用RMSprop优化器，损失函数为categorical_crossentropy，多分类问题，度量指标为accuracy
network.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# 预处理数据，将图像数据reshape为28x28x1（灰度图），并归一化到[0, 1]区间
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float') / 255

# 将标签转换为one-hot编码形式
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 训练网络，使用fit函数进行训练，epochs表示训练的回合数，batch_size表示每批次处理的样本数，verbose设置输出日志
network.fit(train_images, train_labels, epochs=10, batch_size=128, verbose=2)

# 评估模型在测试集上的性能，返回测试集的损失值和准确率
test_loss, test_accuracy = network.evaluate(test_images, test_labels)
print("test_loss:", test_loss, "test_accuracy:", test_accuracy)

# 保存模型为H5格式
network.save('MyModel.h5')

# 保存模型为TensorFlow Lite格式
keras_file = 'MyModel.h5'
tf.keras.models.save_model(network, keras_file)  # 保存模型
model = tf.keras.models.load_model(keras_file)  # 加载保存的模型
converter = tf.lite.TFLiteConverter.from_keras_model(model)  # 创建TensorFlow Lite模型转换器
tflite_model = converter.convert()  # 转换为TensorFlow Lite模型格式

# 将转换后的模型保存为.tflite文件
with open('MyModel.tflite', 'wb') as f:
    f.write(tflite_model)