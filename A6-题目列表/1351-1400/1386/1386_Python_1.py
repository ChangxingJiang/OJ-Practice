from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))  # 4
    print(Solution().maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))  # 2
    print(Solution().maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))  # 4
