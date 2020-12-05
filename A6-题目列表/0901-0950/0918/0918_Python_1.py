from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))  # 3
    print(Solution().maxSubarraySumCircular([5, -3, 5]))  # 10
    print(Solution().maxSubarraySumCircular([3, -1, 2, -1]))  # 4
    print(Solution().maxSubarraySumCircular([3, -2, 2, -3]))  # 3
    print(Solution().maxSubarraySumCircular([-2, -3, -1]))  # -1
