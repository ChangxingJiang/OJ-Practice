# LeetCode题解(1318)：或运算的最小翻转次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (33.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        length = max(a.bit_length(), b.bit_length(), c.bit_length())
        for i in range(length):
            if c & (1 << i):
                if not a & (1 << i) and not b & (1 << i):
                    ans += 1
            else:
                if a & (1 << i):
                    ans += 1
                if b & (1 << i):
                    ans += 1

        return ans
```

