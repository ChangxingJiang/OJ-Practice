import collections
from typing import List


# 哈希表、动态规划
# O(W×H+H×T) W为单词数量 H为单词长度 T为目标单词长度


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


if __name__ == "__main__":
    print(Solution().numWays(words=["acca", "bbbb", "caca"], target="aba"))  # 6
    print(Solution().numWays(words=["abba", "baab"], target="bab"))  # 4
    print(Solution().numWays(words=["abcd"], target="abcd"))  # 1
    print(Solution().numWays(words=["abab", "baba", "abba", "baab"], target="abba"))  # 16
