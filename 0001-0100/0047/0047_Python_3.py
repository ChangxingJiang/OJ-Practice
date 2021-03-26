from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = []
        self.now = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def track_back():
            if len(self.now) == n:
                self.ans.append(self.now[:])
            tmp_set = set()
            for i in range(n):
                if i not in self.visited:
                    if nums[i] in tmp_set:
                        continue
                    tmp_set.add(nums[i])

                    self.visited.add(i)
                    self.now.append(nums[i])
                    track_back()
                    self.now.pop()
                    self.visited.remove(i)

        track_back()

        return self.ans


if __name__ == "__main__":
    # [
    #   [1,1,2],
    #   [1,2,1],
    #   [2,1,1]
    # ]
    print(Solution().permuteUnique([1, 1, 2]))
