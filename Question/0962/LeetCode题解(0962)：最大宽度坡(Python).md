# LeetCode题解(0962)：最大宽度坡(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-width-ramp/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 348ms (51.85%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        size = len(A)
        lst = sorted(range(size), key=A.__getitem__)
        min_val = size
        ans = 0
        for n in lst:
            min_val = min(min_val, n)
            ans = max(ans, n - min_val)
        return ans
```

