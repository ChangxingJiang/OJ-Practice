# LeetCode题解(1088)：易混淆数II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/confusing-number-ii/)（困难）

标签：数学、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 5308ms (70.97%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（暴力解法）：

```python
class Solution:
    _TABLE = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }
    _JUMP = {
        "2": "6",
        "3": "6",
        "4": "6",
        "5": "6",
        "7": "8"
    }

    def confusingNumberII(self, N: int) -> int:
        ans = 0

        i = 1
        while i <= N:
            s = str(i)
            l, r = 0, len(s) - 1
            differ = False
            while l <= r:
                if s[l] not in self._TABLE:
                    i = int(s[:l] + self._JUMP[s[l]] + "".join(["0"] * (len(s) - l - 1)))
                    break
                if s[r] not in self._TABLE:
                    i = int(s[:r] + self._JUMP[s[r]] + "".join(["0"] * (len(s) - r - 1)))
                    break
                elif s[l] != self._TABLE[s[r]]:
                    differ = True
                l += 1
                r -= 1
            else:
                if differ:
                    ans += 1
                i += 1

        return ans
```