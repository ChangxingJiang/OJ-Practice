from typing import List


class Solution:
    def __init__(self):
        self.ans = set()
        self.nums = []
        self.now = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums

        self.count()

        return [list(i) for i in self.ans]

    def count(self, left=0):
        if left == len(self.nums):
            self.ans.add(tuple(self.now))
        else:
            self.now.append(self.nums[left])
            self.count(left + 1)
            self.now.pop()
            self.count(left + 1)


if __name__ == "__main__":
    # [
    #   [3],
    #   [1],
    #   [2],
    #   [1,2,3],
    #   [1,3],
    #   [2,3],
    #   [1,2],
    #   []
    # ]
    print(Solution().subsets([1, 2, 3]))
