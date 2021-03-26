# LeetCode题解(Offer46)：把数字翻译成字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (95.96%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (86.92%) |
| Ans 3 (Python) |            |            |               |

解法一（动态规划）：

```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)

        # 定义状态列表
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) < 26:
                dp[i + 1] = dp[i - 1] + dp[i]
            else:
                dp[i + 1] = dp[i]

        return dp[-1]
```

解法二（优化解法一）：

```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)

        # 定义状态列表
        last1, last2 = 1, 1

        for i in range(1, len(s)):
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) < 26:
                last1, last2 = last2, last1 + last2
            else:
                last1, last2 = last2, last2

        return last2
```