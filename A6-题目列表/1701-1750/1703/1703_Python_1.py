from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minMoves(nums=[1, 0, 0, 1, 0, 1], k=2))  # 1
    print(Solution().minMoves(nums=[1, 0, 0, 0, 0, 0, 1, 1], k=3))  # 5
    print(Solution().minMoves(nums=[1, 1, 0, 1], k=2))  # 0
