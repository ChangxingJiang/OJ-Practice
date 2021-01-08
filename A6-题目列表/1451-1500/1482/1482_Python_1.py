from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))  # 3
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))  # -1
    print(Solution().minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))  # 12
    print(Solution().minDays(bloomDay=[1000000000, 1000000000], m=1, k=1))  # 1000000000
    print(Solution().minDays(bloomDay=[1, 10, 2, 9, 3, 8, 4, 7, 5, 6], m=4, k=2))  # 9
