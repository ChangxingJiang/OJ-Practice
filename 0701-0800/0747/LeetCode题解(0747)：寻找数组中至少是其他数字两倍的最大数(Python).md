# LeetCode题解(0747)：寻找数组中至少是其他数字两倍的最大数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (86.21%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 44ms (86.21%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def dominantIndex(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    max1 = -1
    max2 = -1
    idx = -1
    for i in range(len(nums)):
        n = nums[i]
        if n > max1:
            max2 = max1
            max1 = n
            idx = i
        elif n > max2:
            max2 = n
    if max1 >= max2 * 2:
        return idx
    else:
        return -1
```

解法二：

```python
def dominantIndex(self, nums: List[int]) -> int:
    m = max(nums)
    if all([m >= 2 * n for n in nums if n != m]):
        return nums.index(m)
    else:
        return -1
```



