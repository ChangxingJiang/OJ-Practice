# LeetCode题解(1742)：盒子中小球的最大数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box/)（简单）

标签：数组

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(high-low)$ | $O(1)$     | 356ms (89.14%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = [0] * 50
        for num in range(lowLimit, highLimit + 1):
            val = 0
            while num > 0:
                val += num % 10
                num //= 10
            count[val] += 1
        return max(count)
```

