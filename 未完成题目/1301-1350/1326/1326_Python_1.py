from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]))  # 1
    print(Solution().minTaps(n=3, ranges=[0, 0, 0, 0]))  # -1
    print(Solution().minTaps(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]))  # 3
    print(Solution().minTaps(n=8, ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]))  # 2
    print(Solution().minTaps(n=8, ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]))  # 1
