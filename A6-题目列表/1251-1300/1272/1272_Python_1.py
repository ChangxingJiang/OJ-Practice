from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[0,1],[6,7]]
    print(Solution().removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]))

    # [[0,2],[3,5]]
    print(Solution().removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]))
