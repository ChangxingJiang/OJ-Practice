# LeetCode题解(1771)：由子序列构造的最长回文串的长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximize-palindrome-length-from-subsequences/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 1888ms (85.44%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
import bisect


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s1, s2 = len(word1), len(word2)

        # 计算s1的最长回文子序列
        dp1 = [[0] * (s1 + 1) for _ in range(s1 + 1)]
        for i in range(s1):
            dp1[i][i] = 1

        for i in range(s1 - 1, -1, -1):
            for j in range(i + 1, s1):
                if word1[i] == word1[j]:
                    dp1[i][j] = dp1[i + 1][j - 1] + 2
                else:
                    dp1[i][j] = max(dp1[i + 1][j], dp1[i][j - 1])

        # 计算s2的最长回文子序列
        dp2 = [[0] * s2 for _ in range(s2)]
        for i in range(s2):
            dp2[i][i] = 1

        for i in range(s2 - 1, -1, -1):
            for j in range(i + 1, s2):
                if word2[i] == word2[j]:
                    dp2[i][j] = dp2[i + 1][j - 1] + 2
                else:
                    dp2[i][j] = max(dp2[i + 1][j], dp2[i][j - 1])

        # 生成word2中每个字母的出现位置列表
        position = [[] for _ in range(26)]
        for i2 in range(s2):
            position[ord(word2[i2]) - ord("a")].append(i2)

        # 定义状态矩阵：dp[i][j] （i为隐式）在word1中取到第i个字符，回文串长度为j时，word2被取到的最靠后的字符位置
        dp = [s2] + [-1] * s1

        now = 0  # 定义当前最长子串长度
        ans = 0  # 结果变量

        # 状态转移：逐个遍历word1中字符，并计算取到该字符时，各个回文串长度对应的word2被取到的最靠后的位置
        for i1 in range(s1):
            # 当前字符不找对应字符的情况就是当前状态矩阵，无需处理

            # 当前字符匹配了对应字符的情况
            ch1 = word1[i1]
            pos = position[ord(ch1) - ord("a")]
            for j in range(now, -1, -1):
                index = bisect.bisect_left(pos, dp[j]) - 1  # 寻找当前位置的最近匹配字符位置
                if index == -1:  # 已经没有可以匹配的情况
                    continue
                else:  # 寻找可以匹配的最靠后的位置
                    i2 = pos[index]
                    dp[j + 1] = max(dp[j + 1], i2)  # 计算当前最靠前的匹配位置
                    res = (j + 1) * 2 + max(dp1[i1 + 1][s1 - 1] if i1 < s1 else 0,
                                            dp2[0][i2 - 1] if i2 > 0 else 0)  # 计算当前匹配情况的最大结果

                    # print("i1 =", i1, ",", "i2 =", i2, "->",
                    #       (j + 1), "* 2", "+",
                    #       "max(", dp1[i1 + 1][s1 - 1] if i1 < s1 else 0, ",", dp2[0][i2 - 1] if i2 > 0 else 0, ")",
                    #       "=", res)

                    now = max(now, j + 1)  # 更新当前回文子序列最大长度
                    ans = max(ans, res)

        return ans
```

