# LeetCode题解(1745)：回文串分割IV(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-partitioning-iv/)（困难）

标签：动态规划、广度优先搜索、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 3568ms (59.08%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        size = len(s)

        # ----- 构造子串是否为回文串的状态矩阵 -----
        # 时间复杂度: O(N^2)
        dp = [[False] * size for _ in range(size)]

        # 标记所有长度为1的子串为回文串
        for i in range(size):
            dp[i][i] = True

        # 判断所有长度为2的子串是否为回文串
        for i in range(size - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])

        # 检查所有长度的子串是否回文串
        for l in range(2, size):  # 遍历字符串长度
            for i in range(size - l):  # 遍历字符串开始位置
                j = i + l
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1] is True)

        # ----- 广度优先搜索寻找结果 -----
        # 时间复杂度: O(3×N^2) = O(N^2)
        now = {0}
        for _ in range(3):
            nxt = set()
            for i in now:
                for j in range(i, size):
                    if dp[i][j] is True:
                        nxt.add(j + 1)
            now = nxt

        # 返回最终结果
        return size in now
```

