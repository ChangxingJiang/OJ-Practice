from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[1,6],[8,10],[15,18]]
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

    # [[1,5]]
    print(Solution().merge(intervals=[[1, 4], [4, 5]]))
