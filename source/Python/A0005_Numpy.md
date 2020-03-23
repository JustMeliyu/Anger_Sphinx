**无财作为， 少有斗智， 既饶争时**

# 1.5 numpy 用法
NumPy 最重要的一个特点是其 N 维数组对象 ndarray，
它是一系列同类型数据的集合， 以 0 下标为开始进行集合中元素的索引

## 1.新建
(1)array

    numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

- object: 数组或嵌套的数列
- dtype:  数组元素的数据类型， 可选
- copy:   对象是否需要复制， 可选
- order:  创建数组的样式， C为行方向， F为列方向， A为任意方向（默认）

```python

import numpy as np
d = [[0, 1, 2, 10],
     [12, 13, 100, 101],
     [102, 110, 112, 113]]
c = np.array(d, int)
print c    
```
result

    [[  0   1   2  10]
    [ 12  13 100 101]
    [102 110 112 113]]

(2)arange
根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

    numpy.arange(start, stop, step, dtype)
    

```python
import numpy as np
x = np.arange(10,20,2)  
print (x)
```
result

    [10  12  14  16  18]
    
(3)logspace
numpy.logspace 函数用于创建一个于等比数列。格式如下：

    np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
    
- start:    序列的起始值为：base ** start
- stop:     序列的终止值为：base ** stop, 如果endpoint为true，该值包含于数列中
- num:      要生成的等步长的样本数量，默认为50
- endpoint: 为True, 包含stop值, 否则不包含
- base:     对数log的底数, 默认为10

```python
import numpy as np
a = np.logspace(0,9,10,base=2)
print (a)
```

(4)empty
用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：

```python
import numpy as np 
x = np.empty([3, 2], dtype = int) 
print (x)
```
数组元素为随机值，因为它们未初始化

(5)zeros/ones
创建指定大小的数组，数组元素以 0/1 来填充

```python
import numpy as np
 
x = np.zeros(5) 
print(x)
x = np.ones([2,2], dtype = int)
print(x)

```

(6)reshape
按指定形状重新拆分
```python
import numpy as np
x = np.arange(4)
print x
# >>> [1 2 3 4]
x = x.reshape(2, 2)
print x
# >>> [[1 2]
#      [3 4]]
```
    
## 2.属性

NumPy 数组的维数称为秩（rank），一维数组的秩为 1，二维数组的秩为 2.
多少个

- ndim:     秩，即轴的数量或维度的数量
- shape:    数组的维度，对于矩阵，n 行 m 列
- size:     数组元素的总个数，相当于 .shape 中 n*m 的值
- dtype:    ndarray 对象的元素类型


## 3.常用函数

(1)mean

    numpy.mean(a, axis, dtype, out，keepdims )

对a求平均值, 如果指定axis, 则计算相应轴的评价值, 否则计算整个
