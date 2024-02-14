[TOC]

# Overview

# Details

The rank of a tensor is its shape:

* Rank0 - scalar. A single number.
* Rank1 - array or list; t[i]
* Rank2 - matrix; t[i,j] or t[r,c]
* Rank3 - a 3D matrix; t[i,j,k]
* ...

Three types of tensor data:

* Constant; e.g. x = tf.constant("Hello")
* Placeholder
* Variable

dtypes are:

* float15, float32, float64 - IEEE
* bfloat16 - truncated float
* bcomplex64, bcomplex128
* int8, int16, int32, int64
* uint8, uint16, uint32, uint64
* qint8, qint16
* quint8, quint16
* bool
* string
* resource
* variant

TensorFlow steps are:

* Converted your data to **tensors**
* Define your **flow** or calculation graph.
* Run it.

## Activation Functions

* Linear (or Identity)
* Unit (or Binary Step)
* Sigmoid (or Logistic) 0 to 1
* Tanh -1 to 1
* ReLU = Rectified Linear Unit - relu(x) -> np.maximum(0, x)
* Softmax - probabilities of multiple outputs

tf.truncated_normal(shape) - returns a tensor of random weights; all in range -2*sigma and 2*sigma