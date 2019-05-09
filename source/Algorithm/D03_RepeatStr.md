# 4.3 无重复字符最大长度

### 问题描述
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度, 以及对应字符串。

示例 1:

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
         
具体实现方法有如下几种(皆基于python实现), 
**[github链接](https://github.com/JustMeliyu/Algorithm/blob/master/repeat_str.py)**


### 算法一: 暴力法
两层循环, 第一层(i)从0开始, 第二层从(i+1)开始, 验证 i~j 中是否存在重复元素, 并保留其长度;

代码实现:
```python3
def length_longest_substring(s: str):
    """
    :type s: str
    :rtype: int, str
    """
    n = len(s)
    max_len = 0
    max_str = ''
    for i in range(n):
        for j in range(i + 1, n):
            # 如果后一个元素包含在当前范围
            if s[j] in s[i:j]:
                if j - i > max_len:
                    max_len = j - i
                    max_str = s[i:j]
                # 退出此次内循环
                break
        else:
            # 一直到最后一个元素都没有重复
            if n - i > max_len:
                # 如果此时最大, 则不用再往后, 因为已经到最后一个元素了, 退出外循环
                max_len = n - i
                max_str = s[i:]
                break
    return max_len, max_str
```
可以看出此方法时间复杂度 O(n2)

### 算法二: 划动窗口
在暴力法中, 简单易懂, 但是存在重复检查部分字段是否重复, 可对其进行优化;

- 从最开始, i=j=0, 依次将j递增, 直至遇到重复元素; 
- 再对每一个i做相同的事情, 注意此时j不变(因为我们已经验证了此时的 `i~j` 中没有重复元素); 
- 在这一个 i 中, 再将 j 递增, 检查是否存在重复元素; 
- 如此循环, 直至j到达最后一个元素.

```python3
def length_longest_substring2(s: str):
    i = j = max_len = 0
    n = len(s)
    max_str = ""
    while i < n and j < n:
        if s[j] not in s[i:j]:
            if j - i + 1 > ans:
                max_len = j - i + 1
                max_str = s[i:j + 1]
            j += 1
        else:
            i += 1
    return max_len, max_str
```
 可以看出, 此方法最多执行2n次, 则时间复杂度为 O(n)
 
### 算法三: 优化的划动窗口
在算法二中, 我们还可以进一步进行优化;

算法中, 我们在移动 i 时, 是依次递增1, 假如此时重复的元素在第 k 个, 我们也会重复检查第 `i~k` 个元素.

所以我们可以直接从第 `k + 1` 个开始, 继续对 j 递增, 获取 k 可以根据索引获取

代码实现

```python3
def length_longest_substring3(s: str):
    i = j = ans = 0
    n = len(s)
    max_str = ""
    while i < n and j < n:
        if s[j] not in s[i:j]:
            if j - i + 1 > ans:
                ans = j - i + 1
                max_str = s[i:j + 1]
            j += 1
        else:
            i = i + 1 + s[i:j].index(s[j])
            j += 1
    return ans, max_str
```

此方式最多执行n次, 时间复杂度为, O(n)





