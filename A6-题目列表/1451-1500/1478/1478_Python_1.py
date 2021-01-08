from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minDistance(houses=[1, 4, 8, 10, 20], k=3))  # 5
    print(Solution().minDistance(houses=[2, 3, 5, 12, 18], k=2))  # 9
    print(Solution().minDistance(houses=[7, 4, 6, 1], k=1))  # 8
    print(Solution().minDistance(houses=[3, 6, 14, 10], k=4))  # 0
