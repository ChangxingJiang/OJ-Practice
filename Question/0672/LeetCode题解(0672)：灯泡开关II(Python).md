# LeetCode题解(0672)：灯泡开关II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bulb-switcher-ii/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (98.70%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n == 1:
            return 2 if m > 0 else 1
        if n == 2:
            return [1, 3][m] if m <= 1 else 4
        if n >= 3:
            return [1, 4, 7][m] if m <= 2 else 8
```

