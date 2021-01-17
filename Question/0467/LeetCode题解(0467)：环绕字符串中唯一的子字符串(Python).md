# LeetCode题解(0467)：环绕字符串中唯一的子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (98.87%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        now_val, now_num = float("inf"), 0
        dp = [0] * 26
        for ch in p:
            v = ord(ch) - 97
            if v != (now_val + 1) % 26:
                now_val, now_num = v, 1
            else:
                now_val += 1
                now_num += 1
            dp[v] = max(dp[v], now_num)
        return sum(dp)
```

