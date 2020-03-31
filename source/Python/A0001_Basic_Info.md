**无财作为, 少有斗智, 既饶争时**

1.1 一些python的小知识点
=========================
## 1.1.1 what's python
python 是一门解释性语言，但是实际上需要先编译，后一行一行解释为机器语言执行

当Python程序运行时，先将编译的结果保存在`PyCodeObject`中，
当程序运行结束时，Python解释器则将 `PyCodeObject` 写到`pyc`文件中。
第二次执行程序时，先看是否有`pyc`文件存在，如果有，则直接导入。`pyc` 是`PyCodeObject`持久化的一种表现。
在每次载入前，都会查看`pyc`文件和`py`文件的最后更新时间，不一致则重新生成一份`pyc`文件


## 1.1.1 单下划线与双下划线变量的区别

(1).`_xxx`

- `单下划线` 开头的变量相当于成员变量;
- 只有`类实例`, `子类实例` 能访问这些变量;
- 不能用 `from moudle import *` 导入


<font face="KaiTi" size=5>是一种约定, 实际上这并没有实现真正的私有化, 如果要强行使用也是能用的, 但是最好不要去使用或改变这些：</font>

(2).`__xxx`
 
- `双下划线` 是私有成员(私有变量/方法名);
- 只有 `类对象能访问`, `子类对象` 也不能访问;


<font face="KaiTi" size=5>是一种保护方式, 防止**子类的篡改和覆盖**</font>

(3).`__xxx__`

- 系统定义的名称, python里特殊方法专用;


<font face="KaiTi" size=5>自己定义变量不要使用这种方式</font>

## 1.1.2 一些基础方法

(1) `__new__`

实例化对象时，最先执行方法，之后再执行 `__init__`

(2) super()
调用父类(超类)中的方法

```python
class A:
    def __init__(self):
        print("1111")


class B(A):
    def __init__(self):
        print('222')
        super().__init__()


class C(B):
    def __init__(self):
        super().__init__()

class D(B):
    def __init__(self):
        super(D, self).__init__()

class E(B):
    def __init__(self):
        super(B, self).__init__()
```
`c = C()` 默认重写B类, 所以打印 
```text
1111
222
```

`d = D()` 先找到D类的父类(也就是B类)，将D的对象转化为B的对象，重写B类, 所以打印 
```text
1111
222
```

`e = E()` 先找到B类的父类(也就是A类)，重写A类, 所以打印 
```text
1111
```

## 1.1.3 lock

- `acquire(blocking=True, timeout=-1)` 申请锁
- `release` 释放锁
- `locked` Return true if the lock is acquired. 
- `RLock` 区别与 Lock,  RLock 可以在同一线程中多次加锁，但是acquire与release必须成对出现，而Lock在一个线程中只能被加锁一次

## 1.1.4 list, set, dict, tuple

(1). set 

`无序集合，不可重复，无切片，无索引。和dict一样，不可保存可变元素`
所以向set添加list会报错

```python
a = {1, 2, 3}
b = {3, 4}
a.add('python') # a = {1, 2, 3, 'python'}
b.update('python')  # b = {3, 4, 'p', 'y', 't', 'h', 'o', 'n'}
a.remove('python')  # a = {1, 2, 3}
c = a & b   # c = {3}
d = a | b   # d = {1, 2, 3, 4, 'p', 'y', 't', 'h', 'o', 'n'}
e = a - b   # e = {1, 2}
```
- add, 把一个整体加入到集合中
- update, 把要传入的元素拆分，作为个体放入到集合中
- remove, 删除一个集合中一个元素
- 可以做与或运算, 交集---`&` , 并集---`|`
- 可以相减

(2). list 

`有序集合, 可增减`

(3). tuple

`有序列表, 一旦初始化, 不可修改`

(4). dict 

`dict的key必须不可变对象dict 根据key用hash算法计算出value的位置，如果key可变，就会出现问题。
所以元组可以作为他的key，而list不行`

`dict查询效率高，但是消耗内存多；list、tuple查询效率低、但是消耗内存少`
