from typing import List


class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        pass


if __name__ == "__main__":
    # 43
    print(Solution().electricCarPlan(
        paths=[[1, 3, 3], [3, 2, 1], [2, 1, 3], [0, 1, 4], [3, 0, 5]], cnt=6, start=1, end=0,
        charge=[2, 10, 4, 1]))

    # 38
    print(Solution().electricCarPlan(
        paths=[[0, 4, 2], [4, 3, 5], [3, 0, 5], [0, 1, 5], [3, 2, 4], [1, 2, 8]], cnt=8, start=0, end=2,
        charge=[4, 1, 1, 3, 2]))
