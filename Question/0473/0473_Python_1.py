from typing import List


class Solution:
    def __init__(self):
        self.size = 0
        self.length = 0
        self.nums = []
        self.stats = [0] * 4

    def makesquare(self, nums: List[int]) -> bool:
        self.size = len(nums)
        self.nums = nums

        # 处理边不够的情况
        if self.size < 4:
            return False

        # 计算边长，处理边长不是整数的情况
        total = sum(nums)
        if sum(nums) % 4 != 0:
            return False
        self.length = total // 4

        # 处理是否有超长边
        if max(nums) > self.length:
            return False

        # 深度优先搜索
        return self.dfs(0)

    def dfs(self, idx):
        # 处理递归完成的情况
        if idx == self.size:
            return self.stats[0] == self.stats[1] == self.stats[2] == self.stats[3]

        for i in range(4):
            v = self.nums[idx]
            if self.stats[i] + v <= self.length:
                self.stats[i] += v
                if self.dfs(idx + 1):
                    return True
                self.stats[i] -= v

        return False


if __name__ == "__main__":
    print(Solution().makesquare([1, 1, 2, 2, 2]))  # True
    print(Solution().makesquare([3, 3, 3, 3, 4]))  # False
