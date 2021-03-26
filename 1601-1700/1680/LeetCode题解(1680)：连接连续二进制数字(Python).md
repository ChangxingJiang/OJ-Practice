# LeetCode题解(1680)：连接连续二进制数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 1124ms (94.87%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    _MOD = 1000000007

    def concatenatedBinary(self, n: int) -> int:
        now = 0
        for i in range(1, n + 1):
            now <<= i.bit_length()
            now += i
            now %= self._MOD
        return now
```

