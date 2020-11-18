from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))  # 4
    print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))  # 2
