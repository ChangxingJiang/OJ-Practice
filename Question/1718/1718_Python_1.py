from typing import List


class Solution:
    def __init__(self):
        self.size, self.dp = 0, []
        self.ans = []

    def constructDistancedSequence(self, n: int) -> List[int]:
        self.size = n * 2 - 1
        self.dp = [0] * self.size
        self.dfs(0, [i for i in range(n, 0, -1)])
        return self.ans

    def dfs(self, idx, num):
        # idx=当前已经确定到的坐标（self.dp中的坐标）；num=当前剩余的数
        # 剪枝条件1：已经找到结果（因为第1个找到的结果一定是最好的结果）
        if self.ans:
            return

        # 找到下一个还没有确定数值的位置
        while idx < self.size and self.dp[idx] != 0:
            idx += 1

        # 处理递归完成的情况
        if idx == self.size:
            self.ans = list(self.dp)
            return

        # 剪枝条件2：剩下的位置不足以放置剩下的最大的数
        if self.size - idx <= num[0] != 1:
            return

        # 优先选择更大的数放置在当前的位置中
        for i in range(len(num)):
            if num[i] != 1:
                if self.dp[idx + num[i]] == 0:
                    self.dp[idx] = self.dp[idx + num[i]] = num[i]
                    self.dfs(idx + 1, num[: i] + num[i + 1:])
                    self.dp[idx] = self.dp[idx + num[i]] = 0
            else:
                self.dp[idx] = num[i]
                self.dfs(idx + 1, num[: i] + num[i + 1:])
                self.dp[idx] = 0


if __name__ == "__main__":
    print(Solution().constructDistancedSequence(2))  # [2,1,2]
    print(Solution().constructDistancedSequence(3))  # [3,1,2,3,2]
    print(Solution().constructDistancedSequence(4))  # [4,2,3,2,4,3,1]
    print(Solution().constructDistancedSequence(5))  # [5,3,1,4,3,5,2,4,2]
    print(Solution().constructDistancedSequence(7))  # [7,5,3,6,4,3,5,7,4,6,2,1,2]
    print(Solution().constructDistancedSequence(8))  # [8,6,4,2,7,2,4,6,8,5,3,7,1,3,5]
