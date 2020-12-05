from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxVacationDays(flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                                     days=[[1, 3, 1], [6, 0, 3], [3, 3, 3]]))  # 12
    print(Solution().maxVacationDays(flights=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                                     days=[[1, 1, 1], [7, 7, 7], [7, 7, 7]]))  # 3
    print(Solution().maxVacationDays(flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                                     days=[[7, 0, 0], [0, 7, 0], [0, 0, 7]]))  # 21
