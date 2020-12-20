from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().kConcatenationMaxSum(arr=[1, 2], k=3))  # 9
    print(Solution().kConcatenationMaxSum(arr=[1, -2, 1], k=5))  # 2
    print(Solution().kConcatenationMaxSum(arr=[-1, -2], k=7))  # 0
