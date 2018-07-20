# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 14:13
# @Author  : buf
# @Email   : niuxinzan@cennavi.com.cn
# @File    : LeNet5.py
# @Software: PyCharm
import tensorflow as tf

# LeNet5网路结构
def inference(input_tensor,num_labels,regularizer=None,num_channels=1, trainFlag=True, conv1_deep= 32,conv1_size= 5,
              conv2_deep= 64,conv2_size= 5,fc_size= 512,dropout= 0.7):
    '''
    :param input_tensor:输入图片
    :param trainFlag:是不是训练过程，是为True
    :param regularizer:正则化
    :param num_channels:图片通道数
    :param num_labels:标签类型数
    :param conv1_deep:第一层卷积核个数
    :param conv1_size:第一层卷积核大小
    :param conv2_deep:第二层卷积核个数
    :param conv2_size:第二层卷积核大小
    :param fc_size:全连接层大小
    :param dropout:dropout大小
    :return:logit:预测值
    '''
    with tf.variable_scope("layer1-conv1"):
        conv1_weights = tf.get_variable(
            "weight", [conv1_size, conv1_size, num_channels, conv1_deep],
            initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable("bias", [conv1_deep], initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))
    with tf.name_scope("layer2-pool1"):
        pool1= tf.nn.max_pool(relu1,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")
    with tf.variable_scope("layer3-conv2"):
        conv2_weights=tf.get_variable("weight",[conv2_size,conv2_size,conv1_deep,conv2_deep],initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2_biases=tf.get_variable("bias",[conv2_deep],initializer=tf.truncated_normal_initializer(0.0))
        conv2=tf.nn.conv2d(pool1,conv2_weights,strides=[1,1,1,1],padding="SAME")
        relu2=tf.nn.relu(tf.nn.bias_add(conv2,conv2_biases))
    with tf.name_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        pool_shape = pool2.get_shape().as_list()
        nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
        reshaped = tf.reshape(pool2, [-1, nodes])
    with tf.variable_scope('layer5-fc1'):
        fc1_weights = tf.get_variable("weight", [nodes, fc_size],initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable("bias", [fc_size], initializer=tf.constant_initializer(0.1))
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if trainFlag:
            fc1 = tf.nn.dropout(fc1, dropout)
    with tf.variable_scope('layer6-fc2'):
        fc2_weights = tf.get_variable("weight", [fc_size, num_labels],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [num_labels], initializer=tf.constant_initializer(0.1))
        logit = tf.matmul(fc1, fc2_weights) + fc2_biases

    return logit