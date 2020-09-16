# LeetCode题解(1513)：统计字符串中仅含1的子串数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-substrings-with-only-1s/)（中等）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 68ms (76.32%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        now = 0
        ans = 0
        for ch in s:
            if ch == "1":
                now += 1
                ans += now
            else:
                now = 0
        return ans % MOD
```