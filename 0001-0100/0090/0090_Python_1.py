import collections
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.nums = []
        self.count = []
        self.now = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = list(sorted(set(nums)))
        self.count = collections.Counter(nums)
        self.dfs(0)
        return self.ans

    def dfs(self, idx):
        # 递归完成
        if idx == len(self.nums):
            self.ans.append(list(self.now))
            return

        # 不选择当前数字
        self.dfs(idx + 1)
        for _ in range(1, self.count[self.nums[idx]] + 1):
            self.now.append(self.nums[idx])
            self.dfs(idx + 1)
        for _ in range(self.count[self.nums[idx]]):
            self.now.pop()


if __name__ == "__main__":
    # [
    #   [2],
    #   [1],
    #   [1,2,2],
    #   [2,2],
    #   [1,2],
    #   []
    # ]
    print(Solution().subsetsWithDup([1, 2, 2]))
