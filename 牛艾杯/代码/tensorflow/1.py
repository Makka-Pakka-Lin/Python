from tensorflow.keras import datasets , layers , optimizers , Sequential
import tensorflow as tf


conv_layers = [
    # 5 units of conv + max pooling
    # unit 1
    layers.Conv2D(64, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2,2],strides=2, padding='same' ),
    
    # unit 2
    layers.Conv2D(128, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.Conv2D(128, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2,2],strides=2, padding='same' ),
    
    # unit 3
    layers.Conv2D(256, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.Conv2D(256, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2,2],strides=2, padding='same' ),
    
    # unit 4
    layers.Conv2D(512, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.Conv2D(512, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2,2],strides=2, padding='same' ),
    
    # unit 5
    layers.Conv2D(512, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.Conv2D(512, kernel_size=[3,3],padding = 'same',activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2,2],strides=2, padding='same' ),
]






#加载数据集
def preprocess(x,y):
    x = tf.cast(x,dtype =tf.float32)/255.
    y = tf.cast(y,dtype =tf.int32)
    return x,y




(x,y),(x_test,y_test) = datasets.cifar100.load_data()


train_db = tf.data.Dataset.from_tensor_slices((x,y))
train_db = train_db.shuffle(1000).map(preprocess).batch(64)


test_db = tf.data.Dataset.from_tensor_slices((x_test,y_test))
test_db = test_db.map(preprocess).batch(64)


sample = next(iter(train_db))
print(sample[0].shape,sample[0].shape,tf.reduce_min(sample[0]),tf.reduce_max(sample[0]))


def main():
    conv_net = Sequential(conv_layers)
    #x = tf.random.normal([4,32,32,3])
    #out = conv_net(x)
    #print(out.shape)
    
    #全连接层网络
    fc_net = Sequential([
        layers.Dense(256, activation=tf.nn.relu),
        layers.Dense(128, activation=tf.nn.relu),
        layers.Dense(100, activation=None)
        
    ])


    conv_net.build(input_shape=[None, 32, 32, 3])
    fc_net.build(input_shape=[None, 512] )
    
    #优化器
    optimizer = optimizers.Adam(lr = 1e-4)
    
    #[1,2] + [3,4] =>[1,2,3,4]
    variables = conv_net.trainable_variables + fc_net.trainable_variables
    
    for epoch in range(50):
        for step ,(x,y) in enumerate(train_db):
            with tf.GradientTape() as tape:
                #[b,32,32,3]=>[b,1,1,512]
                out = conv_net(x)
                #[b,1,1,512] =>[b,512]
                out = tf.reshape(out, [-1,512])
                #[b,512]=>[b,100]
                logits = fc_net(out)
                #[b]=>[b,100]
                y_onehot = tf.one_hot(y,depth = 100)
                #计算loss
                loss = tf.losses.categorical_crossentropy(y_onehot , logits , from_logits = True)
                loss = tf.reduce_mean(loss)
            grads = tape.gradient(loss,variables)
            #梯度更新
            optimizer.apply_gradients(zip(grads,variables))
            
            if step %100 == 0:
                print(epoch,step,'loss:',float(loss))
if __name__ =='__main__':
    main()