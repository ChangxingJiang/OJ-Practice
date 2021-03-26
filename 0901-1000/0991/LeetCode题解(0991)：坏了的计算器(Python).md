# LeetCode题解(0991)：坏了的计算器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/broken-calculator/)（中等）

标签：贪心算法、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logY)$  | $O(logY)$  | 36ms (74.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _BIG = 10 ** 9

    @functools.lru_cache(None)
    def brokenCalc(self, x: int, y: int) -> int:
        if x > y:
            return x - y
        if x == y:
            return 0

        if y % 2 == 0:
            return self.brokenCalc(x, y // 2) + 1
        else:
            return self.brokenCalc(x, y + 1) + 1
```

