**无财作为, 少有斗智, 既饶争时**

单例模式
========

确保一个类只有一个实例

## 1.9.1 使用模块
Python的模块天然是一个单例模式，第一次导入模块，会生成一个pyc文件，
当你第二次导入同一个模块时，实际是导入这个pyc文件

所以只需导入这个模块即可

```python
# single 文件
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()

# 导入, from single import Singleton
```

## 1.9.2 使用装饰器
将第一次实例化保存在一个字典中，第二次实例化时，直接取该实例

```python
def singleton(cls):
    _instance = {}
    def _singleton(*arg, **kwargs):
        if _instance.get(_instance) is not None:
            _instance[_instance] = cls(*arg, **kwargs)
        return _instance[_instance]

@singleton
class SingleTon:
    def __init__(self):
        pass
 
```

## 1.9.3 使用类
在实例化对象时，先是调用 `__new__` 方法，再调用 `__init__`方法

```python
import threading

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_isinstance'):
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    Singleton._instance = super().__new__(cls)
        return Singleton._instance
```

 