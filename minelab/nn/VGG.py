import tensorflow as tf

import numpy as np
from functools import reduce

VGG_MEAN = [103.939, 116.779, 123.68]
def inference(RGBData,label_size,train_mode=True,trainable=True, dropout=0.5,rgb_channel_size=3,image_width = 224,\
              image_high = 224,conv1_deep= 64,conv2_deep= 128,conv3_deep= 256,conv4_deep= 512,conv5_deep= 512,\
              fc6_size=4096,fc7_size=4096,kernal_size=3,max_pool_size=[1, 2, 2, 1],\
              max_pool_strides=[1,2,2,1],conv_strides=[1,1,1,1]):
    '''
    :param RGBData:RGB图片数据
    :param label_size:
    :param train_mode:训练模式，如果为true，开启dropout
    :param trainable:是否是训练模式，默认是
    :param dropout:dropout值
    :param rgb_channel_size:图片通道数
    :param image_width:图片宽度
    :param image_high:图片长度
    :param conv1_deep:第一层卷积核通道数
    :param conv2_deep:第二层卷积核通道数
    :param conv3_deep:第三层卷积核通道数
    :param conv4_deep:第四层卷积核通道数
    :param conv5_deep:第五层卷积核通道数
    :param fc6_size:第六层全连接层输出神经元个数
    :param fc7_size:第七层全连接层输出神经元个数
    :param kernal_size:卷积核大小
    :param max_pool_size:池化层大小
    :param max_pool_strides:池化层步长
    :param conv_strides:卷积核步长
    :return:predictValue,预测分类值
    '''
    # rgb_scaled = RGBData * 255.0
    # # Convert RGB to BGR
    # red, green, blue = tf.split(axis=rgb_channel_size, num_or_size_splits=rgb_channel_size, value=rgb_scaled)
    # assert red.get_shape().as_list()[1:] == [image_width, image_high, 1]
    # assert green.get_shape().as_list()[1:] == [image_width, image_high, 1]
    # assert blue.get_shape().as_list()[1:] == [image_width, image_high, 1]
    # bgr = tf.concat(axis=rgb_channel_size, values=[
    #     blue - VGG_MEAN[0],
    #     green - VGG_MEAN[1],
    #     red - VGG_MEAN[2],
    # ])
    # assert RGBData.get_shape().as_list()[1:] == [image_width, image_high, rgb_channel_size]

    conv1_1 = conv_layer(RGBData, rgb_channel_size, conv1_deep, "conv1_1",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv1_2 = conv_layer(conv1_1, conv1_deep, conv1_deep, "conv1_2",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    pool1 = max_pool(conv1_2, 'pool1')

    conv2_1 = conv_layer(pool1, conv1_deep, conv2_deep, "conv2_1",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv2_2 = conv_layer(conv2_1, conv2_deep, conv2_deep, "conv2_2",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    pool2 = max_pool(conv2_2, 'pool2')

    conv3_1 = conv_layer(pool2, conv2_deep, conv3_deep, "conv3_1",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv3_2 = conv_layer(conv3_1, conv3_deep, conv3_deep, "conv3_2",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv3_3 = conv_layer(conv3_2, conv3_deep, conv3_deep, "conv3_3",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv3_4 = conv_layer(conv3_3, conv3_deep, conv3_deep, "conv3_4",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    pool3 = max_pool(conv3_4, 'pool3')

    conv4_1 = conv_layer(pool3, conv3_deep, conv4_deep, "conv4_1",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv4_2 = conv_layer(conv4_1, conv4_deep, conv4_deep, "conv4_2",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv4_3 = conv_layer(conv4_2, conv4_deep, conv4_deep, "conv4_3",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv4_4 = conv_layer(conv4_3, conv4_deep, conv4_deep, "conv4_4",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    pool4 = max_pool(conv4_4, 'pool4',max_pool_size=max_pool_size)

    conv5_1 = conv_layer(pool4, conv4_deep, conv5_deep, "conv5_1",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv5_2 = conv_layer(conv5_1, conv5_deep, conv5_deep, "conv5_2",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv5_3 = conv_layer(conv5_2, conv5_deep, conv5_deep, "conv5_3",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    conv5_4 = conv_layer(conv5_3, conv5_deep, conv5_deep, "conv5_4",trainable=trainable,kernal_size=kernal_size,strides=conv_strides)
    pool5 = max_pool(conv5_4, 'pool5',max_pool_size=max_pool_size,strides=max_pool_strides)

    pool_shape = pool5.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    fc6 = fc_layer(pool5, nodes, fc6_size, "fc6",trainable=trainable)  # 25088 = ((224 // (2 ** 5)) ** 2) * 512
    relu6 = tf.nn.relu(fc6)
    if train_mode is not None:
        relu6 = tf.cond(train_mode, lambda: tf.nn.dropout(relu6, dropout), lambda: relu6)
    elif trainable:
        relu6 = tf.nn.dropout(relu6, dropout)
    fc7 = fc_layer(relu6, fc6_size, fc7_size, "fc7",trainable=trainable)
    relu7 = tf.nn.relu(fc7)
    if train_mode is not None:
        relu7 = tf.cond(train_mode, lambda: tf.nn.dropout(relu7, dropout), lambda: relu7)
    elif trainable:
        relu7 = tf.nn.dropout(relu7, dropout)

    fc8 = fc_layer(relu7, fc7_size, label_size, "fc8",trainable=trainable)
    predictValue = tf.nn.softmax(fc8, name="prob")
    return predictValue

def max_pool(bottom, name,max_pool_size=[1,2,2,1],strides=[1,2,2,1]):
    return tf.nn.max_pool(bottom, ksize=max_pool_size, strides=strides, padding='SAME', name=name)

def conv_layer(bottom, in_channels, out_channels, name,trainable=True,kernal_size=3,strides=[1, 1, 1, 1]):
    with tf.variable_scope(name):
        filt, conv_biases = get_conv_var(kernal_size, in_channels, out_channels, name,trainable=trainable)
        conv = tf.nn.conv2d(bottom, filt, strides, padding='SAME')
        bias = tf.nn.bias_add(conv, conv_biases)
        relu = tf.nn.relu(bias)

        return relu

def fc_layer(bottom, in_size, out_size, name,trainable=True):
    with tf.variable_scope(name):
        weights, biases = get_fc_var(in_size, out_size, name,trainable=trainable)
        x = tf.reshape(bottom, [-1, in_size])
        fc = tf.nn.bias_add(tf.matmul(x, weights), biases)

        return fc
def get_conv_var(filter_size, in_channels, out_channels, name,trainable=True):
    initial_value = tf.truncated_normal([filter_size, filter_size, in_channels, out_channels], 0.0, 0.001)
    filters = get_var(initial_value, name + "_filters",trainable=trainable)
    initial_value = tf.truncated_normal([out_channels], .0, .001)
    biases = get_var(initial_value, name + "_biases",trainable=trainable)

    return filters, biases

def get_fc_var(in_size, out_size, name,trainable=True):
    initial_value = tf.truncated_normal([in_size, out_size], 0.0, 0.001)
    weights = get_var(initial_value,name + "_weights",trainable=trainable)

    initial_value = tf.truncated_normal([out_size], .0, .001)
    biases = get_var(initial_value,name + "_biases",trainable=trainable)

    return weights, biases

def get_var(initial_value, var_name,trainable=True):
    value = initial_value
    var = tf.Variable(value, name=var_name)
    # if trainable:
    #     var = tf.Variable(value, name=var_name)
    # else:
    #     var = tf.constant(value, dtype=tf.float32, name=var_name)

    # print var_name, var.get_shape().as_list()
    assert var.get_shape() == initial_value.get_shape()

    return var
def save_npy(sess,var_dict,npy_path="./vgg19-save.npy"):
    assert isinstance(sess, tf.Session)

    data_dict = {}

    for (name, idx), var in list(var_dict.items()):
        var_out = sess.run(var)
        if name not in data_dict:
            data_dict[name] = {}
        data_dict[name][idx] = var_out

    np.save(npy_path, data_dict)
    print(("file saved", npy_path))
    return npy_path

