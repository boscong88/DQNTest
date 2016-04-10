'''
Module for the CNN
'''
# General
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

# tensorflow import
import tensorflow as tf

#
# Common CNN operations
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev = 0.01)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.01, shape = shape)
    return tf.Variable(initial)

def conv2d(x, W, stride):
    return tf.nn.conv2d(x, W, strides = [1, stride, stride, 1], padding = "SAME")

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = "SAME")

'''
3 conv layers + 1 fully connected layer
input: [None, 200, 200, 4] -- 3 frames of 200 x 200 representing 200 days stock 
prices and 1 frame of 200x200 representing 200 days of stock trading volume
conv layer 1: 
 in: [200x200x4] 
 kernel: 10x10x4x32, stride 4
 out: [50, 50, 32]
 max pooling 2x2: [25, 25, 32]
conv layer 2:
 in: [25, 25, 32]
 kernel: 5x5x32x64, stride 5
 out: [5,5,64]
 max pooling 2x2: [3,3,64]
conv layer 3:
 in: [3,3,64]
 kernel: 3x3x64x64, stride 1
 out: [3,3,64]
 max pooling 2x2: [2,2,64]
fully connected layer 1:
 in: [2,2,64]
 reshape: [256x1]
 relu: [256x1]
output:
 in: [256x]
 matrix multiplier: [3x1]
'''
def createNetwork():
    # network weights
    W_conv1 = weight_variable([10, 10, 4, 32])
    stride_1 = 4
    b_conv1 = bias_variable([32])

    W_conv2 = weight_variable([5, 5, 32, 64])
    stride_2 = 5
    b_conv2 = bias_variable([64])

    W_conv3 = weight_variable([3, 3, 64, 64])
    stride_3 = 1
    b_conv3 = bias_variable([64])
    
    W_fc1 = weight_variable([256, 256])
    b_fc1 = bias_variable([256])

    W_fc2 = weight_variable([256, 3])
    b_fc2 = bias_variable([3])

    # input layer
    input_layer = tf.placeholder("float", [None, 200, 200, 4])

    # hidden layers
    h_conv1 = tf.nn.relu(conv2d(s, W_conv1, stride_1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2, stride_2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3, stride_3) + b_conv3)
    h_pool3 = max_pool_2x2(h_conv3)

    h_pool3_flat = tf.reshape(h_pool3, [-1, 256])
    #h_conv3_flat = tf.reshape(h_conv3, [-1, 1600])

    h_fc1 = tf.nn.relu(tf.matmul(h_conv3_flat, W_fc1) + b_fc1)

    # readout layer
    readout = tf.matmul(h_fc1, W_fc2) + b_fc2

    return input_layer, readout, h_fc1


	