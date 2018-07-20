# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 11:40
# @Author  : buf
# @Email   : niuxinzan@cennavi.com.cn
# @File    : test001.py
# @Software: PyCharm
import tensorflow as tf
a=tf.constant(2)
b=tf.constant(3)
x=tf.constant(4)
y=tf.constant(5)
z = tf.multiply(a, b)
result = tf.cond(x > y, lambda: tf.add(x, z), lambda: tf.square(y))
with tf.Session() as session:
    print(result.eval())
    initial_value = tf.truncated_normal([2, 2], 0.0, 0.001)
    print(initial_value)
    var = tf.constant([1,2,3,4],  name="asd")
    print(session.run(var))
