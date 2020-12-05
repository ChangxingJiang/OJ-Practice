from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]]))

    # 1
    print(Solution().minAreaFreeRect([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]))

    # 0
    print(Solution().minAreaFreeRect([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]))

    # 2
    print(Solution().minAreaFreeRect([[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]))
