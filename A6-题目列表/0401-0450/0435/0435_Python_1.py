from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))

    # 2
    print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))

    # 0
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]))
