# 4.1 快速排序

**定义：快速排序衍生与冒泡排序, 是在每一论排序时, 选择一个基准数, 
依次与每个元素比较, 将比基准数小的放到其左边, 比基准数大的放大右边, 
再分别对左边和右边做同样的操作, 一般选择第一个元素做基准数**

具体实现方法有如下几种(皆基于python实现)

### 方法一 
此方法会牺牲掉一些空间, 因为每一次都会增加两个数组
```python
# encoding: utf-8
def quick_sort1(my_list):
    if len(my_list) > 1:
        # 选择第一个元素做基准数(pivot)
        povit = my_list[0]
        left = []
        right = []
        for i in my_list[1:]:
            if i < povit:
                # 将小的放到一个数组
                left.append(i)
            else:
                # 大的放到另一个数组
                right.append(i)
        # 再分别递归两个数组, 将所有数组相加
        return quick_sort1(left) + [povit] + quick_sort1(right)
    else:
        return my_list
```

### 方法二
左右依次交替比较, 此方法会重复比较几次元素
```python
# encoding: utf-8
def quick_sort2(start, end, my_list):
    if start < end:
        i = start
        j = end
        pivot = my_list[i]
        while i < j:
            # 从第j个元素向前, 依次与pivot比较, 当出现比它小的时候, 停止,
            while i < j and my_list[j] >= pivot:
                j -= 1
            # 此时将此时的第j个元素赋值给第i个元素
            my_list[i] = my_list[j]

            # 从第i个元素向后, 依次与pivot比较, 当出现比它大的时候, 停止,
            while i < j and my_list[i] <= pivot:
                i += 1
            # 此时将此时的第i个元素赋值给第j个元素
            my_list[j] = my_list[i]
        # 当i与j相等时, 将povit赋值给第i个元素
        my_list[i] = pivot
        # 递归前半区
        quick_sort2(start, i - 1, my_list)
        # 递归后半区
        quick_sort2(i + 1, end, my_list)
    return my_list            
```

### 方法二变形

```python
# encoding: utf-8
def quick_sort3(my_list):
    if len(my_list) > 0:
        i = 0
        j = len(my_list) - 1
        pivot = my_list[i]

        while i < j:
            while (i < j) and (my_list[j] >= pivot):
                j -= 1
            my_list[i] = my_list[j]

            while (i < j) and (my_list[i] <= pivot):
                i += 1
            my_list[j] = my_list[i]

        my_list[i] = pivot
        # 递归前后半区, 结果求和
        return quick_sort3(my_list[:i]) + [my_list[i]] + quick_sort3(my_list[i + 1:])
    return my_list
``` 