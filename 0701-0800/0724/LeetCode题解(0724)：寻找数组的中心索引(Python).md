# LeetCode题解(0724)：寻找数组的中心索引(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-pivot-index/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 9104ms (11.77%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 56ms (95.05%)   |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 64ms (86.25%)   |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def pivotIndex(self, nums: List[int]) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i
    else:
        return -1
```

解法二（插值法）：

```python
def pivotIndex(self, nums: List[int]) -> int:
    differ = sum(nums)
    for i in range(len(nums)):
        if i > 0:
            differ -= nums[i] + nums[i - 1]
        else:
            differ -= nums[i]
        if differ == 0:
            return i
    else:
        return -1
```

解法三：

```python
def pivotIndex(self, nums: List[int]) -> int:
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        if left == (total - left - nums[i]):
            return i
        left += nums[i]
    else:
        return -1
```