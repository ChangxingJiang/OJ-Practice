# LeetCode题解(0319)：灯泡开关(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bulb-switcher/)（中等）

标签：脑筋急转弯、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (31.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(pow(n, 0.5)) if n > 0 else 0
```