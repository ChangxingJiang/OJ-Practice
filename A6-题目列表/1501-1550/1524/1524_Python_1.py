from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numOfSubarrays([1, 3, 5]))  # 4
    print(Solution().numOfSubarrays([2, 4, 6]))  # 0
    print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))  # 16
    print(Solution().numOfSubarrays([100, 100, 99, 99]))  # 4
    print(Solution().numOfSubarrays([7]))  # 1
