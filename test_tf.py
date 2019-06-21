#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:36:07 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import tensorflow as tf

x = [[1,2,3],
     [1,2,3]]

xx = tf.cast(x,tf.float32)

mean_all = tf.reduce_mean(xx, keepdims=False)
mean_0 = tf.reduce_mean(xx, axis=0, keepdims=False)
mean_1 = tf.reduce_mean(xx, axis=1, keepdims=False)


with tf.Session() as sess:
    print("mean_all:",sess.run(mean_all))
    print("mean_0:", sess.run(mean_0))
    print("mean_1:", sess.run(mean_1))