# LeetCode题解(1639)：统计只差一个字符的子串数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character/)（困难）

标签：动态规划、哈希表

| 解法           | 时间复杂度                                             | 空间复杂度   | 执行用时     |
| -------------- | ------------------------------------------------------ | ------------ | ------------ |
| Ans 1 (Python) | $O(H×(W+T))$ : W为单词数量 H为单词长度 T为目标单词长度 | $O(H×(W+T))$ | 2012ms (64%) |
| Ans 2 (Python) |                                                        |              |              |
| Ans 3 (Python) |                                                        |              |              |

解法一（动态规划）：

```python
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # 预处理单词列表
        # O(W×H) W为单词数量 H为单词长度
        size = len(words[0])
        counts = [collections.Counter() for _ in range(size)]
        for word in words:
            for i, ch in enumerate(word):
                counts[i][ch] += 1

        # 生成状态列表
        dp = [[0] * size for _ in range(len(target))]

        # 计算左上角
        if target[0] in counts[0]:
            dp[0][0] = counts[0][target[0]]

        # 计算第一行
        for j in range(1, size):
            dp[0][j] = dp[0][j - 1]
            if target[0] in counts[j]:
                dp[0][j] += counts[j][target[0]]

        # 计算其他位置
        for i in range(1, len(target)):
            for j in range(i, size):
                dp[i][j] = dp[i][j - 1]
                if target[i] in counts[j]:
                    dp[i][j] += dp[i - 1][j - 1] * counts[j][target[i]]

        return dp[-1][-1] % (10 ** 9 + 7)
```