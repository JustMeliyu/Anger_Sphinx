**无财作为, 少有斗智, 既饶争时**

1 一些python的小知识点
=========================

## 1.1 单下划线与双下划线变量的区别

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

## 1.2 一些基础方法

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
