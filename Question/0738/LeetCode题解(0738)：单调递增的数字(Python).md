# LeetCode题解(0738)：单调递增的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/monotone-increasing-digits/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 44ms (40.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = list(str(N))

        i = 1
        while i < len(s) and int(s[i - 1]) <= int(s[i]):
            i += 1

        if i == len(s):
            return N

        while i > 0 and s[i - 1] > s[i]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            i -= 1

        for i in range(i + 1, len(s)):
            s[i] = "9"

        return int("".join(s))
```