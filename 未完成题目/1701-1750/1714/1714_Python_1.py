from typing import List


class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().solve(nums=[0, 1, 2, 3, 4, 5, 6, 7], queries=[[0, 3], [5, 1], [4, 2]]))  # [9,18,10]
    print(Solution().solve(nums=[100, 200, 101, 201, 102, 202, 103, 203], queries=[[0, 7]]))  # [303]
