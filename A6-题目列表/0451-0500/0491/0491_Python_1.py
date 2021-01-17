from typing import List


class Solution:
    def __init__(self):
        self.ans = set()
        self.nums = []
        self.now = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs(0)
        return [list(elem) for elem in self.ans]

    def dfs(self, idx):
        if idx == len(self.nums):
            if len(self.now) >= 2:
                self.ans.add(tuple(self.now))
        else:
            if not self.now or self.now[-1] <= self.nums[idx]:
                self.now.append(self.nums[idx])
                self.dfs(idx + 1)
                self.now.pop()
            self.dfs(idx + 1)


if __name__ == "__main__":
    # [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
    print(Solution().findSubsequences([4, 6, 7, 7]))
