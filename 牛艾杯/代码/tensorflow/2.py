import tensorflow as tf
tf.compat.v1.disable_eager_execution()#保证sess.run()能够正常运行
hello = tf.constant("hello,world!")#定义一个常量(张量)
sess = tf.compat.v1.Session() #创建一个session,用来执行操作
print(sess.run(help))#调用session的run方法执行hello操作,并打印结果
sess.close()#关闭session
