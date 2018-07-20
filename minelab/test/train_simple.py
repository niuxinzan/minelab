"""
Simple tester for the vgg19_trainable
"""

import tensorflow as tf

import minelab.test.utils as utils
import  minelab.nn.LeNet5 as lenet5
#define X
img = utils.load_image("./img-guitar-224x224.jpg")
#define Y
img_true_result = [1 if i == 1 else 0 for i in range(2)]

batch = img.reshape((1, 224, 224, 3))

# 初始化tensorflow
images = tf.placeholder(tf.float32, [1, 224, 224, 3])
true_out = tf.placeholder(tf.float32, [1, 2])
train_mode = tf.placeholder(tf.bool)

rgb_scaled = images * 255.0
# Convert RGB to BGR
red, green, blue = tf.split(axis=3, num_or_size_splits=3, value=rgb_scaled)
assert red.get_shape().as_list()[1:] == [224, 224, 1]
assert green.get_shape().as_list()[1:] == [224, 224, 1]
assert blue.get_shape().as_list()[1:] == [224, 224, 1]
VGG_MEAN = [103.939, 116.779, 123.68]
bgr = tf.concat(axis=3, values=[
    blue - VGG_MEAN[0],
    green - VGG_MEAN[1],
    red - VGG_MEAN[2],
])

# prob=vgg19.inference(images,2,train_mode=train_mode)
prob=lenet5.inference(images,2,num_channels=3)
prob = tf.nn.softmax(prob, name="prob")

cost = tf.reduce_sum((prob - true_out) ** 2)
train = tf.train.GradientDescentOptimizer(0.0001).minimize(cost)

pred_max =tf.argmax(prob, 1)
y_max =tf.argmax([img_true_result], 1)
correct_pred = tf.equal(pred_max, y_max)
accuracy=tf.reduce_mean(tf.cast(correct_pred, tf.float32))

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    step = 1
    print("Start  training!")
    while step < 2:
        sess.run(train,feed_dict={images: batch, true_out: [img_true_result], train_mode: True})
        accuracy1 =sess.run(accuracy,feed_dict={images: batch, true_out: [img_true_result], train_mode: False})
        print("accuracy1",accuracy1)
    saver.save(sess, "./accuracy1")
