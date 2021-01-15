from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []
        self.now = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs(0)
        return self.ans

    def dfs(self, state):
        if state == (1 << len(self.nums)) - 1:
            self.ans.append(list(self.now))

        for i in range(len(self.nums)):
            if state & (1 << i) == 0:
                self.now.append(self.nums[i])
                self.dfs(state | (1 << i))
                self.now.pop()


if __name__ == "__main__":
    # [
    #   [1,2,3],
    #   [1,3,2],
    #   [2,1,3],
    #   [2,3,1],
    #   [3,1,2],
    #   [3,2,1]
    # ]
    print(Solution().permute([1, 2, 3]))
