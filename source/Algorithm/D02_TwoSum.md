# 4.2 求两数之和

## 问题描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

具体实现方法有如下几种(皆基于python实现), 
**[github链接](https://github.com/JustMeliyu/Algorithm/blob/master/two_sum.py)**

## 算法一
两层遍历, 时间复杂度 O(n2), 空间复杂度 O(1)

```python
def two_sum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    print("result is null")
    return None, None
```

## 算法二
一层遍历, 用字典存储已遍历结果
时间复杂度 O(n), 空间复杂度 O(n)

```python
def two_sum2(nums, target):
    require_num = {}
    for index in range(len(nums)):
        if require_num.get(target - nums[index]) is not None:
            return require_num.get(target - nums[index]), index
        else:
            require_num[nums[index]] = index
    print("result is null")
    return None, None
```

