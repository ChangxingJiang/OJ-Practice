from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = set()
        self.now = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def track_back():
            if len(self.now) == len(nums):
                self.ans.add(tuple([nums[i] for i in self.now]))
            for i in range(len(nums)):
                if i not in self.visited:
                    self.visited.add(i)
                    self.now.append(i)
                    track_back()
                    self.now.pop()
                    self.visited.remove(i)

        track_back()

        return [list(e) for e in self.ans]


if __name__ == "__main__":
    # [
    #   [1,1,2],
    #   [1,2,1],
    #   [2,1,1]
    # ]
    print(Solution().permuteUnique([1, 1, 2]))
